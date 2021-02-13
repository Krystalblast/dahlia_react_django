import django.contrib.auth.password_validation as validators
from django.utils.translation import ugettext_lazy as _
from django.core import exceptions

from rest_framework import serializers

from .models import *

class AuPairUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuPairUser
        fields = ('username',
                    'email',
                    'password',
                    'first_name',
                    'last_name',
                    'agency',
                    'created_dt',
                    'modified_dt',
                    'last_login')
        read_only_fields = ('email', )

class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=120,
        min_length=5)
    email = serializers.EmailField()
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    agency = serializers.CharField(max_length=255)

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
            'username': self.validated_data.get('username',''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name',''),
            'last_name': self.validated_data.get('last_name',''),
            'agency': self.validated_data.get('agency',''),
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
