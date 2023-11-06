from rest_framework import serializers
from shelters.models.pet_application import PetApplication, PetListing
from shelters.models.application_response import Question, ListingQuestion, Answer
from shelters import models


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class PetApplicationSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = PetApplication
        fields = '__all__'


class ShelterQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question']

    def create(self, validated_data):
        user = self.context['request'].user
        # pretty sure this logic can be moved to the view, we can have a
        # permission method for this
        if not hasattr(user, 'shelter'):
            raise serializers.ValidationError("You are not a shelter")
        question = Question.objects.create(**validated_data, shelter=user.shelter)
        return question


class ListingQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingQuestion
        fields = ['id', 'question']


class PetApplicationFormSerializer(serializers.Serializer):
    # on post, each question associated with the listing should be a field in the serializer
    # listing_questions = ListingQuestionSerializer(many=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.listing_id = self.context.get('request').parser_context.get('kwargs').get('listing_id')
        listing_questions = ListingQuestion.objects.filter(listing_id=self.listing_id)

        question_dict = {}
        # for each question that belongs to this pet listing, make a field for it
        # may need to add more data such as type of the question so corresponding fields can be used
        for listing_question in listing_questions:
            question_string = listing_question.question.question
            question_dict[str(listing_question.id)] = serializers.CharField(label=question_string, required=False)
        self.fields.update(question_dict)

    def create(self, validated_data):
        # should create an application instance here as well as for each response create answers
        application = PetApplication.objects.create(listing_id=self.listing_id, applicant=self.context['request'].user)
        for key, value in validated_data.items():
            Answer.objects.create(answer=value, question_id=key, application=application)
        return application


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class PetListingSerializer(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(many=True, queryset=Question.objects.all(), write_only=True)
    listing_questions = serializers.SerializerMethodField(read_only=True)

    # user can select the questions, which will create new rows in listing questions
    class Meta:
        # for listing or creating a serializer
        model = PetListing
        fields = '__all__'

    def create(self, validated_data):
        questions_data = validated_data.pop('questions')
        pet_listing = PetListing.objects.create(**validated_data)
        for question in questions_data:
            ListingQuestion.objects.create(listing=pet_listing, question=question)
        return pet_listing

    def update(self, instance, validated_data):
        # if question is not already in the listing then update it
        questions_data = validated_data.pop('questions')
        # remove the ones that no longer exist
        new_question_ids = [q.id for q in questions_data]
        # Get all questions that belong to this pet listing
        existing_questions = ListingQuestion.objects.filter(listing=instance)
        existing_question_ids = [q.question.id for q in existing_questions]

        for question in questions_data:
            if question.id not in existing_question_ids:
                ListingQuestion.objects.create(listing=instance, question=question)

        for existing_question in existing_questions:
            if existing_question.question.id not in new_question_ids:
                existing_question.delete()

        # for question in questions_data:
        return super().update(instance, validated_data)

    def get_listing_questions(self, obj):
        listing_questions = ListingQuestion.objects.filter(listing=obj)
        return ListingQuestionSerializer(listing_questions, many=True).data


class ShelterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shelter
        fields = '__all__'
