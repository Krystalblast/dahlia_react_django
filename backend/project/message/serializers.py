from rest_framework import serializers
from .models import Message


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        app_label = 'message'
        model = Message
        fields = ['id',
                  'date_created',
                  'message_creator',
                  'message_receiver',
                  'message_text',
                  'message_media', ]

    def create(self, validated_data):
        return Message.object.create(**validated_data)

    def update(self, instance, validated_data):
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.message_creator = validated_data.get('message_creator', instance.message_creator)
        instance.message_receiver = validated_data.get('message_receiver', instance.message_receiver)
        instance.message_text = validated_data.get('message_text', instance.message_text)
        instance.message_media = validated_data.get('message_media', instance.message_media)
        instance.save()
        return instance
