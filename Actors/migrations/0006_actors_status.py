# Generated by Django 5.0 on 2023-12-08 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Actors', '0005_remove_actors_userid_actors_actor_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='actors',
            name='Status',
            field=models.CharField(default='Active', max_length=20),
        ),
    ]