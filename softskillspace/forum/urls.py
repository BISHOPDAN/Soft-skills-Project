from django.urls import path

from forum import views, ajax_views

app_name = "forum"

urlpatterns = [
    path(
        "",
        view=views.ForumListView.as_view(),
        name="forum-list",
    ),
    path(
        "<slug:slug>/",
        view=views.ForumDetailView.as_view(),
        name="forum-detail",
    ),
    path(
        "post/likes/<slug:slug>/",
        view=ajax_views.ForumPostLikesView.as_view(),
        name="like-post",
    ),
]
