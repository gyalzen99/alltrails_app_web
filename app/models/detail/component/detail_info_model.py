from django.db import models

class DetailInfoModel(models.Model):
  detail_info_title = models.CharField(max_length=2000)
  detail_info_sentence = models.TextField()

  def __str__(self) -> str:
    return self.detail_info_title