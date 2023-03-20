from django.views.generic import DetailView, ListView

from career.models import Career


class CareerListView(ListView):
    model = Career
    template_name = "career/list.html"
    context_object_name = "career"
    paginate_by = 3

    def get_queryset(self):
        search = self.request.GET.get("search", "")
        CareerSearch = Career.objects.filter(title__icontains=search)
        return CareerSearch


class CareerDetailView(DetailView):
    model = Career
    context_object_name = "careers"
    template_name = "career/detail.html"
