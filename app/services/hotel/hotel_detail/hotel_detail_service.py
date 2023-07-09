from app.models.hotel.component.hotel_detail_model import HotelDetailModel
from app.models.hotel.component.hotel_service_model import HotelServiceModel
from app.models.hotel.hotel_model import HotelModel


class HotelDetailService:
    def getData(
        self,
        hotel_detail_object: HotelDetailModel,
    ):
        hotel_name = hotel_detail_object.hotel_name
        hotel_image = hotel_detail_object.hotel_image
        hotel_info = hotel_detail_object.hotel_info

        hotel_service: HotelServiceModel = hotel_detail_object.hotel_service_detail
        hotel_location = hotel_service.location

        data = {
            'hotel_name': hotel_name,
            'hotel_image': hotel_image,
            'hotel_info': hotel_info,
            'hotel_location': hotel_location
        }

        return data