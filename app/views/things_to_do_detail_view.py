from rest_framework.views import View
from django.shortcuts import render
from app.models.things_to_do.component.culture_tour_model import CultureTourModel
from app.models.things_to_do.component.food_tour_model import FoodTourModel
from app.models.things_to_do.component.treak_model import TreakModel
from app.services.things_to_do.things_to_do_detail.things_to_do_detail_service import ThingsToDoDetailService

from app.services.things_to_do.things_to_do_service import ThingsToDoService

class ThingsToDoDetailView(View):
      def get(self, request):
        culture_tour_id = request.GET.get('culture_tour_id')
        food_tour_id = request.GET.get('food_tour_id')
        treak_id = request.GET.get('treak_id')
        things_to_do_service = ThingsToDoDetailService()
        data = None

        if culture_tour_id != None:
            things_to_do_detail_object = CultureTourModel.objects.get(id=culture_tour_id)
            data = things_to_do_service.getData(
                things_to_do_detail_object=things_to_do_detail_object,
            )
        if food_tour_id != None:
            things_to_do_detail_object = FoodTourModel.objects.get(id=food_tour_id)
            data = things_to_do_service.getData(
                things_to_do_detail_object=things_to_do_detail_object,
            )
        if treak_id != None:
            things_to_do_detail_object = TreakModel.objects.get(id=treak_id)
            data = things_to_do_service.getData(
                things_to_do_detail_object=things_to_do_detail_object,
            )

        return render(
            request,
            'things_to_do/things_to_do_detail/things_to_do_detail.html',
            data,
        )