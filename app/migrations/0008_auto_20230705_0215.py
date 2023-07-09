# Generated by Django 3.2.13 on 2023-07-05 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20230705_0133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='culturetourmodel',
            old_name='culture_tour_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='culturetourmodel',
            old_name='culture_tour_info',
            new_name='info',
        ),
        migrations.RenameField(
            model_name='culturetourmodel',
            old_name='culture_tour_location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='culturetourmodel',
            old_name='culture_tour_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='foodtourmodel',
            old_name='food_tour_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='foodtourmodel',
            old_name='food_tour_info',
            new_name='info',
        ),
        migrations.RenameField(
            model_name='foodtourmodel',
            old_name='food_tour_location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='foodtourmodel',
            old_name='food_tour_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='treakmodel',
            old_name='treak_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='treakmodel',
            old_name='treak_info',
            new_name='info',
        ),
        migrations.RenameField(
            model_name='treakmodel',
            old_name='treak_location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='treakmodel',
            old_name='treak_title',
            new_name='title',
        ),
    ]
