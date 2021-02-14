from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class AuPairUserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, agency, password=None):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email = self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            agency=agency,

        )
'''
    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save()
        return user
'''
class AuPairUser(AbstractBaseUser):
    username = models.CharField(max_length=50,default='',editable=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    agency = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    created_dt = models.DateTimeField(_('create_dt'), auto_now_add=True)
    modified_dt = models.DateTimeField(_('modified_dt'), auto_now=True)

    objects = AuPairUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = []

    def __str__(self):
        return self.email

    def get_full_name(self):
        #The use is identified by their email address
        return self.email

    def get_short_name(self):
         #The use is identified by their email address
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
         # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_active(self):
        "Is the user active?"
        return self.active

    @property
    def is_admin(self):
        "Is the user an admin"
        return self.admin

class AuPairInfo(models.Model):
    user = models.OneToOneField(AuPairUser, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    town = models.CharField(max_length=100)
    state = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=5)
