from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=400)
    summary = models.TextField()
    text = models.TextField()
    tag = models.TextField(max_length=50)
    type = models.TextField(max_length=50)
    lang = models.CharField(max_length=2)
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title


class Now(models.Model):
    now = models.TextField()
    def __str__(self):
        return self.now
