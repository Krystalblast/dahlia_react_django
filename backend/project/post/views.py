from itertools import chain
from operator import attrgetter

from django.utils.translation import ugettext_lazy as _
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .models import Post, Comment, Like, AuPairUser
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
# from friend.views import get_friends
# Create your views here.
from friend.views import FriendsView

from friend.models import Friend


@authentication_classes([TokenAuthentication, ])
@api_view(('POST',))
def create_post(request):
    if request.method == 'POST':
        creator = request.POST.get("post_creator")
        text = request.POST.get("post_text")
        data = {'post_creator': creator,
                'post_text': text}
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @authentication_classes([TokenAuthentication, ])
    def perform_create(self):
        self.serializer_class.save(post_creator=self.request.user)


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
        qry_friends = Friend.objects.all()
        flt_friends = qry_friends.filter(user_id=user_id)
        f_feeds = []
        for friend in flt_friends:
            f_feeds = list(chain(f_feeds,queryset.filter(post_creator_id=friend.friend.pk)))
        result_list = sorted(chain(filtered, f_feeds), key=attrgetter('date_created'), reverse=True)
        data = PostSerializer(result_list, many=True).data
        return Response(data, status=status.HTTP_200_OK)


class RemovePostView(GenericAPIView):
    """
    Remove Post from AuPairUsers Feed
    """

    @api_view(('DELETE',))
    @authentication_classes([TokenAuthentication, ])
    def remove_post(self, post_id, format=None):
        post = Post.objects.filter(id=post_id).delete()
        if post:
            return Response({"detail": _("Successfully removed post.")}, status=status.HTTP_200_OK)

        return Response({"error": _("Error removing post.")}, status=status.HTTP_400_BAD_REQUEST)
