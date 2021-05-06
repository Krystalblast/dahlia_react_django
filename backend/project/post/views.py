from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

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


class PostsView(GenericAPIView):

    """
    Get Posts from AuPairUser
    """
    @api_view(('GET',))
    @authentication_classes([TokenAuthentication, ])
    def get_feed(self, user_id, format=None):
        queryset = Post.objects.all()
        filtered = queryset.filter(post_creator_id=user_id)
        converted = []
        for post in filtered:
            converted.append(post)
        data = PostSerializer(converted, many=True).data
        return Response(data, status=status.HTTP_200_OK)
