from django.db import models

from app.models.things_to_do.component.culture_tour_model import CultureTourModel
from app.models.things_to_do.component.food_tour_model import FoodTourModel
from app.models.things_to_do.component.treak_model import TreakModel

class ThingsToDoModel(models.Model):
    title = models.CharField(max_length=200, default='Things to do')
    culture_tour = models.ManyToManyField(CultureTourModel, related_name='culture_tour')
    food_tour = models.ManyToManyField(FoodTourModel, related_name='food_tour')
    treak = models.ManyToManyField(TreakModel, related_name='treak')

    def __str__(self) -> str:
        return self.title