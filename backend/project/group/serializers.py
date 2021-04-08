from rest_framework import serializers
from .models import Group


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        app_label = 'group'
        model = Group
        fields = '__all__'

    def create(self, validated_data):
        return Group.object.create(**validated_data)

    def update(self, instance, validated_data):
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.group_creator = validated_data.get('group_creator', instance.group_creator)
        instance.group_name = validated_data.get('group_name', instance.group_name)
        instance.group_users = validated_data.get('group_users', instance.group_users)
        instance.group_chat = validated_data.get('group_chat', instance.group_chat)
        instance.save()
        return instance
