from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        app_label = 'post'
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        return Post.object.create(**validated_data)

    def update(self, instance, validated_data):
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.post_creator = validated_data.get('post_creator', instance.post_creator)
        instance.post_text = validated_data.get('post_text', instance.post_text)
        instance.post_liked = validated_data.get('post_liked', instance.post_liked)
        instance.post_replies = validated_data.get('post_replies', instance.post_replies)
        instance.post_media = validated_data.get('post_media', instance.post_media)
        instance.save()
        return instance
