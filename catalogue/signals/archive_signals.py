from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from catalogue.models.archive import Archive
from catalogue.helpers.solr_helpers import solr_index, solr_delete
from catalogue.serializers.search.archive import ArchiveSearchSerializer


#when receive the post_save signal
@receiver(post_save, sender=Archive)
def index_archive(sender, instance, created, **kwargs):
    print('Archive added')
    solr_index(ArchiveSearchSerializer, [instance])
    #it will pass in the class and the instance of the class that is being saved, and a flag to tell you if it is a new instance or an existing (creating or updating)

@receiver(post_delete, sender=Archive)
def delete_archive(sender, instance, **kwargs):
    print('Archive deleted')
    solr_delete([instance])
    #no need to create a flag for delete
