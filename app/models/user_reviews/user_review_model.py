from django.db import models
from django.contrib.auth.models import User, AnonymousUser

class UserReviewModel(models.Model):
    user = models.ForeignKey(User, default=AnonymousUser, on_delete=models.CASCADE)
    user_review = models.TextField()
    review_date = models.DateField(auto_now_add=True)
    review_time = models.TimeField(auto_now_add=True)
    review_update_date = models.DateField(auto_now=True)
    review_update_time = models.TimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.username + ' Review'