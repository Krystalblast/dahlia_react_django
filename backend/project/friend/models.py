from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
AuPairUser = get_user_model()


class Friend(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    friend = models.ForeignKey(AuPairUser, on_delete=models.CASCADE, related_name='friend')

    def __str__(self):
        return '%s: %s' % (str(self.friend), str(self.date_created))
