from django.db import models

class TreakModel(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    info = models.TextField()
    image = models.ImageField(upload_to='images/things_to_do/treak')

    def __str__(self) -> str:
        return self.title