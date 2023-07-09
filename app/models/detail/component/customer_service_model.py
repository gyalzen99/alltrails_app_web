from django.db import models

class CustomerServiceModel(models.Model):
  service_info = models.TextField()

  def __str__(self) -> str:
    return str(self.id)