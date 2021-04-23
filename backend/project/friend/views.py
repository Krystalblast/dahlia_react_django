from django.http import Http404
from django.views.decorators.csrf import csrf_protect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import GenericAPIView

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


# duplicate: wip TODO:RMV
@api_view(('POST',))
@csrf_protect
def add_friend_here(self, user_pk, friend_pk, format=None):
    data = {'user': user_pk, 'friend': friend_pk }
    serializer = FriendSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class FriendsView(GenericAPIView):
    authentication_classes = TokenAuthentication,
    # permission_classes = [AllowAny]

    @api_view(('POST',))
    @csrf_protect
    def add_friend(self, user_pk, friend_pk, format=None):
        # TODO: Currently Hackish... Should use request.data, works tho
        data = {'user': user_pk, 'friend': friend_pk }
        serializer = FriendSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
