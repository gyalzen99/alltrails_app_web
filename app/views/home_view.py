from django.shortcuts import render
from rest_framework.views import View
from ..models.home.home_model import HomeModel
from ..models.home.component.kathmandu_tour_model import KathmanduTourModel
from ..models.home.component.popular_destination_model import PopularDestinationModel
from ..services.home.home_service import HomeService

class HomeView(View):
    def get(self, request):
        home_object = HomeModel.objects.first()
        kathmandu_tour_object = KathmanduTourModel.objects.all()
        popular_destination_object = PopularDestinationModel.objects.all()

        home_service_object = HomeService()

        data = home_service_object.getData(
            home_object = home_object,
            kathmandu_tour_object=kathmandu_tour_object,
            popular_destination_object=popular_destination_object,
        )

        return render(
            request,
            'home/home.html',
            data,
        )