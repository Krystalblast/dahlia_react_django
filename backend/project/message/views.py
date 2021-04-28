from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponse
from django.utils.translation import ugettext_lazy as _
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import GenericAPIView
from django.db.models import Q

from .models import Message
from friend.models import Friend
from restauth.models import *
AuPairUser = get_user_model()
# Create your views here.


class MessagesView(GenericAPIView):

    """
    Send Message to another AuPairUser
    """
    @api_view(('POST',))
    @authentication_classes([TokenAuthentication, ])
    # @permission_classes([IsAuthenticated])
    def send_message(self, user_id, friend_id, message, media, format=None):
        # user = AuPairUser.objects.get(pk=self.user.pk)
        user = AuPairUser.objects.get(pk=user_id)
        friend = AuPairUser.objects.get(pk=friend_id)
        message = Message.objects.create(message_creator=user,
                                         message_receiver=friend,
                                         message_text=message,
                                         message_media=media)
        message.save()
        msg = {"detail": _("Message sent.")}
        return Response(msg, status=status.HTTP_200_OK)

    """
    Get Messages from AuPairUsers' Friend(s)
    """
    @api_view(('GET',))
    @authentication_classes([TokenAuthentication, ])
    # @permission_classes([IsAuthenticated])
    def get_messages(self, user_id, format=None):
        # user = AuPairUser.objects.get(pk=self.user.pk)
        user = AuPairUser.objects.get(pk=user_id)
        all_msg = Message.objects.all()
        friends = Friend.objects.filter(user=user)
        converted = []
        for f in friends:
            converted.append(f.friend)

        combined = []
        for friend in converted:
            messages = all_msg.filter((Q(message_creator=user) & Q(message_receiver=friend)) | (Q(message_creator=friend) & Q(message_receiver=user))).order_by('date_created')
            if messages:
                lst = list(messages.values())
                combined.append(lst)

        return JsonResponse(combined, content_type='application/json', safe=False)

    """
    Remove Message from AuPairUsers' conversation with Friend
    """
    @api_view(('POST',))
    @authentication_classes([TokenAuthentication, ])
    # @permission_classes([IsAuthenticated])
    def remove_message(self, msg_id, format=None):
        message = Message.objects.get(pk=msg_id)
        if message:
            message.delete()
            return Response({"detail": _("Successfully removed message.")}, status=status.HTTP_200_OK)

        return Response({"error": _("Something went wrong.")}, status=status.HTTP_404_NOT_FOUND)

    """
    Delete entire conversation with Friend
    """
    @api_view(('POST',))
    @authentication_classes([TokenAuthentication, ])
    # @permission_classes([IsAuthenticated])
    def remove_messages(self, user_id, friend_id, format=None):
        all_msg = Message.objects.all()
        # user = AuPairUser.objects.get(pk=self.user.pk)
        user = AuPairUser.objects.get(pk=user_id)
        friend = AuPairUser.objects.get(pk=friend_id)
        messages = all_msg.filter((Q(message_creator=user) & Q(message_receiver=friend)) | (Q(message_creator=friend) & Q(message_receiver=user))).order_by('date_created')
        if messages:
            messages.delete()
            return Response({"detail": _("Successfully removed conversation.")}, status=status.HTTP_200_OK)

        return Response({"error": _("Something went wrong.")}, status=status.HTTP_404_NOT_FOUND)
