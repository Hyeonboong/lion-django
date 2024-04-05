from django.db import models

# Create your models here.
# title, url

class Bookmark(models.Model):
    title = models.CharField('TITLE', max_length=100, blank =True) # 최대길이 100, 공백허용 TRUE
    url = models.URLField('URL', unique=True)
    def __str__(self):
        return self.title + " " + self.url