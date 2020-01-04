from django.shortcuts import render

def index(request):
    if request.user.is_anonymous:
        return render(request, 'index.html')

    return render(request, 'dashboard.html')