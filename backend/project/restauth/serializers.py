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

    class Meta:
        model = AuPairUser
        fields = ('user','agency','town','state','zipcode')

    def create(self, validated_data):
        user_data = {'username': validated_data['user.username'],
                     'email' : validated_data['user.email'],
                     'password' : validated_data['user.password']
                     }
        print(user_data)
        user = User.objects.create(**user_data)
        aupair_user = AuPairUser.objects.create(user=user,
                                                 agency=validated_data['agency'],
                                                 town=validated_data['town'],
                                                 state=validated_data['state'],
                                                 zipcode=validated_data['zipcode'])
        return aupair_user

