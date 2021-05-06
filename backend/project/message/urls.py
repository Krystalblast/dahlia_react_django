from django.urls import path
from .views import *

app_name = "message"

urlpatterns = [
    # path('send_message/<int:user_id>/<int:friend_id>', MessagesView.send_message, name='send_message'),
    # path('send_message/<int:friend_id>', MessagesView.send_message, name='send_message'),
    path('send_message/', SendMessageView.as_view(), name='send_message'),
    # path('send_message/', MessagesView.send_message, name='send_message'),
    path('get_messages/<int:user_id>', MessagesView.get_messages, name='get_messages'),
    path('remove_message/', MessagesView.remove_message, name='remove_message'),
    path('remove_message/<int:msg_id>', MessagesView.remove_message, name='remove_message'),
    path('remove_messages/', MessagesView.remove_messages, name='remove_messages'),
    path('remove_messages/<int:user_id>/<int:friend_id>', MessagesView.remove_messages, name='remove_messages'),
    # path('remove_messages/<int:friend_id>', MessagesView.remove_messages, name='remove_messages'),
]
