from typing import Dict, Any

from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.utils.translation import ugettext_lazy as _
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import GenericAPIView
from django.db.models import Q

from .models import Group
from restauth.models import *
from .serializers import GroupSerializer

AuPairUser = get_user_model()
# Create your views here.


@authentication_classes([TokenAuthentication, ])
@api_view(('POST',))
def create_group(request):
    if request.method == 'POST':
        creator = request.POST.get("group_creator")
        name = request.POST.get("group_name")
        users = request.POST.get("group_users")
        # chat = request.POST.get("group_chat")
        data: dict[str, Any] = {'group_creator': creator,
                                'group_name': name,
                                'group_users': users}
        # 'group_chat': chat}
        serializer = GroupSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


@api_view(('POST',))
@authentication_classes([TokenAuthentication, ])
# @permission_classes([IsAuthenticated])
def remove_group(self, group_id, format=None):
    group = Group.objects.get(pk=group_id)
    if group:
        group.delete()
        return Response({"detail": _("Successfully removed group.")}, status=status.HTTP_200_OK)

    return Response({"error": _("Something went wrong.")}, status=status.HTTP_404_NOT_FOUND)


@api_view(('POST',))
@authentication_classes([TokenAuthentication, ])
# @permission_classes([IsAuthenticated])
def remove_group_msg(self, user_id, friend_id, format=None):
    all_msg = Group.objects.all()
    # user = AuPairUser.objects.get(pk=self.user.pk)
    user = AuPairUser.objects.get(pk=user_id)
    friend = AuPairUser.objects.get(pk=friend_id)
    messages = all_msg.filter((Q(message_creator=user) & Q(message_receiver=friend)) | (Q(message_creator=friend) & Q(message_receiver=user))).order_by('date_created')
    if messages:
        messages.delete()
        return Response({"detail": _("Successfully removed conversation.")}, status=status.HTTP_200_OK)

    return Response({"error": _("Something went wrong.")}, status=status.HTTP_404_NOT_FOUND)


class GroupsView(GenericAPIView):
    @api_view(('GET',))
    @authentication_classes([TokenAuthentication, ])
    # @permission_classes([IsAuthenticated])
    def get_groups(self, user_id, format=None):
        queryset = Group.objects.all()
        filtered = queryset.filter(group_creator_id=user_id)
        converted = []
        for groups in filtered:
            converted.append(groups)
        data = GroupSerializer(converted, many=True).data
        return Response(data, status=status.HTTP_200_OK)
