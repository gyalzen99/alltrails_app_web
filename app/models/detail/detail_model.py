from django.db import models

from app.models.detail.component.customer_service_model import CustomerServiceModel
from app.models.detail.component.detail_info_model import DetailInfoModel
from app.models.detail.component.itinary_model import ItinaryModel

class DetailModel(models.Model):
    detail_title = models.CharField(max_length=100)
    detail_image = models.ImageField(upload_to='images/detail')
    price_title = models.CharField(max_length=1000)
    price = models.CharField(max_length=1000)
    actual_price = models.CharField(max_length=1000, blank=True, null=True)
    customer_service = models.ForeignKey(CustomerServiceModel, on_delete=models.DO_NOTHING, related_name='customer_service_data')
    detail_info = models.ForeignKey(DetailInfoModel, on_delete=models.DO_NOTHING, related_name='detail_info_data')
    itinary = models.ForeignKey(ItinaryModel, on_delete=models.DO_NOTHING, related_name='itinary_data')

    def __str__(self) -> str:
        return self.detail_title