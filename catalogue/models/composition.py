from django.db import models


class Composition(models.Model):
    class Meta:
        app_label = "catalogue"

    #Andrew used this instead of:  name = models.CharField(max_length=255)
    title = models.CharField(max_length=64)
    anonymous = models.BooleanField(default=False)

    #Relationships
    source = models.ForeignKey("catalogue.Source")
    composer = models.ForeignKey("catalogue.Composer", blank=True, null=True)
    #compositions belong to sources and also belong to a composer

    def __str__(self):
        return "{0}".format(self.shelfmark)