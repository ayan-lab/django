from django.conf import settings
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class LikedItem(models.Model):
    # if a user is deleted, delete all fields user liked
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # type of items user liked
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # identifying that item
    object_id = models.PositiveIntegerField()
    # resding actual object
    object_content = GenericForeignKey()