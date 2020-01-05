import json
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from app.helpers.request import is_post
from user.services.user_service import update_user_settings, update_user_password, delete_user_account, get_user_by_username, get_user_data_structure
from user.exceptions import UserValidationException
from user.structures import UserSettingStructure, UserDataStructure

@login_required(login_url='/sign-in')
@require_http_methods(["GET"])
def profile(request, username):
    user = get_user_by_username(username)

    if not user:
        return 'rip'

    data = get_user_data_structure(user)

    return render(request, 'user/profile.html', {
        'username': username,
        'user_data': json.dumps(data.__dict__)
    })

@login_required(login_url='/sign-in')
@require_http_methods(["GET"])
def settings(request):
    user_data = {
        'email': request.user.email,
        'username': request.user.username,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
    }

    args = {
        'data': UserSettingStructure(user_data),
        'errors': {},
    }

    return render(request, 'user/settings.html', args)

@login_required(login_url='/sign-in')
def update_settings(request):
    if not is_post(request):
        return redirect('settings')

    args = {
        'data': UserSettingStructure(request.POST),
        'errors': {},
    }

    try:
        update_user_settings(request.user, args['data'])
        args['success_message'] = 'Settings successfully updated'
    except UserValidationException as e:
        args['errors'] = e.errors

    return render(request, 'user/settings.html', args)

@login_required(login_url='/sign-in')
def update_password(request):
    if not is_post(request):
        return redirect('settings')

    args = {
        'data': UserSettingStructure(request.POST),
        'errors': {},
    }

    try:
        update_user_password(request.user, args['data'])
        args['success_message'] = 'Password successfully changed'
    except UserValidationException as e:
        args['errors'] = e.errors

    return render(request, 'user/settings.html', args)

@login_required(login_url='/sign-in')
@require_http_methods(["POST"])
def delete_account(request):
    delete_user_account(request)

    return redirect('index')