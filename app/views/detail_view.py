from rest_framework import views
from django.shortcuts import render
from app.models.home.component.kathmandu_tour_model import KathmanduTourModel
from app.models.home.component.popular_destination_model import PopularDestinationModel

from app.services.detail.detail_service import DetailService

class DetailView(views.View):
    def get(self, request):
        popular_destination_data_id = request.GET.get('popular_destination_data_id')
        kathmandu_tour_data_id = request.GET.get('kathmandu_tour_data_id')

        popular_destination_object = None
        kathmandu_tour_object = None
        if kathmandu_tour_data_id == None:
            popular_destination_object = PopularDestinationModel.objects.get(id=popular_destination_data_id)

        if popular_destination_data_id == None:
            kathmandu_tour_object = KathmanduTourModel.objects.get(id=kathmandu_tour_data_id)

        detail_service = DetailService()
        data = detail_service.get_data(
            popular_destination_object = popular_destination_object,
            kathmandu_tour_object = kathmandu_tour_object,
        )

        return render(
            request,
            'detail_layout.html',
            data,
        )