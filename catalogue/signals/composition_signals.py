from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from catalogue.models.composition import Composition
from catalogue.helpers.solr_helpers import solr_index, solr_delete
from catalogue.serializers.search.composition import CompositionSearchSerializer


#when receive the post_save signal
@receiver(post_save, sender=Composition)
def index_composition(sender, instance, created, **kwargs):
    print('Composition added')
    solr_index(CompositionSearchSerializer, [instance])
    #it will pass in the class and the instance of the class that is being saved, and a flag to tell you if it is a new instance or an existing (creating or updating)

@receiver(post_delete, sender=Composition)
def delete_composition(sender, instance, **kwargs):
    print('Composition deleted')
    solr_delete([instance])
    #no need to create a flag for delete
