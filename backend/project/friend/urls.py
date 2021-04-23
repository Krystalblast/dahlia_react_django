from django.urls import path
from .views import *

app_name = "friend"

urlpatterns = [
    path('add_friend/<int:friend_id>', FriendsView.add_friend, name='add_friend'),
    path('list/', get_friends_list, name='friends_list'),
    path('remove/', remove_friend, name='friend_remove'),
    path('find/', get_friend_object, name='friend_find'),
    # path('update_profile/', ProfileUpdateView.as_view(), name='update_profile'),
]
