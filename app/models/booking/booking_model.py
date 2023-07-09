from django.db import models
from django.contrib.auth.models import User
from utils.choices.payment_choice import PaymentChoices

class BookingModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking_detail')
    booking_type = models.CharField(max_length=200)
    number_of_people = models.IntegerField()
    start_day = models.DateField()
    phone_number = models.IntegerField(blank=True, null=True)
    payment_type = models.CharField(max_length=200, default=PaymentChoices.CASH_IN_FRONT.value, choices=PaymentChoices.choices)

    def __str__(self) -> str:
        return self.user.username