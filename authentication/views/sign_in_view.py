from rest_framework.views import View
from django.shortcuts import render, redirect
from django.contrib import auth, messages

class SignInView(View):
    def get(self, request):
        return render(
            request,
            'sign_in/sign_in.html',
        )

    def post(self, request):
        username = request.POST['signInUsername']
        password = request.POST['signInPassword']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')

        else:
            messages.info(request, 'Please enter correct credential ')
            return redirect('sign_in')

def logout(request):
    auth.logout(request)
    return redirect(
        '/'
    )
