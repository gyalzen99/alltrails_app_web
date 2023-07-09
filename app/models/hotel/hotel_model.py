from django.db import models
from app.models.hotel.component.hotel_detail_model import HotelDetailModel

class HotelModel(models.Model):
    title = models.CharField(max_length=200)
    hotel_detail = models.ManyToManyField(HotelDetailModel)

    def __str__(self) -> str:
        return self.title