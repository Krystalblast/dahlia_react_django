from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
AuPairUser = get_user_model()


class Message(models.Model):
    date_created = models.DateTimeField()
    message_creator = models.ForeignKey(AuPairUser, on_delete=models.CASCADE, related_name='message_creator')
    message_receiver = models.ForeignKey(AuPairUser, on_delete=models.CASCADE, related_name='message_receiver')
    message_text = models.CharField(max_length=1020)
    message_media = models.URLField()

    def __str__(self):
        return str(self.message_text) + " " + str(self.date_created)
