from rest_framework.views import View
from django.shortcuts import render
from app.models.hotel.hotel_model import HotelModel

from app.services.hotel.hotel_service import HotelService

class HotelView(View):
    def get(self, request):
        hotel_object = HotelModel.objects.first()
        hotel_service = HotelService()

        data = hotel_service.getData(hotel_object=hotel_object)
        return render(
            request,
            'hotel/hotel.html',
            data,
        )