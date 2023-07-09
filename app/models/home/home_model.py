from django.db import models
from .component.popular_destination_model import PopularDestinationModel
from .component.kathmandu_tour_model import KathmanduTourModel

class HomeModel(models.Model):
    image_name = models.CharField(max_length=40)
    home_main_image = models.ImageField(upload_to='images/home')
    popular_destination = models.ManyToManyField(PopularDestinationModel)
    kathmandu_tour = models.ManyToManyField(KathmanduTourModel)

    def __str__(self) -> str:
        return self.image_name