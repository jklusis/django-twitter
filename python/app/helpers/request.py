def is_logged_in(request):
    return not request.user.is_anonymous

def is_post(request):
    return request.method == 'POST'