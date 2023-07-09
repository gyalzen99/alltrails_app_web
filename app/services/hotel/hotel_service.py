from app.models.hotel.component.hotel_detail_model import HotelDetailModel
from app.models.hotel.hotel_model import HotelModel


class HotelService:
    def getData(self, hotel_object: HotelModel):
        title = hotel_object.title
        hotel_details = hotel_object.hotel_detail.all()

        data = {
            'title': title,
            'hotel_details': hotel_details,
        }

        return data