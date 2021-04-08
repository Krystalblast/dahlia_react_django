from django.contrib.auth import authenticate
import django.contrib.auth.password_validation as validators
from django.utils.translation import ugettext_lazy as _
from django.core import exceptions

from rest_framework import serializers

from .models import *


class AuthAuPairUserSerializer(serializers.Serializer):
    email = serializers.EmailField(label=_("Email"))
    password = serializers.CharField(label=_("Password"), style={'input_type': 'password'})

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            print('user: {}'.format(user))
            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError(msg)

            else:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg)
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg)

        attrs['user'] = user
        return attrs


class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=120,
        min_length=5)
    email = serializers.EmailField()
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length=255, required=True)
    last_name = serializers.CharField(max_length=255, required=True)
    agency = serializers.CharField(max_length=255, required=True)

    def validated_username(self, username):
        usr = AuPairUser.objects.filter(username=username)
        if usr:
            raise serializers.ValidationError(
                _("A user is already registered with this username."))
        return username

    def validate_email(self, email):
        eml = AuPairUser.objects.filter(email=email)
        if eml:
            raise serializers.ValidationError(
                _("A user is already registered with this e-mail address."))
        return email

    def validate_password1(self, password):
        errors = dict()
        try:
            validators.validate_password(password=password)
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)
        return password

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(_("The two password fields didn't match."))
        return data

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'agency': self.validated_data.get('agency', ''),
        }

    def save(self, request):
        self.cleaned_data = self.get_cleaned_data()
        new_user = AuPairUser(username=self.cleaned_data['username'],
                              email=self.cleaned_data['email'],
                              first_name=self.cleaned_data['first_name'],
                              last_name=self.cleaned_data['last_name'],
                              agency=self.cleaned_data['agency'],
                              )
        new_user.set_password(self.cleaned_data['password1'])
        new_user.save()
        return new_user


class AuPairUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuPairUser
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    user = AuPairUserSerializer(required=True)

    class Meta:
        model = AuPairProfile
        fields = '__all__'

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        username = self.validated_data['user']['username']
        user = AuPairUser.object.get(username=username)
        print(user)
        user_serializer = AuPairUserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.update(user, user_data)
        instance.save()
        return instance
