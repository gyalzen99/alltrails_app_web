from django.db import models
from django.utils.translation import gettext_lazy as _


class RoomChoices(models.TextChoices):
    PrivateRoom = "PrivateRoom", _("PrivateRoom")
    Apartment = "Apartment", _("Apartment")
    CityInn = "CityInn", _("CityInn")
