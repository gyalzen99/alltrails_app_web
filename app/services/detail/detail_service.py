from app.services.detail.component.kathmandu_tour_destination_service import KathmanduTourService
from app.services.detail.component.popular_destination_detail_service import PopularDestinationService


class DetailService:
    def get_data(
        self,
        popular_destination_object = None,
        kathmandu_tour_object = None,
    ):
        if popular_destination_object != None:
            popular_destination_service = PopularDestinationService()
            return popular_destination_service.getData(
                popular_destination_object = popular_destination_object,
            )

        else:
            kathmandu_tour_service = KathmanduTourService()
            return kathmandu_tour_service.getData(
                kathmandu_tour_object = kathmandu_tour_object,
            )
