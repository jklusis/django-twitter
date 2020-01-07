from datetime import datetime
from user.models import UserFollow

def get_user_follower_count(user_id):

    return 0

def get_user_followers(user_id):

    return {}

# Returns whether user is following
def toggle_follow(active_user_id, user_id):
    if not get_is_following(active_user_id, user_id):
        user_follow = UserFollow(following_user_id=active_user_id, followed_user_id=user_id, created_at=datetime.now())
        user_follow.save()

        return True

    UserFollow.objects.filter(following_user_id=active_user_id, followed_user_id=user_id).delete()

    return False

def get_is_following(following_user_id, followed_user_id):
    return UserFollow.objects.filter(following_user_id=following_user_id, followed_user_id=followed_user_id).exists()