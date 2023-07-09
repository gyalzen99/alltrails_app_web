from django.db import models

class HotelServiceModel(models.Model):
    hotel_name = models.CharField(max_length=400)
    location = models.CharField(max_length=1000)
    hotel_image = models.ImageField(upload_to='images/hotels/hotel_detail')
    total_room = models.IntegerField(default=100)
    vip_room = models.IntegerField(default=50)
    normal_room = models.IntegerField(default=50)
    is_bar_exist = models.BooleanField(default=True)
    is_swimming_pool_exist = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.hotel_name