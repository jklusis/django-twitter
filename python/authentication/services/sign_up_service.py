from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from authentication.structures import SignUpStructure
from authentication.exceptions import AuthValidationException
from user.services.user_validate_service import *

def attempt_sign_up(request, data: SignUpStructure):
    validate_data(data)

    user = User.objects.create_user(username=data.username, email=data.email, password=data.password, first_name=data.first_name, last_name=data.last_name)
    user.save()

    user = authenticate(request, username=data.username, password=data.password)

    login(request, user)

    return True

def validate_data(data: SignUpStructure):
    errors = {}

    email_error = validate_email(data.email)
    if email_error:
        errors['email'] = email_error

    username_error = validate_username(data.username)
    if username_error:
        errors['username'] = username_error

    first_name_error = validate_first_name(data.first_name)
    if first_name_error:
        errors['first_name'] = first_name_error

    last_name_error = validate_last_name(data.last_name)
    if last_name_error:
        errors['last_name'] = last_name_error

    password_error = validate_password(data.password)
    if password_error:
        errors['password'] = password_error

    password_confirm_error = validate_password_confirm(data.password, data.password_confirm)
    if password_confirm_error:
        errors['password_confirm'] = password_confirm_error

    if errors:
        raise AuthValidationException(errors)

    return True