from django.urls import path

from career import views

app_name = "career"


urlpatterns = [
    path(
        "",
        view=views.CareerListView.as_view(),
        name="careerlist",
    ),
    path(
        "<int:pk>/",
        view=views.CareerDetailView.as_view(),
        name="careerdetail",
    ),
]
