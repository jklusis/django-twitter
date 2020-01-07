from datetime import datetime
from posts.models import Post, PostLike
from posts.structures import PostDataStructure

def create_post():
    pass

def get_feed(user_id: int, offset: int = 0):
    return Post.objects.filter().order_by('-created_at').all()
    
def get_user_feed(user_id: int, offset: int = 0):
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