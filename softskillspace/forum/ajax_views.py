
from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from forum.models import Post


class ForumPostLikesView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        """
        Ability to like forum post
        """
        user = request.user
        post = get_object_or_404(Post, slug=kwargs['slug'])
        liked = False

        if post.likes.filter(id=user.id).exists():
            post.likes.remove(request.user)
            post.save()
        else:
            post.likes.add(user)
            post.save()
            liked = True
        data = {
            'liked': liked,
            'total_likes': post.total_likes

        }
        return JsonResponse(data, safe=False)
