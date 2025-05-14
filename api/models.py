from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)  # 기본값을 설정

    def __str__(self):
        return self.title
