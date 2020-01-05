import json
from django.shortcuts import render
from user.services.user_service import get_user_data_structure

def index(request):
    if request.user.is_anonymous:
        return render(request, 'index.html')

    data = get_user_data_structure(request.user)

    return render(request, 'dashboard.html', {
        'user_data': json.dumps(data.__dict__)
    })