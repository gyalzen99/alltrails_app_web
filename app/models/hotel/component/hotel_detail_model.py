from django.db import models

from app.models.hotel.component.hotel_service_model import HotelServiceModel
from app.models.user_reviews.user_review_model import UserReviewModel

class HotelDetailModel(models.Model):
    hotel_name = models.CharField(max_length=200)
    hotel_image = models.ImageField(upload_to='images/hotels')
    hotel_info = models.TextField()
    hotel_service_detail = models.ForeignKey(HotelServiceModel, on_delete=models.CASCADE, related_name='hotel_service_detail')
    hotel_review = models.ManyToManyField(UserReviewModel, blank=True)

    def __str__(self) -> str:
        return self.hotel_name