from rest_framework import serializers
from django.contrib.auth.models import User
from .models import AuPairUser

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username','email','password')

class AuPairUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
   # agency = serializers.CharField(max_length=100)
   # town = serializers.CharField(max_length=100)
  #  state = serializers.CharField(max_length=30)
  #  zipcode = serializers.CharField(max_length=5)

    class Meta:
        model = AuPairUser
        fields = ('user','agency','town','state','zipcode')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        aupair_user, create = AuPairUser.objects.update_or_create(user=user,
                                        agency=validated_data.pop('agency'),
                                        town=validated_data.pop('town'),
                                        state=validated_data.pop('state'),
                                        zipcode=validated_data('zipcode'))
        return aupair_user