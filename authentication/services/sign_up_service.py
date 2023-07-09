from django.contrib.auth.models import User

class SignUpService:
    def register_user(
        self,
        request,
        user,
    ):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        is_form_valid, form_message = self.is_form_valid(
          first_name=first_name,
          last_name=last_name,
          username=username,
          email=email,
          password1=password1,
          password2=password2
        )

        if not is_form_valid:
            return False, form_message

        is_password_match, password_match_message = self.password_match(
            password1=password1,
            password2=password2,
        )

        if not is_password_match:
            return False, password_match_message

        is_user_already_exist, exist_message = self.user_already_exist(
            user=user,
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password1
        )

        if not is_user_already_exist:
            return False, exist_message

        return True, None



    def is_form_valid(
        self,
        first_name,
        last_name,
        username,
        email,
        password1,
        password2
    ):

        if first_name == '' or last_name == '' or username == '' or email == '' or password1 == '' or password2 == '':
            return False, 'Please fill all the field'

        return True, None

    def password_match(
        self,
        password1,
        password2
    ):
        if password1 != password2:
            return False
        return True, 'Password do not match.'

    def user_already_exist(
        self,
        user: User,
        first_name,
        last_name,
        username,
        email,
        password,
    ):
        if user.objects.filter(username=username).exists():
            return False, 'Username already taken.'

        if user.objects.filter(email=email).exists():
            return False,  'Email already exists.'

        new_user = user.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )

        new_user.save()
        return True, None