from django.db import models

# Create your models here.


class Singer(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=40, blank=True, null=True)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Song(models.Model):
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='song')
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    def __str__(self):
        return self.title


