from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from catalogue.models.source import Source


#when receive the post_save signal
@receiver(post_save, sender=Source)
def index_source(sender, instance, created, **kwargs):
    #it will pass in the class and the instance of the class that is being saved, and a flag to tell you if it is a new instance or an existing (creating or updating)
    print('Source saved')


@receiver(post_delete, sender=Source)
def delete_source(sender, instance, **kwargs):
    #no need to create a flag for delete
    print('Source deleted')
