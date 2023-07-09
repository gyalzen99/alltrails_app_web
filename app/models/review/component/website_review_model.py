from django.db import models

class WebsiteReviewModel(models.Model):
    user_name = models.CharField(max_length=100, default='Anonymous User')
    webiste_review = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.user_name