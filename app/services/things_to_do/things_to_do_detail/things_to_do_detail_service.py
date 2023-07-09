from app.models.things_to_do.component.culture_tour_model import CultureTourModel
from app.models.things_to_do.component.food_tour_model import FoodTourModel
from app.models.things_to_do.component.treak_model import TreakModel


class ThingsToDoDetailService:
    def getData(
        self,
        things_to_do_detail_object: CultureTourModel | FoodTourModel | TreakModel,
    ):
        title = things_to_do_detail_object.title
        info = things_to_do_detail_object.info
        location = things_to_do_detail_object.location
        image = things_to_do_detail_object.image

        data = {
            'title': title,
            'info': info,
            'location': location,
            'image': image,
        }

        return data