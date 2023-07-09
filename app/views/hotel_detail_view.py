from rest_framework.views import View
from django.shortcuts import render
from app.models.hotel.component.hotel_detail_model import HotelDetailModel
from app.models.hotel.hotel_model import HotelModel

from app.services.hotel.hotel_detail.hotel_detail_service import HotelDetailService

class HotelDetailView(View):
    def get(self, request):
        hotel_detail_page = 'hotel/hotel_detail/hotel_detail.html'
        hotel_detail_id = request.GET.get('hotel_detail_id')
        hotel_detail_object = HotelDetailModel.objects.get(id=hotel_detail_id)

        hotel_detail_service = HotelDetailService()
        data = hotel_detail_service.getData(hotel_detail_object=hotel_detail_object)

        return render(
            request,
            hotel_detail_page,
            data
        )