import uuid

import auto_prefetch
from ckeditor.fields import RichTextField
from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.text import slugify

from softskillspace.utils.choices import ForumApproval
from softskillspace.utils.models import NamedTimeBasedModel, TimeBasedModel
from softskillspace.utils.strings import get_words_from_html


class PostCategory(NamedTimeBasedModel):

    class Meta:
        verbose_name_plural = "Post Categories"


class Post(TimeBasedModel):
    user = auto_prefetch.ForeignKey(
        "home.CustomUser", on_delete=models.CASCADE, null=True
    )
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True, max_length=200)
    content = RichTextField()
    approved = models.CharField(
        max_length=100,
        default=ForumApproval.Pending,
        choices=ForumApproval.choices)
    categories = models.ManyToManyField('forum.PostCategory')
    view_count = models.IntegerField(default=0)
    likes = models.ManyToManyField(
        'home.CustomUser',
        blank=True,
        related_name='likes'
    )

    def save(self, *args, **kwargs):
        uuid_start = str(uuid.uuid1()).split("-", 1)[0]
        if not self.pk:
            self.slug = slugify(self.title) + "-" + uuid_start

        super().save()

    def __str__(self):
        return str(self.title)

    @property
    def minute_read(self):
        # // returns the integer part.
        # assuming 250 words per minute
        word_list = get_words_from_html(self.content)
        return len(word_list) // 250

    @property
    def total_likes(self):
        return self.likes.count()


class ForumComment(TimeBasedModel):
    forum = auto_prefetch.ForeignKey(
        Post, on_delete=models.CASCADE, null=True
    )
    user = auto_prefetch.ForeignKey(
        "home.CustomUser", on_delete=models.CASCADE, null=True
    )
    comment = models.TextField(max_length=200)

    @property
    def comments(self):
        return truncatechars(self.comment, 50)

    def __str__(self):
        return self.forum.title
