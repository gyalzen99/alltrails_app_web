from rest_framework.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from app.models.review.component.website_review_model import WebsiteReviewModel

from app.models.review.review_model import ReviewModel
from app.services.review.review_service import ReviewService

class ReviewView(View):
    def get(self, request):
        review_object = ReviewModel.objects.first()
        review_service = ReviewService()

        data = review_service.getData(
            review_object=review_object,
            user = User
        )

        return render(
            request,
            'review/review.html',
            data,
        )

    def post(self, request):
        comment = request.POST['comment']

        review: ReviewModel = ReviewModel.objects.first()
        review.website_review_detail.create(
            webiste_review = comment,
            user_name = review.user.username,
        )

        return redirect('review')