from ckeditor.fields import RichTextField
from django.db import models
from django.utils import timezone

from softskillspace.utils.choices import JobType
from softskillspace.utils.models import NamedTimeBasedModel, TimeBasedModel

# Create your models here.


class JobCategory(NamedTimeBasedModel):

    class Meta:
        verbose_name_plural = "Job Categories"


class Career(TimeBasedModel):
    title = models.CharField(max_length=300)
    description = RichTextField()
    location = models.CharField(max_length=150)
    jobtype = models.CharField(
        max_length=50, default=JobType.FullTime, choices=JobType.choices
    )
    category = models.ForeignKey(
        "career.JobCategory",
        on_delete=models.CASCADE)
    deadline = models.DateTimeField(default=timezone.now)
    salary = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.title
