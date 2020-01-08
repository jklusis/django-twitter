from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from posts.structures import PostDataStructure
from posts.services.post_service import create, delete, get_feed, get_user_feed, get_post_data_structure
import json

@login_required(login_url='/sign-in')
@require_http_methods(["POST"])
def create_post(request):
    # Because ajax and json is received, we need to decode it
    data = json.loads(request.body)
    post = data.get('post')

    create(request.user.id, post)

    return JsonResponse({
        'success': post
    })

@login_required(login_url='/sign-in')
@require_http_methods(["POST"])
def delete_post(request):
    # Because ajax and json is received, we need to decode it
    data = json.loads(request.body)
    post_id = data.get('post_id')

    delete(request.user.id, post_id)

    return JsonResponse({
        'success': True
    })

@login_required(login_url='/sign-in')
@require_http_methods(["POST"])
def get_feed_posts(request):
    posts = get_feed(request.user.id)

    postData = []
    for post in posts:
        postData.append(get_post_data_structure(post).__dict__) # Convert to dict so it is json seriazable

    return JsonResponse({
        'postData': postData
    })

@login_required(login_url='/sign-in')
@require_http_methods(["POST"])
def get_user_feed_posts(request, user_id):
    posts = get_user_feed(user_id)

    postData = []
    for post in posts:
        postData.append(get_post_data_structure(post).__dict__) # Convert to dict so it is json seriazable

    return JsonResponse({
        'postData': postData
    })