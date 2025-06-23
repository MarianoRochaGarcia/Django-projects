from django.db import models

class Publication(models.Model):
    tittle = models.CharField(max_length=30)

    def __str__(self):
        return self.tittle


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.headline

                              