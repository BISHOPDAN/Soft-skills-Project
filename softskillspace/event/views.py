from django.utils import timezone
from django.views.generic import DetailView, ListView

from event.models import Event

# Create your views here.


class EventListView(ListView):
    model = Event
    template_name = "event/list.html"
    context_object_name = "event"
    paginate_by = 6

    def get_queryset(self):
        return Event.objects.exclude(deadline__lte=timezone.now())


class EventDetailView(DetailView):
    model = Event
    context_object_name = "events"
    template_name = "event/detail.html"
