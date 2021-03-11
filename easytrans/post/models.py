from django.db import models

# Create your models here.
class Poster(models.Model):
    title = models.CharField(max_length=120)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title