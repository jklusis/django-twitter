from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from posts.structures import PostDataStructure
from posts.services.post_service import get_post_data_structure, get_feed, get_user_feed

@login_required(login_url='/sign-in')
def create_post(request):

    return

@login_required(login_url='/sign-in')
def delete_post(request):

    return

@login_required(login_url='/sign-in')
def get_feed_posts(request):
    posts = get_feed(request.user.id)

    postData = []
    for post in posts:
        postData.append(get_post_data_structure(post).__dict__) # Convert to dict so it is json seriazable

    return JsonResponse({
        'postData': postData
    })

@login_required(login_url='/sign-in')
def get_user_feed_posts(request, user_id):
    posts = get_user_feed(user_id)

    postData = []
    for post in posts:
        postData.append(get_post_data_structure(post).__dict__) # Convert to dict so it is json seriazable

    return JsonResponse({
        'postData': postData
    })