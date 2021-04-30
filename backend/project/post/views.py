from django.shortcuts import render

from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from .models import Post, Comment, Like
from .serializers import PostSerializer, NewPostSerializer, CommentSerializer, LikeSerializer
# Create your views here.

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(post_creator=self.request.user)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer