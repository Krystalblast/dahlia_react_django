from rest_framework import serializers
from .models import Group

from restauth.serializers import AuPairUserSerializer
from message.serializers import MessageSerializer


class GroupSerializer(serializers.ModelSerializer):
    group_creator = AuPairUserSerializer()
    group_name = serializers.CharField(max_length=255)
    group_users = AuPairUserSerializer()
    group_chat = MessageSerializer()

    class Meta:
        app_label = 'group'
        model = Group
        fields = '__all__'

    def create(self, validated_data):
        return Group.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.group_creator = validated_data.get('group_creator', instance.group_creator)
        instance.group_name = validated_data.get('group_name', instance.group_name)
        instance.group_users = validated_data.get('group_users', instance.group_users)
        instance.group_chat = validated_data.get('group_chat', instance.group_chat)
        instance.save()
        return instance
