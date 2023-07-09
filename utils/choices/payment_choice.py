from django.db import models
from django.utils.translation import gettext_lazy as _


class PaymentChoices(models.TextChoices):
    CASH_IN_FRONT = "CashInFront", _("Cash In Front")
    KHALTI = "Khalti", _("Khalti"),