from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
# Create your models here.
AuPairUser = get_user_model()


class Post(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, default=timezone.now)
    post_creator = models.ForeignKey(AuPairUser, on_delete=models.CASCADE, related_name='post_creator')
    post_text = models.CharField(max_length=255)
    post_liked = models.ForeignKey(AuPairUser, on_delete=models.CASCADE, related_name='post_liked')
    post_replies = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies')
    post_media = models.URLField()

    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return str(self.post_text) + " " + str(self.date_created)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})


class Comments(models.Model):
    post = models.ForeignKey(Post, related_name='details', on_delete=models.CASCADE)
    comment_creator = models.ForeignKey(AuPairUser, related_name='details', on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=255)
    comment_date = models.DateTimeField(default=timezone.now, auto_now_add=True)


class Like(models.Model):
    like_creator = models.ForeignKey(AuPairUser, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)

# Credit: Kumar Shubham Jan 3, 2021 Originally published at towardsdatascience.com
# Link: https://dev.to/shubham1710/build-a-social-media-website-with-django-feed-app-backend-part-4-4hn4
