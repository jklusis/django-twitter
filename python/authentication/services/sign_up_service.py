from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from authentication.structures import SignUpStructure
from authentication.exceptions import AuthValidationException

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

def validate_email(email):
    if not email:
        return 'Please enter your email address'

    if User.objects.filter(email=email).exists():
        return 'This email has already been taken'
    
    return None

def validate_username(username):
    if not username:
        return 'Please enter your username'

    if User.objects.filter(username=username).exists():
        return 'This username has already been taken'

    return None

def validate_first_name(name):
    if not name:
        return 'Please enter your first name'

def validate_last_name(name):
    if not name:
        return 'Please enter your last name'

def validate_password(password):
    if len(password) < 7:
        return 'Password must be at least 7 characters long'

    return None

def validate_password_confirm(password, password_confirm):
    if not password == password_confirm:
        return 'Password and password confirm does not match'

    return None
    