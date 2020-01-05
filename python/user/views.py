from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from app.helpers.request import is_post
from user.services.user_service import update_settings, update_password
from user.structures import UserSettingStructure

@login_required(login_url='/sign-in')
@require_http_methods(["GET"])
def profile(request, username):

    return render(request, 'user/profile.html', {'username': username})

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
@require_http_methods(["POST"])
def update_settings(request):
    args = {
        'data': UserSettingStructure(request.POST),
        'errors': {},
    }

    return render(request, 'user/settings.html', args)

@login_required(login_url='/sign-in')
@require_http_methods(["POST"])
def update_password(request):
    args = {
        'data': UserSettingStructure(request.POST),
        'errors': {},
    }

    return render(request, 'user/settings.html', args)

@login_required(login_url='/sign-in')
@require_http_methods(["POST"])
def delete_account(request):

    return redirect('index')