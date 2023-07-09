from urllib.parse import urlencode

from django.urls import reverse
from utils.constants.image_path import set_image_path
from utils.constants.link import set_redirect_link


class HomeService:
    def getData(
        self,
        home_object,
        kathmandu_tour_object,
        popular_destination_object,
    ):
        image_path = home_object.home_main_image

        hero_image_path = set_image_path(path = image_path)

        data = {
            'hero_image_path': hero_image_path,
            'popular_destination_object': popular_destination_object,
            'kathmandu_tour_object': kathmandu_tour_object,
        }

        return data