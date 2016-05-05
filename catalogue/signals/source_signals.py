from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from catalogue.models.source import Source
from catalogue.helpers.slor_helpers import solr_helpers, solr_delete
from catalogue.serializers.search.source import SourceSearchSerializer


#when receive the post_save signal
@receiver(post_save, sender=Source)
def index_source(sender, instance, created, **kwargs):
    print('Source added')
    solr_index(SourceSearchSerializer, [instance])
    #it will pass in the class and the instance of the class that is being saved, and a flag to tell you if it is a new instance or an existing (creating or updating)

@receiver(post_delete, sender=Source)
def delete_source(sender, instance, **kwargs):
    print('Source deleted')
    solr_delete([instance])
    #no need to create a flag for delete
