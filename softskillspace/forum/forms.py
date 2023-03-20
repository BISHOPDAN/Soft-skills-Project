from django import forms

from softskillspace.utils.forms import CssForm

from .models import ForumComment


class ForumCommentForm(CssForm, forms.ModelForm):
    class Meta:
        model = ForumComment
        fields = ['comment']
