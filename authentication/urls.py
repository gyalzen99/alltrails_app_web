from django.urls import path

from .views.sign_in_view import SignInView
from .views.sign_up_view import SignUpView


urlpatterns = [
    path('sign_in', SignInView.as_view(), name='sign_in'),
    path('sign_up', SignUpView.as_view(), name='sign_up'),
]