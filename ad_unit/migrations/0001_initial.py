# Generated by Django 4.1.5 on 2023-01-09 17:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdUnit',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=256)),
                ('language', models.CharField(max_length=256)),
                ('device', models.CharField(max_length=256)),
                ('os', models.CharField(max_length=10)),
                ('browser', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'unique_together': {('country', 'language', 'device', 'os', 'browser')},
            },
        ),
    ]
