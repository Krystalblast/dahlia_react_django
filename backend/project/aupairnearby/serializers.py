from rest_framework import serializers
from .models import AuPairNearBy


class AuPairNearBySerializer(serializers.ModelSerializer):

    class Meta:
        app_label = 'aupairnearby'
        model = AuPairNearBy
        fields = '__all__'

    def create(self, validated_data):
        return AuPairNearBy.object.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.enabled = validated_data.get('enabled', instance.enabled)
        instance.location = validated_data.get('location', instance.location)
        instance.nearby_users = validated_data.get('nearby_users', instance.nearby_users)
        instance.save()
        return instance
