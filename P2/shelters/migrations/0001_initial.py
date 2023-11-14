# Generated by Django 4.2 on 2023-11-14 02:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShelterReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('text', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('shelter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='shelters.shelter')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shelter_reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShelterQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('type', models.CharField(choices=[('FILE', 'File'), ('CHECKBOX', 'Checkbox'), ('DATE', 'Date'), ('EMAIL', 'Email'), ('TEXT', 'Text'), ('NUMBER', 'Number')], default='TEXT', max_length=100)),
                ('shelter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shelter_questions', to='shelters.shelter')),
            ],
        ),
        migrations.CreateModel(
            name='PetListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('available', 'Available'), ('not_available', 'Not Available')], default='available', max_length=15)),
                ('shelter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listings', to='shelters.shelter')),
            ],
        ),
        migrations.CreateModel(
            name='PetApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('denied', 'Denied'), ('withdrawn', 'Withdrawn'), ('approved', 'Approved')], default='pending', max_length=15)),
                ('application_time', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to=settings.AUTH_USER_MODEL)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='shelters.petlisting')),
            ],
        ),
        migrations.CreateModel(
            name='AssignedQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.PositiveSmallIntegerField(blank=True, default=0)),
                ('required', models.BooleanField(default=True)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_questions', to='shelters.petlisting')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shelters.shelterquestion')),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=3000)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application_responses', to='shelters.petapplication')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shelters.assignedquestion')),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='shelters.petapplication')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application_comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
