from django.urls import path
from .views import *

app_name = "friend"

urlpatterns = [
    path('add_friend/<int:friend_id>', FriendsView.add_friend, name='add_friend'),
    path('friends_list/<int:user_id>', FriendsView.get_friends, name='friends_list'),
    path('remove_friend/<int:friend_id>', FriendsView.remove_friend, name='remove_friend'),
    # path('update_profile/', ProfileUpdateView.as_view(), name='update_profile'),
]
