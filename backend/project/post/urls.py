from . import views
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *

app_name = "posts"
routers = SimpleRouter()
routers.register("posts", views.PostViewSet, "posts")
routers.register("comments", views.CommentViewSet, "comments")


# urlpatterns = routers.urls
urlpatterns = [
    path('create_post/', views.create_post, name='create_post'),
    path('feed/<int:user_id>', PostsView.get_feed, name='feed'),
    path('remove_post/<int:post_id>', RemovePostView.remove_post, name='remove_post'),
    # path('feed/', PostsView.get_feed, name='feed')
]
