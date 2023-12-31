# Generated by Django 4.2.2 on 2023-07-04 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_hotelmodel_hotel_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelDetailModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=200)),
                ('hotel_image', models.ImageField(upload_to='images/hotels')),
                ('hotel_info', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='hotelmodel',
            name='hotel_image',
        ),
        migrations.RemoveField(
            model_name='hotelmodel',
            name='hotel_name',
        ),
        migrations.RemoveField(
            model_name='hotelmodel',
            name='hotel_detail',
        ),
        migrations.AddField(
            model_name='hotelmodel',
            name='hotel_detail',
            field=models.ManyToManyField(to='app.hoteldetailmodel'),
        ),
    ]
