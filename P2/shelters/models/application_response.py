from django.db import models
from .pet_application import PetApplication, PetListing
from .shelter import Shelter


# each question is owned by a shelter
class ShelterQuestion(models.Model):
    # the types here will result in corresponding fields
    FILE = 'FILE'
    CHECKBOX = 'CHECKBOX'
    DATE = 'DATE'
    EMAIL = 'EMAIL'
    TEXT = 'TEXT'
    NUMBER = 'NUMBER'
    QUESTION_TYPE_CHOICES = (
        (FILE, 'File'),
        (CHECKBOX, 'Checkbox'),
        (DATE, 'Date'),
        (EMAIL, 'Email'),
        (TEXT, 'Text'),
        (NUMBER, 'Number')
    )
    shelter = models.ForeignKey(Shelter, related_name='shelter_questions', on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)
    type = models.CharField(choices=QUESTION_TYPE_CHOICES, max_length=100, default=TEXT)
    required = models.BooleanField(default=True)

    def __str__(self):
        return self.question


class AssignedQuestion(models.Model):
    question = models.ForeignKey(ShelterQuestion, on_delete=models.CASCADE)
    listing = models.ForeignKey(PetListing, related_name='assigned_questions', on_delete=models.CASCADE)
    rank = models.PositiveSmallIntegerField(blank=True, default=0)


class ApplicationResponse(models.Model):
    answer = models.CharField(max_length=3000)  # 3000 chars is approx 500 words
    question = models.ForeignKey(AssignedQuestion, on_delete=models.CASCADE)
    application = models.ForeignKey(PetApplication, related_name='application_responses', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.question}: {self.answer}'