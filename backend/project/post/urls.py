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
    path('feed/<int:user_id>', PostsView.get_feed, name='feed')
    # path('feed/', PostsView.get_feed, name='feed')
]
