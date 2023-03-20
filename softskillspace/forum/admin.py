from django.contrib import admin

from forum.models import Post, ForumComment, PostCategory


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ["categories", "approved", "created_at"]
    search_fields = ["title"]
    list_display = ["title", "user", "view_count", "total_likes", "approved"]
    filter_horizontal = ["categories"]
    readonly_fields = ['slug', 'total_likes']


@admin.register(ForumComment)
class ForumCommentAdmin(admin.ModelAdmin):
    list_select_related = ["user", "forum"]
    list_filter = ["created_at"]
    list_display = ["forum", "user", "comments"]
    search_fields = ["forum__title", "user"]


admin.site.register(PostCategory)
