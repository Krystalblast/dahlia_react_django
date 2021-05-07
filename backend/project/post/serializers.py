from rest_framework import serializers
from .models import Post, Comment, Like


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    post_replies = CommentSerializer(many=True, allow_null=True, read_only=True)
    post_liked = LikeSerializer(many=True, allow_null=True, read_only=True)

    class Meta:
        app_label = 'post'
        model = Post
        fields = '__all__'
        # optional_fields = ('post_media')

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.post_creator = validated_data.get('post_creator', instance.post_creator)
        instance.post_text = validated_data.get('post_text', instance.post_text)
        instance.post_liked = validated_data.get('post_liked', instance.post_liked)
        instance.post_replies = validated_data.get('post_replies', instance.post_replies)
        # instance.post_media = validated_data.get('post_media', instance.post_media)
        instance.save()
        return instance


class NewPostSerializer(serializers.ModelSerializer):
    post_replies = CommentSerializer(many=True, read_only=True)
    post_liked = LikeSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'post_creator', 'post_text', 'post_replies', 'post_liked']
        optional_fields = ('post_media',)
