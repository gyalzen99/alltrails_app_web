from rest_framework.views import View
from django.shortcuts import render
from app.models.things_to_do.things_to_do_model import ThingsToDoModel

from app.services.things_to_do.things_to_do_service import ThingsToDoService

class ThingsToDoView(View):
    def get(self, request):
        things_to_do_service = ThingsToDoService()
        things_to_do_object = ThingsToDoModel.objects.first()

        data = things_to_do_service.getData(
            things_to_do_object=things_to_do_object,
        )

        return render(
            request,
           'things_to_do/things_to_do.html',
            data,
        )