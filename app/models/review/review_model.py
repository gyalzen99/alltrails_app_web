from django.db import models
from django.contrib.auth.models import User, AnonymousUser

from app.models.review.component.website_review_model import WebsiteReviewModel

class ReviewModel(models.Model):
    user = models.ForeignKey(User, default=AnonymousUser, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200, default='About Us')
    image = models.ImageField(upload_to='image/about_us')
    website_review_detail = models.ManyToManyField(WebsiteReviewModel, blank=True, related_name='website_review_detail')

    def __str__(self) -> str:
        return self.title