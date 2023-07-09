from django.db import models

from app.models.detail.detail_model import DetailModel

class PopularDestinationModel(models.Model):
    title = models.CharField(max_length=40)
    image_path = models.ImageField(upload_to='images/home/popular_destination/')
    popular_destination_detail = models.ForeignKey(DetailModel, on_delete=models.DO_NOTHING)

    def __str__(self)-> str:
        return self.title