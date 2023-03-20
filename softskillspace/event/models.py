from ckeditor.fields import RichTextField
from django.db import models
from django.utils import timezone
from django_resized import ResizedImageField
from softskillspace.utils.media import get_image_upload_path
from softskillspace.utils.models import TimeBasedModel


class Event(TimeBasedModel):
    title = models.CharField(max_length=100)
    description = RichTextField()
    location = models.CharField(max_length=200, default="online")
    deadline = models.DateTimeField(default=timezone.now)
    image = ResizedImageField(
        upload_to=get_image_upload_path,
        blank=True,
        verbose_name="Event banner",
        null=True,
    )
    price = models.FloatField(default=0)

    def __str__(self):
        return self.title
