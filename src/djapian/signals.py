"""
Here are the post_save and the pre_delete signals
"""
from djapian.models import Change

def post_save(sender, instance, created, *args, **kwargs):
    '''Create the Change object to update the index'''
    Change.objects.create(object=instance, action="add" if created else "edit")

def pre_delete(sender, instance, *args, **kwargs):
    '''Create the Change object to update the index'''
    Change.objects.create(object=instance, action="delete")
