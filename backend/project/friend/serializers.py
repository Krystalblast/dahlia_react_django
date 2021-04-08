from rest_framework import serializers
# from backend.project.restauth.serializers import AuPairUserSerializer
from .models import Friend


class FriendSerializer(serializers.ModelSerializer):

    class Meta:
        app_label = 'friend'
        model = Friend
        fields = '__all__'

    def create(self, validated_data):
        return Friend.object.create(**validated_data)

    def update(self, instance, validated_data):
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.friend = validated_data.get('friend', instance.friend)
        instance.save()
        return instance
