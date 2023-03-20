from django.urls import path

from event import views

app_name = "event"


urlpatterns = [
    path(
        "",
        view=views.EventListView.as_view(),
        name="eventlist",
    ),
    path(
        "<int:pk>/",
        view=views.EventDetailView.as_view(),
        name="eventdetail",
    ),
]
