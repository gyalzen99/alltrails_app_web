from app.models.home.component.kathmandu_tour_model import KathmanduTourModel


class KathmanduTourService:
    def getData(self, kathmandu_tour_object: KathmanduTourModel):
        page_title = kathmandu_tour_object.title
        image_path = '/media/' + str(kathmandu_tour_object.image_path)
        kathmandu_tour_detail = kathmandu_tour_object.kathmandu_tour_detail
        service_info = kathmandu_tour_detail.customer_service.service_info
        detail_info = kathmandu_tour_detail.detail_info
        itinary = kathmandu_tour_detail.itinary

        data = {
            'page_title': page_title,
            'image_path': image_path,
            'details': kathmandu_tour_detail,
            'service_info': service_info,
            'detail_info': detail_info,
            'itinary': itinary,
        }

        return data