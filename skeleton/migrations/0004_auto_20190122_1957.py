# Generated by Django 2.1.3 on 2019-01-22 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skeleton', '0003_auto_20190122_1837'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='pointsA',
            new_name='points_A',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='pointsB',
            new_name='points_B',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='teamA',
            new_name='team_A',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='teamB',
            new_name='team_B',
        ),
    ]
