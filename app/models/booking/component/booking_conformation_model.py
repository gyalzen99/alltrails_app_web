from django.db import models
from app.models.booking.booking_model import BookingModel

class BookingConformationModel(models.Model):
    booking_detail = models.ForeignKey(BookingModel, on_delete=models.CASCADE, related_name='booking_detail')
    total_price = models.IntegerField()
    booking_date = models.DateField(auto_now_add=True)
    booking_time = models.TimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.booking_detail__user.username