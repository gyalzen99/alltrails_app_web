from django.contrib import admin
from app.models.booking.booking_model import BookingModel
from app.models.booking.component.booking_conformation_model import BookingConformationModel

from app.models.hotel.component.hotel_detail_model import HotelDetailModel
from app.models.review.component.website_review_model import WebsiteReviewModel
from app.models.review.review_model import ReviewModel
from app.models.things_to_do.component.culture_tour_model import CultureTourModel
from app.models.things_to_do.component.food_tour_model import FoodTourModel
from app.models.things_to_do.component.treak_model import TreakModel
from app.models.things_to_do.things_to_do_model import ThingsToDoModel
from app.models.vacation_rentals.component.vacation_rentals_detail_model import VacationRentalsDetailModel
from app.models.vacation_rentals.vacation_rentals_model import VacationRentalsModel
from app.services.things_to_do.things_to_do_detail.things_to_do_detail_service import ThingsToDoDetailService
from app.views.things_to_do_detail_view import ThingsToDoDetailView
from .models.home.home_model import HomeModel
from .models.home.component.kathmandu_tour_model import KathmanduTourModel
from .models.home.component.popular_destination_model import PopularDestinationModel
from .models.detail.detail_model import DetailModel
from .models.detail.component.customer_service_model import CustomerServiceModel
from .models.detail.component.detail_info_model import DetailInfoModel
from .models.detail.component.itinary_model import ItinaryModel
from .models.hotel.hotel_model import HotelModel
from .models.hotel.component.hotel_service_model import HotelServiceModel
from .models.user_reviews.user_review_model import UserReviewModel

admin.site.register([
    HomeModel,
    PopularDestinationModel,
    KathmanduTourModel,
    DetailModel,
    CustomerServiceModel,
    DetailInfoModel,
    ItinaryModel,
    HotelModel,
    HotelServiceModel,
    UserReviewModel,
    HotelDetailModel,
    ThingsToDoModel,
    CultureTourModel,
    FoodTourModel,
    TreakModel,
    VacationRentalsModel,
    VacationRentalsDetailModel,
    ReviewModel,
    WebsiteReviewModel,
    BookingModel,
])