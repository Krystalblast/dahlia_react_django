from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import GenericAPIView

from .models import Friend
from .serializers import FriendSerializer
from restauth.serializers import AuPairUserSerializer
AuPairUser = get_user_model()
# Create your views here.


class FriendsView(GenericAPIView):

    """
    Add Friend to AuPairUsers friends_list
    """
    @api_view(('POST',))
    @authentication_classes([TokenAuthentication, ])
    # @permission_classes([IsAuthenticated])
    def add_friend(self, friend_id, format=None):
        data = {'user': self.user.pk, 'friend': friend_id}
        serializer = FriendSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

    """
    Get FriendsList of AuPairUser
    """
    @api_view(('GET',))
    @authentication_classes([TokenAuthentication, ])
    # @permission_classes([IsAuthenticated])
    def get_friends(self, user_id, format=None):
        queryset = Friend.objects.all()
        filtered = queryset.filter(user=user_id)
        converted = []
        for friends in filtered:
            converted.append(friends.friend)
        data = AuPairUserSerializer(converted, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    """
    Remove Friend from AuPairUsers friends_list
    """
    @api_view(('POST',))
    @authentication_classes([TokenAuthentication, ])
    # @permission_classes([IsAuthenticated])
    def remove_friend(self, friend_id, format=None):
        friends = Friend.objects.get(user=self.user.pk, friend=friend_id)
        friends.delete()
        msg = {"detail": _("Successfully removed friend.")}
        return Response(msg, status=status.HTTP_200_OK)

    """
    For Testing
    """
    @api_view(('POST',))
    @authentication_classes([TokenAuthentication, ])
    # @permission_classes([IsAuthenticated])
    def remove_friend2(self, friend_id, user_id, format=None):
        friends = Friend.objects.get(user=user_id, friend=friend_id)
        friends.delete()
        msg = {"detail": _("Successfully removed friend.")}
        return Response(msg, status=status.HTTP_200_OK)
