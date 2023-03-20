from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from forum.forms import ForumCommentForm
from forum.models import ForumComment, Post
from softskillspace.utils.choices import ForumApproval

# Create your views here.


class ForumListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "forum/forum_list.html"
    context_object_name = "forum"
    paginate_by = 25

    def get_queryset(self):
        return Post.items.filter(approved=ForumApproval.Approved) \
            .order_by("-updated_at").prefetch_related('categories') \
            .select_related('user')


class ForumDetailView(LoginRequiredMixin, DetailView, CreateView):
    model = Post
    context_object_name = "forum"
    template_name = "forum/forum_detail.html"
    form_class = ForumCommentForm

    def get_queryset(self):
        return Post.items.filter(approved=ForumApproval.Approved) \
            .order_by("-updated_at").prefetch_related('categories') \
            .select_related('user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        forum_comments = ForumComment.items.select_related(
            "user", "forum"
        )
        already_liked = self.get_object().likes.filter(
            id=self.request.user.id
        ).exists()
        comment_count = forum_comments.count()
        context.update({
            "already_liked": already_liked,
            "forum_comments": forum_comments,
            "comment_count": comment_count,
        })
        return context

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.forum = self.object
        comment.user = self.request.user
        comment.save()

        return redirect("forum:forum-detail", self.kwargs["slug"])
