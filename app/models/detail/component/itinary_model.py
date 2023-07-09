from django.db import models

class ItinaryModel(models.Model):
  itinary_info_title = models.CharField(max_length=2000)
  itinary_info = models.TextField()

  def __str__(self) -> str:
    return str(self.id)
