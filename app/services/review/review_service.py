from app.models.review.review_model import ReviewModel
from django.contrib.auth.models import User, AnonymousUser


class ReviewService:
    def getData(
        self,
        review_object: ReviewModel,
        user: User
    ):
        user = User

        title = review_object.title
        image = review_object.image
        review = review_object.website_review_detail.all()


        data = {
            'title': title,
            'image': image,
            'reviews': review,
            'user': user,
        }

        return data