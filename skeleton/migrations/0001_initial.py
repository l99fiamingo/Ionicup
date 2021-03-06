# Generated by Django 2.1.3 on 2019-01-24 03:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllStarGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('rules', models.CharField(blank=True, max_length=999)),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Court',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=16)),
                ('importance', models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=16)),
                ('format', models.CharField(choices=[('Round-Robin', "All'italiana"), ('Elimination', 'Ad eliminazione')], default='Round-Robin', max_length=32)),
                ('number_of_teams', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('importance', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=16)),
                ('last_name', models.CharField(max_length=16)),
                ('jersey_size', models.CharField(blank=True, choices=[('XXS', 'XXS'), ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], max_length=4)),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points_A', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('points_B', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('number', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('sb_current_sixth', models.CharField(blank=True, choices=[('1', 'Primo'), ('2', 'Secondo'), ('3', 'Terzo'), ('4', 'Quarto'), ('5', 'Quinto'), ('6', 'Sesto'), ('7', 'Supplementare')], max_length=16)),
                ('sb_timer', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('sb_partial_A', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('sb_partial_B', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('sb_1_sixth_A', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('sb_1_sixth_B', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('sb_2_sixth_A', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('sb_2_sixth_B', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('sb_3_sixth_A', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('sb_3_sixth_B', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('sb_4_sixth_A', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('sb_4_sixth_B', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('sb_5_sixth_A', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('sb_5_sixth_B', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('sb_6_sixth_A', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('sb_6_sixth_B', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('sb_7_sixth_A', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('sb_7_sixth_B', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('sb_color_A', models.CharField(blank=True, choices=[('Black', 'Nero'), ('Silver', 'Argento'), ('Gray', 'Grigio'), ('White', 'Bianco'), ('Maroon', 'Amaranto'), ('Red', 'Rosso'), ('Orange', 'Arancione'), ('Purple', 'Viola'), ('Fuchsia', 'Fucsia'), ('Green', 'Verde Scuro'), ('Lime', ' Verde Lime'), ('Yellow', 'Giallo'), ('Navy', 'Blue Navy'), ('Blue', 'Blu'), ('Teal', 'Verde Acqua'), ('Azure', 'Azzurro'), ('Pink', 'Rosa')], max_length=16)),
                ('sb_color_B', models.CharField(blank=True, choices=[('Black', 'Nero'), ('Silver', 'Argento'), ('Gray', 'Grigio'), ('White', 'Bianco'), ('Maroon', 'Amaranto'), ('Red', 'Rosso'), ('Orange', 'Arancione'), ('Purple', 'Viola'), ('Fuchsia', 'Fucsia'), ('Green', 'Verde Scuro'), ('Lime', ' Verde Lime'), ('Yellow', 'Giallo'), ('Navy', 'Blue Navy'), ('Blue', 'Blu'), ('Teal', 'Verde Acqua'), ('Azure', 'Azzurro'), ('Pink', 'Rosa')], max_length=16)),
                ('court', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='matches', to='skeleton.Court')),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rounds', to='skeleton.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('games_played', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('wins', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('losses', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('points_made', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('points_conceded', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('goals_made', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('goals_conceded', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='skeleton.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=16)),
                ('protected', models.BooleanField(default=False)),
                ('precedent_stage', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_stage', to='skeleton.Stage')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
                ('short_name', models.CharField(blank=True, max_length=12)),
                ('city', models.CharField(blank=True, max_length=36)),
                ('slug', models.SlugField(blank=True)),
                ('color', models.CharField(blank=True, choices=[('Black', 'Nero'), ('Silver', 'Argento'), ('Gray', 'Grigio'), ('White', 'Bianco'), ('Maroon', 'Amaranto'), ('Red', 'Rosso'), ('Orange', 'Arancione'), ('Purple', 'Viola'), ('Fuchsia', 'Fucsia'), ('Green', 'Verde Scuro'), ('Lime', ' Verde Lime'), ('Yellow', 'Giallo'), ('Navy', 'Blue Navy'), ('Blue', 'Blu'), ('Teal', 'Verde Acqua'), ('Azure', 'Azzurro'), ('Pink', 'Rosa')], default='White', max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(blank=True, max_length=16)),
                ('event', models.CharField(blank=True, max_length=32)),
                ('initial', models.BooleanField(default=False)),
                ('day', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='times', to='skeleton.Day')),
                ('precedent_time', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_time', to='skeleton.Time')),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=99)),
                ('title', models.CharField(blank=True, max_length=99)),
                ('slug', models.SlugField(blank=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('human_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='skeleton.Human')),
                ('cell_number', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('email', models.EmailField(blank=True, max_length=64, null=True)),
            ],
            bases=('skeleton.human',),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('human_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='skeleton.Human')),
                ('year_of_birth', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2100)])),
                ('jersey_number', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)])),
                ('all_star_game', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='players', to='skeleton.AllStarGame')),
            ],
            bases=('skeleton.human',),
        ),
        migrations.AddField(
            model_name='team',
            name='tournament',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='skeleton.Tournament'),
        ),
        migrations.AddField(
            model_name='stage',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stages', to='skeleton.Tournament'),
        ),
        migrations.AddField(
            model_name='score',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='skeleton.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='round',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='skeleton.Round'),
        ),
        migrations.AddField(
            model_name='match',
            name='team_A',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matches_A', to='skeleton.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='team_B',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matches_B', to='skeleton.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='time',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='matches', to='skeleton.Time'),
        ),
        migrations.AddField(
            model_name='group',
            name='stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='skeleton.Stage'),
        ),
        migrations.AddField(
            model_name='day',
            name='tournament',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='days', to='skeleton.Tournament'),
        ),
        migrations.AddField(
            model_name='court',
            name='tournament',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courts', to='skeleton.Tournament'),
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='skeleton.Team'),
        ),
        migrations.AddField(
            model_name='coach',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coaches', to='skeleton.Team'),
        ),
    ]
