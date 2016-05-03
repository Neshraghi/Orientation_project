from django.db import models


class Source(models.Model):
    class Meta:
        app_label = "catalogue"

    shelfmark = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.IntegerField()
    end_date = models.IntegerField()
    type = models.CharField(max_length=127) #we didn't use source_type because using "source" is kind of redundant
    surface = models.CharField(max_length=127, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    #Relationships
    archive = models.ForeignKey("catalogue.Archive")
    #sources belong to archives

    def __str__(self):
        return "{0}".format(self.shelfmark)
        #return self.shelfmark --> returns an object
        #"{0}".format(self.shelfmark) --> returns string