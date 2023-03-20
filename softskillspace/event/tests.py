from django.test import TestCase
from event.models import Event


class EventTestCase(TestCase):
    def setUp(self):
        self.event = Event.objects.create(
            title="test title",
            description="test_description",
            price=20.00,
            location="online",
            visible=True
        )

    def test_event_created(self):
        event_count = Event.items.count()
        self.assertEqual(1, event_count)
