from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import Post
from .serializers import PostSerializer
# Create your views here.

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer