from django.contrib.auth.models import User
from user.exceptions import UserValidationException
from user.structures import UserSettingStructure, UserPasswordStructure
from user.services.user_validate_service import *

def update_settings(user: User, data: UserSettingStructure):
    validate_user_settings(data)
    
    return True

def validate_user_settings(data: UserSettingStructure):
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

    if errors:
        raise UserValidationException(errors)

    return True

def update_password(user, data: UserPasswordStructure):
    validate_user_password(data)

    return True

def validate_user_password(data: UserPasswordStructure):
    errors = {}

    password_error = validate_password(data.password)
    if password_error:
        errors['password'] = password_error

    password_confirm_error = validate_password_confirm(data.password, data.password_confirm)
    if password_confirm_error:
        errors['password_confirm'] = password_confirm_error

    if errors:
        raise UserValidationException(errors)

    return True

    