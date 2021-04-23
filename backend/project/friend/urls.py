from django.urls import path
from .views import *
from . import views

app_name = "friend"

urlpatterns = [
    path('list/', get_friends_list, name='friends_list'),
    path('add/<int:userID>/', add_friend, name='friend_add'),
    path('remove/', remove_friend, name='friend_remove'),
    path('find/', get_friend_object, name='friend_find'),
    path('add_friend/<int:user_pk>/<int:friend_pk>', FriendsView.add_friend, name='add_friend'),
    path('add4/<int:user_pk>/<int:friend_pk>', views.add_friend_here, name='add4'),
    # path('update_profile/', ProfileUpdateView.as_view(), name='update_profile'),
]
