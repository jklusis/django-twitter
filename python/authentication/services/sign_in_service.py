from django.contrib.auth import authenticate, login
from authentication.structures import SignInStructure
from authentication.exceptions import AuthValidationException

def attempt_sign_in(request, data: SignInStructure):
    user = authenticate(request, username=data.username, password=data.password)

    if not user:
        raise AuthValidationException({'credentials': 'Invalid Username or Password'})

    login(request, user)

    return True