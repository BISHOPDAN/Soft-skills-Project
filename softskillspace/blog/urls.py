from django.urls import path

from blog import views

app_name = "blog"

urlpatterns = [
    path("", views.BlogListView.as_view(), name="index"),
    path("category/<slug:category>/",
         views.BlogListView.as_view(), name="category"),
    path("<str:slug>/", views.BlogDetailView.as_view(), name="detail"),
]
