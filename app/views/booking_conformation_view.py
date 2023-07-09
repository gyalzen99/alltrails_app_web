from rest_framework.views import View
from django.shortcuts import render, redirect
from app.models.booking.booking_model import BookingModel

from app.services.booking.component.booking_conformation_service import BookingConformationService

class BookingConformationView(View):
    def get(self, request):
        user = request.user

        booking_conformation_service = BookingConformationService()

        data = booking_conformation_service.get_data(
            user = user,
        )

        return render(
            request,
            'booking/component/booking_conformation.html',
            data,
        )

    def post(self, request):
        id = request.GET.get('id')
        booking_object = BookingModel.objects.filter(id=id)
        booking_object.delete()

        if booking_object.exists():
            booking_object.delete()
            return


        return redirect('home')
