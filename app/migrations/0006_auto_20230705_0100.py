# Generated by Django 3.2.13 on 2023-07-05 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_hotelmodel_hotel_review_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CultureTourModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('culture_tour_title', models.CharField(max_length=200)),
                ('culture_tour_location', models.CharField(max_length=200)),
                ('culture_tour_info', models.TextField()),
                ('culture_tour_image', models.ImageField(upload_to='images/things_to_do/culture_tour')),
            ],
        ),
        migrations.CreateModel(
            name='FoodTourModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_tour_title', models.CharField(max_length=200)),
                ('food_tour_location', models.CharField(max_length=200)),
                ('food_tour_info', models.TextField()),
                ('food_tour_image', models.ImageField(upload_to='images/things_to_do/food_tour')),
            ],
        ),
        migrations.CreateModel(
            name='ThingsToDoDetailModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thing_name', models.CharField(max_length=200)),
                ('thing_image', models.ImageField(upload_to='images/things_to_do')),
                ('culture_tour', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='culture_tour', to='app.culturetourmodel')),
                ('food_tour', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='food_tour', to='app.foodtourmodel')),
            ],
        ),
        migrations.CreateModel(
            name='TreakModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treak_title', models.CharField(max_length=200)),
                ('treak_location', models.CharField(max_length=200)),
                ('treak_info', models.TextField()),
                ('treak_image', models.ImageField(upload_to='images/things_to_do/treak')),
            ],
        ),
        migrations.CreateModel(
            name='ThingsToDoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Things to do', max_length=200)),
                ('culture_tour_details', models.ManyToManyField(related_name='culture_tour_detail', to='app.ThingsToDoDetailModel')),
                ('food_tour_details', models.ManyToManyField(related_name='food_tour_details', to='app.ThingsToDoDetailModel')),
                ('treak_details', models.ManyToManyField(related_name='treak_details', to='app.ThingsToDoDetailModel')),
            ],
        ),
        migrations.AddField(
            model_name='thingstododetailmodel',
            name='treak',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='treak', to='app.treakmodel'),
        ),
    ]
