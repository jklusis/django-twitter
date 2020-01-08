import json
from django.shortcuts import render
from user.services.user_service import get_user_data_structure, get_users_by_username

def index(request):
    if request.user.is_anonymous:
        return render(request, 'index.html')

    data = get_user_data_structure(request.user)

    return render(request, 'dashboard.html', {
        'user_data': json.dumps(data.__dict__)
    })

def search(request):
    username = request.GET.get('username', '')

    if username:
        users = get_users_by_username(username)
    else:
        users = []

    return render(request, 'search.html', {
        'username': username,
        'users': users,
    })