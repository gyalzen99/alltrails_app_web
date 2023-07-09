from django.db import models

from utils.choices.vacation_choices import RoomChoices

class VacationRentalsDetailModel(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/vacation')
    room_type = models.CharField(max_length=200, default=RoomChoices.PrivateRoom)
    location = models.CharField(max_length=200)
    number_of_bed_room = models.IntegerField(default=1)
    number_of_bath_room = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.name