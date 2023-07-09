from rest_framework.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import AnonymousUser

from app.services.booking.booking_service import BookingService

class BookingView(View):
    def get(self, request):
        booking_type = request.GET.get('booking')
        user = request.user

        if not user.is_authenticated:
            return redirect('sign_in')

        data = {
            'user': user,
            'booking_type': booking_type,
        }

        return render(
            request,
            'booking/booking.html',
            data,
        )

    def post(self, request):
        booking_service = BookingService()

        is_booking_successful, booking_message = booking_service.save_user_booking_detail(
            request=request,
        )

        if is_booking_successful:
            return redirect('booking_conformation')

        return redirect('booking')