from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
AuPairUser = get_user_model()


class Friend(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(AuPairUser, on_delete=models.CASCADE, related_name='friend_user')
    friend = models.ForeignKey(AuPairUser, on_delete=models.CASCADE, related_name='friend')

    def __str__(self):
        return '%s: %s\n' % (str(self.user), str(self.friend))

    class Meta:
        unique_together = ['user', 'friend']
