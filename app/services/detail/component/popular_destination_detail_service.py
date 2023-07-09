from app.models.home.component.popular_destination_model import PopularDestinationModel


class PopularDestinationService:
    def getData(self, popular_destination_object: PopularDestinationModel):
        page_title = popular_destination_object.title
        image_path = '/media/' + str(popular_destination_object.image_path)
        popular_destination_detail = popular_destination_object.popular_destination_detail
        service_info = popular_destination_detail.customer_service.service_info
        detail_info = popular_destination_detail.detail_info
        itinary = popular_destination_detail.itinary


        data = {
            'page_title': page_title,
            'image_path': image_path,
            'details': popular_destination_detail,
            'service_info': service_info,
            'detail_info': detail_info,
            'itinary': itinary,
        }

        return data