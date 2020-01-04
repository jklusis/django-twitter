from django.shortcuts import render, redirect
from django.contrib.auth import logout
from app.helpers.request import is_post, is_logged_in
from authentication.structures import SignUpStructure, SignInStructure
from authentication.services import sign_up_service, sign_in_service
from authentication.exceptions import AuthValidationException

def signup(request):
    data = SignUpStructure(request.POST)

    args = {
        'data': data,
        'errors': {},
    }

    if is_post(request):
        try:
            sign_up_service.attempt_sign_up(request, data)
        except AuthValidationException as e:
            args['errors'] = e.errors

            return render(request, 'authentication/signup.html', args)
            
        return redirect('dashboard')

    return render(request, 'authentication/signup.html', args)

def signin(request):
    data = SignInStructure(request.POST)

    args = {
        'data': data,
        'errors': {},
    }

    if is_post(request):
        try:
            sign_in_service.attempt_sign_in(request, data)
        except AuthValidationException as e:
            args['errors'] = e.errors

            return render(request, 'authentication/signin.html', args)

        return redirect('dashboard')

    return render(request, 'authentication/signin.html', args)

def signout(request):
    if not is_post(request) or not is_logged_in(request):
        return redirect('index')

    logout(request)

    return redirect('index')