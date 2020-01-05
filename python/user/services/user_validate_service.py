from django.contrib.auth.models import User

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

def verify_password(user, password):
    if not user.check_password(password):
        return 'Invalid password'

    return None