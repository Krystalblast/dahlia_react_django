from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
AuPairUser = get_user_model()


class Post(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    post_creator = models.ForeignKey(AuPairUser, on_delete=models.CASCADE, related_name='post_creator')
    post_text = models.CharField(max_length=255)
    post_liked = models.ForeignKey(AuPairUser, on_delete=models.CASCADE, related_name='post_liked')
    post_replies = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies')
    post_media = models.URLField()

    def __str__(self):
        return str(self.post_text) + " " + str(self.date_created)
