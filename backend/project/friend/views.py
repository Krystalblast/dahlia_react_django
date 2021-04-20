from django.http import Http404
from requests import Response
from rest_framework import status

from .models import Friend
from .serializers import FriendSerializer
# Create your views here.


def get_friend_object(self, pk, format=None):
    try:
        return Friend.objects.get(pk=pk)
    except Friend.DoesNotExist:
        raise Http404


def add_friend(self, request, pk, format=None):
    friend = get_friend_object(pk)
    serializer: FriendSerializer = FriendSerializer(friend, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def remove_friend(self, request, pk, format=None):
    friends = get_friend_object(pk)
    friends.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


def get_friends_list(self, request, pk, format=None):
    # TODO need to add where user=???
    friends = Friend.objects.all()
    serializer = FriendSerializer(friends, many=True)
    return Response(serializer.data)
