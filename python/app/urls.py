"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app import views as base_views
from authentication import views as authentication_views
from user import views as user_views
from posts import views as post_views

urlpatterns = [
    path('', base_views.index, name='index'),
    path('', base_views.index, name='dashboard'),

    path('search', base_views.search, name='search'),

    path('sign-in', authentication_views.signin, name='signin'),
    path('sign-up', authentication_views.signup, name='signup'),
    path('sign-out', authentication_views.signout, name='signout'),

    path('user/<slug:username>', user_views.profile, name='profile'),

    path('user-rpc/toggle-follow', user_views.toggle_follow_user, name='rpc-toggle-follow-user'),

    path('settings', user_views.settings, name='settings'),
    path('settings/update-settings', user_views.update_settings, name='update-settings'),
    path('settings/update-password', user_views.update_password, name='update-password'),
    path('settings/delete-account', user_views.delete_account, name='delete-account'),

    path('post-rpc/create', post_views.create_post, name='rpc-create-post'),
    path('post-rpc/delete', post_views.delete_post, name='rpc-delete-post'),
    path('post-rpc/get', post_views.get_feed_posts, name='rpc-get-feed-posts'),
    path('post-rpc/user-feed/<int:user_id>', post_views.get_user_feed_posts, name='rpc-get-user-feed-posts'),

    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
