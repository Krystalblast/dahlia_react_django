from django.db import models
from django.contrib.auth import get_user_model

AuPairUser = get_user_model()
# Create your models here.


class AuPairNearBy(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(AuPairUser, on_delete=models.CASCADE, related_name="me")
    enabled = models.BooleanField(default=False, db_index=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    # nearby_users = models.ForeignKey('self', on_delete=models.CASCADE, related_name='nearby')

    def __str__(self):
        return '%s: %s, %s' % (str(self.enabled), str(self.latitude), str(self.longitude))
