from django.contrib.auth.models import User

from app.models.booking.booking_model import BookingModel

class BookingConformationService:
    def get_data(
        self,
        user: User
    ):
        username = user.username

        booking_detail: BookingModel =  user.booking_detail.all().first()

        data = {
            'id': booking_detail.id,
            'username': username,
            'booking_detail': booking_detail
        }

        return data