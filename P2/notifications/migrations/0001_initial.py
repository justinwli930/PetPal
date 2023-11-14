# Generated by Django 4.2 on 2023-11-14 04:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationPreferences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_message', models.BooleanField(default=True)),
                ('application_status_change', models.BooleanField(default=True)),
                ('pet_listing', models.BooleanField(default=True)),
                ('application', models.BooleanField(default=True)),
                ('review', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='notification_preferences', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.CharField(choices=[('applicationMessage', 'New Application Message'), ('applicationSatusChange', 'Application Status Change'), ('petListing', 'New Pet Listing'), ('application', 'New Application'), ('review', 'New Review')], max_length=30)),
                ('associated_model_id', models.PositiveIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('read', models.BooleanField(default=False)),
                ('associated_model_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='associated_model', to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]