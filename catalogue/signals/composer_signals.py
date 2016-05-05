from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from catalogue.models.composer import Composer
from catalogue.helpers.solr_helpers import solr_index, solr_delete
from catalogue.serializers.search.composer import ComposerSearchSerializer


#when receive the post_save signal
@receiver(post_save, sender=Composer)
def index_composer(sender, instance, created, **kwargs):
    print('Composer added')
    solr_index(ComposerSearchSerializer, [instance])
    #it will pass in the class and the instance of the class that is being saved, and a flag to tell you if it is a new instance or an existing (creating or updating)

@receiver(post_delete, sender=Composer)
def delete_composer(sender, instance, **kwargs):
    print('Composer deleted')
    solr_delete([instance])
    #no need to create a flag for delete
