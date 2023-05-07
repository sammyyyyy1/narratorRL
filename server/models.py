from django.db import models


class Image(models.Model):

    id = models.CharField(max_length=500, primary_key=True)
    text = models.TextField()

    def __str__(self):
        return f"{self.id}: {self.text[:10]}"
