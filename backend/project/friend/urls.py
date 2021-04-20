from django.urls import path
from .views import *

app_name = "friend"

urlpatterns = [
    path('friends/list', get_friends_list, name='friends_list'),
    path('friends/add/<int:userID>', add_friend, name='friend_add'),
    path('friends/remove', remove_friend, name='friend_remove'),
    path('friends/find', get_friend_object, name='friend_find'),
    # path('update_profile/', ProfileUpdateView.as_view(), name='update_profile'),
]
