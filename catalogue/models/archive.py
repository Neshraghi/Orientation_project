from django.db import models


class Archive(models.Model):
    class Meta:
        app_label = "catalogue"

    name = models.CharField(max_length=255)
    city = models.CharField(max_length=127)
    siglum = models.CharField(max_length=127)
    country = models.CharField(max_length=127)

    def __str__(self):
        return "{0}".format(self.name)

