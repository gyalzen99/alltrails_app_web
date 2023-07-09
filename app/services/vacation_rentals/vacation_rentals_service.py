from app.models.vacation_rentals.vacation_rentals_model import VacationRentalsModel


class VacationRentalsService:
    def getData(
        self,
        vacation_rental_object: VacationRentalsModel,
    ):
        title = vacation_rental_object.title
        details = vacation_rental_object.vacation_rentals_detail.all()

        data = {
            'title': title,
            'details': details,
        }

        return data