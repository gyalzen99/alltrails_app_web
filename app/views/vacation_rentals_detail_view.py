from rest_framework.views import View
from django.shortcuts import render

class VacationRentalsDetailView(View):
    def get(self, request):

        data = {}

        return render(
            request,
            'vacation_rentals/vacation_rentals_detail/vacation_rentals_detail.html',
            data,
        )