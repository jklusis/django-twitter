from datetime import datetime
from user.models import UserFollow
from posts.models import Post, PostLike
from posts.structures import PostDataStructure

def create(user_id:int, post):
    newPost = Post(user_id=user_id, post=post, created_at=datetime.now(), updated_at=datetime.now())

    newPost.save()

    return True

def delete(user_id:int, post_id:int):
    Post.objects.filter(user_id=user_id, id=post_id).delete()

    return True

def get_feed(user_id: int):
    followed_user_ids = UserFollow.objects.filter(following_user_id=user_id).values('followed_user_id')

    combined_queryset = Post.objects.filter(user_id__in=followed_user_ids) | Post.objects.filter(user_id=user_id) # Include also user

    return combined_queryset.order_by('-created_at').all()
    
def get_user_feed(user_id: int):
    return Post.objects.filter(user_id=user_id).order_by('-created_at').all()

def get_user_post_count(user_id: int):
    return Post.objects.filter(user_id=user_id).count()

def get_post_like_count(post_id: int):
    return Post.objects.filter(post_id=post_id).count()

def get_post_data_structure(post):
    data = PostDataStructure()

    data.id = post.id
    data.user_id = post.user.id
    data.username = post.user.username
    data.post = post.post
    data.like_count = 0
    data.created_at = int(datetime.timestamp(post.created_at))
    data.updated_at = int(datetime.timestamp(post.updated_at))

    return data