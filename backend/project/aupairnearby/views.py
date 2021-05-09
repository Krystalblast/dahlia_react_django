from django.utils.translation import ugettext_lazy as _
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework import status

from .models import AuPairNearBy
from .serializers import AuPairNearBySerializer

# set enabled/not_enable

# set latitude/longitude

# get users lats/Longs that are enabled

# Create your views here.


@authentication_classes([TokenAuthentication, ])
@api_view(('GET',))
def get_nearby(request):
    nearby = AuPairNearBy.objects.all()
    data = AuPairNearBySerializer(nearby, many=True).data
    return Response(data, status=status.HTTP_200_OK)


@authentication_classes([TokenAuthentication, ])
@api_view(('POST',))
def create_nearby(request):
    if request.method == 'POST':
        user = request.POST.get("user")
        enabled = request.POST.get("enabled")
        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")
        # nearby_users = request.POST.get("nearby_users")
        data = {'user': user,
                'enabled': enabled,
                'latitude': latitude,
                'longitude': longitude}
        #        'nearby_users': nearby_users}
        serializer = AuPairNearBySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


@api_view(('DELETE',))
@authentication_classes([TokenAuthentication, ])
def remove_nearby(self, nearby_id, format=None):
    nearby = AuPairNearBy.objects.filter(id=nearby_id).delete()
    if nearby:
        return Response({"detail": _("Successfully removed Nearby location.")}, status=status.HTTP_200_OK)

    return Response({"error": _("Error removing Nearby location.")}, status=status.HTTP_400_BAD_REQUEST)
