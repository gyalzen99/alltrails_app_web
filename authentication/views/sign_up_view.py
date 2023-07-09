from rest_framework.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

from authentication.services.sign_up_service import SignUpService

class SignUpView(View):
    def get(self, request):
        return render(
            request,
            'sign_up/sign_up.html',
        )

    def post(self, request):
        sign_up_service = SignUpService()
        is_signup_valid, message = sign_up_service.register_user(
            request=request,
            user = User
        )

        if not is_signup_valid:
            messages.info(request, message)
            return redirect('sign_up')

        else:
            return redirect('sign_in')
