from django.db import models

from app.models.vacation_rentals.component.vacation_rentals_detail_model import VacationRentalsDetailModel

class VacationRentalsModel(models.Model):
    title = models.CharField(max_length=200, default='Vacation Rentals')
    vacation_rentals_detail = models.ManyToManyField(VacationRentalsDetailModel)

    def __str__(self) -> str:
        return self.title