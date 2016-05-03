from django.db import models


class Composition(models.Model):
    class Meta:
        app_label = "catalogue"

    #Andrew used this instead of:  name = models.CharField(max_length=255)
    title = models.CharField(max_length=64)
    anonymous = models.BooleanField(default=False)
