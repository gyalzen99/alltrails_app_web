from rest_framework.views import View
from django.shortcuts import render

from app.models.vacation_rentals.vacation_rentals_model import VacationRentalsModel
from app.services.vacation_rentals.vacation_rentals_service import VacationRentalsService

class VacationRentalsView(View):
    def get(self, request):
        vacation_rental_object =  VacationRentalsModel.objects.first()

        vacation_rental_service = VacationRentalsService()
        data = vacation_rental_service.getData(
            vacation_rental_object = vacation_rental_object,
        )

        return render(
            request,
            'vacation_rentals/vacation_rentals.html',
            data,
        )