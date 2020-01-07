from datetime import datetime
from django.contrib.auth import logout
from django.contrib.auth.models import User
from user.models import UserFollow
from user.exceptions import UserValidationException
from user.structures import UserSettingStructure, UserDataStructure
from user.services.user_validate_service import *
from posts.services.post_service import get_user_post_count

def update_user_settings(user: User, data: UserSettingStructure):
    validate_user_settings(user, data)

    user.email = data.email
    user.username = data.username
    user.first_name = data.first_name
    user.last_name = data.last_name

    user.save()
    
    return True

def validate_user_settings(user: User, data: UserSettingStructure):
    errors = {}

    # Only check if email has changed
    if not user.email == data.email:
        email_error = validate_email(data.email)
        if email_error:
            errors['email'] = email_error

    # Only check if username has changed
    if not user.username == data.username:
        username_error = validate_username(data.username)
        if username_error:
            errors['username'] = username_error

    first_name_error = validate_first_name(data.first_name)
    if first_name_error:
        errors['first_name'] = first_name_error

    last_name_error = validate_last_name(data.last_name)
    if last_name_error:
        errors['last_name'] = last_name_error

    if errors:
        raise UserValidationException(errors)

    return True

def update_user_password(user, data: UserSettingStructure):
    validate_user_password(user, data)

    user.set_password(data.password_new)

    return True

def validate_user_password(user: User, data: UserSettingStructure):
    errors = {}

    password_verify_error = verify_password(user, data.password_current)
    if password_verify_error:
        errors['password_current'] = password_verify_error

    password_new_error = validate_password(data.password_new)
    if password_new_error:
        errors['password_new'] = password_new_error

    password_new_confirm_error = validate_password_confirm(data.password_new, data.password_new_confirm)
    if password_new_confirm_error:
        errors['password_new_confirm'] = password_new_confirm_error

    if errors:
        raise UserValidationException(errors)

    return True

def delete_user_account(request):
    user = request.user
    
    user.first_name = 'Former user'
    user.last_name = ''
    user.is_active = False
    user.save()

    logout(request)

    return True

def get_user_by_username(username):
    return User.objects.get(username=username)
    
def get_user_data_structure(user):
    data = UserDataStructure()

    data.id = user.id
    data.email = user.email
    data.username = user.username
    data.first_name = user.first_name
    data.last_name = user.last_name
    data.date_joined = int(datetime.timestamp(user.date_joined))
    data.following_count = UserFollow.objects.filter(following_user_id=user.id).count()
    data.follower_count = UserFollow.objects.filter(followed_user_id=user.id).count()
    data.post_count = get_user_post_count(user.id)

    return data

