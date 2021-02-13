from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from .serializers import *
from .models import *
# Create your views here.

class SignUpView(GenericAPIView):
    serializer_class = SignUpSerializer

    def post(self, request, *args, **kwargs):
        post_data = request.POST.copy()
        serializer = self.serializer_class(data=post_data)

        if serializer.is_valid(raise_exception=ValueError):
            serializer.save(request)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
