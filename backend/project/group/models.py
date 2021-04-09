from django.db import models
from django.contrib.auth import get_user_model

# from message.models import Message
# Create your models here.
from message.models import Message

AuPairUser = get_user_model()


class Group(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    group_creator = models.ForeignKey(AuPairUser, on_delete=models.CASCADE, related_name='group_creator')
    group_name = models.CharField(max_length=255)
    group_users = models.ForeignKey(AuPairUser, on_delete=models.CASCADE, related_name='group_users')
    group_chat = models.ForeignKey(Message, on_delete=models.CASCADE)

    def __str__(self):
        return '%s: %s' % (str(self.group_name), str(self.date_created))
