from django.contrib.auth import login
from django.utils.translation import ugettext_lazy as _

from rest_framework import status, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, UpdateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import JsonResponse, Http404
from django.middleware.csrf import get_token

from .serializers import *
from .models import *
# Create your views here.


@api_view(('GET',))
def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})


class SignUpView(GenericAPIView):
    authentication_classes = TokenAuthentication,
    permission_classes = [AllowAny]
    serializer_class = SignUpSerializer

    def post(self, request, *args, **kwargs):
        post_data = request.POST.copy()
        serializer = self.serializer_class(data=post_data)

        if serializer.is_valid(raise_exception=ValueError):
            new_user = serializer.save(request)
            if new_user:
                token = Token.objects.create(user=new_user)
                json = serializer.data
                json['token'] = token.key
            return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class SignInView(GenericAPIView):
    # permission_classes = [AllowAny]
    serializer_class = AuthAuPairUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        login(request, user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        }, status=status.HTTP_200_OK)


class SignOutView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kargs):
        request.user.auth_token.delete()
        msg = {"detail": _("Successfully logged out.")}

        return Response(msg, status=status.HTTP_204_NO_CONTENT)


class ProfileUpdateView(UpdateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProfileSerializer

    def get_object(self):
        return AuPairProfile.objects.get(user=self.request.user)


class UserGeneralView(APIView):

    """
    Retrieve AuPairUser by user_id
    """
    @api_view(('GET',))
    @authentication_classes([TokenAuthentication, ])
    # @permission_classes([IsAuthenticated])
    def get_user(self, user_id, **kwargs):
        user = AuPairUser.objects.get(pk=user_id)
        data = AuPairUserSerializer(user).data
        return Response(data, status=status.HTTP_200_OK)

    """
    Retrieve all AuPairUsers
    """
    @api_view(('GET',))
    @authentication_classes([TokenAuthentication, ])
    @permission_classes([IsAuthenticated])
    def get_users(self):
        queryset = AuPairUser.objects.all()
        serializer = AuPairUserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    """
    Retrieve AuPairUsers profile
    """
    def get_profile(self, user):
        # TODO: not correct
        try:
            return AuPairProfile.objects.get(user=user)
        except AuPairProfile.DoesNotExist:
            raise Http404

class AuPairUserListView(ListAPIView):
    queryset = AuPairUser.objects.all()
    serializer_class = AuPairUserSerializer
