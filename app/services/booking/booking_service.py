from datetime import datetime
from app.models.booking.booking_model import BookingModel


class BookingService:
    def save_user_booking_detail(
            self,
            request,
    ):
        user = request.user
        booking_type = request.POST['booking_type']
        phone_number = request.POST['phone_number']
        number_of_people = request.POST['number_of_people']
        start_day = datetime.strptime(request.POST['start_day'], '%Y-%m-%d').date()
        payment_type = request.POST['payment_type']

        if not user.is_authenticated:
            return False, 'Invalid User'

        if  phone_number == None or start_day is None or payment_type == '' or number_of_people is None:
            return False, 'Please fill all the field'

        booking = BookingModel(
            user=user,
            booking_type = booking_type,
            number_of_people = number_of_people,
            start_day = start_day,
            phone_number = phone_number,
            payment_type = payment_type,
        )

        booking.save()
        return True, 'Successfully Saved'