from http import HTTPStatus
from allauth.account.models import EmailAddress
from django.test import TestCase
from django.urls import reverse_lazy
from django.utils import timezone as tz
from home.models import CustomUser
from softskillspace.utils.choices import AcademicLevel, InstitutionType
from subject.models import InstitutionClassification, Subject
from tutor.models import (
    Tutor,
    TutorAvailability,
    TutorRequest,
    TutorSubject,
    TutorQualification
)


class Test(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        run this setup before any test
        """
        cls.current_time_zone = tz.get_current_timezone()
        cls.user = CustomUser.objects.create_user(
            username="jack",
            email="jackdoe@test.com",
            password="testpassword",
            is_active=True,
        )

        EmailAddress.objects.create(
            user=cls.user,
            email=cls.user.email,
            verified=True,
            primary=True
        )

        # Simple subject with just a name for simplicity
        cls.subject = Subject.objects.create(
            name="Django"
        )

        cls.institution_class = InstitutionClassification.objects.create(
            name="Test Institute"
        )

        cls.tutor = Tutor.objects.create(
            user=cls.user,
            bio="Test Bio",
            rate_per_hour=100,
            verified_at=tz.datetime.now(tz=cls.current_time_zone),
            id_documents_provided="Test Doc",
            account_no="123456789",
            sort_code="ABD12CD",
            street="Test Street",
            town="Test Town",
            city="Test City",
            post_code="12345"
        )

        cls.tutor_qualification = TutorQualification.objects.create(
            tutor=cls.tutor,
            institution_name="Test Insitute",
            institution_type=InstitutionType.College,
            course_taken="Django",
            level=AcademicLevel.PhD,
            start_date=tz.datetime.now().date(),
            end_date=tz.datetime.now().date()
        )

        cls.tutor_subject = TutorSubject.objects.create(
            tutor=cls.tutor,
            subject=cls.subject,
        )

        cls.tutor_subject.levels.add(cls.institution_class)

        # A signal automaticaticaly creates the TutorAvaibility
        # So I'll just get the user and check if its created
        cls.tutor_availability = TutorAvailability.objects.get(
            tutor=cls.tutor,
        )

        cls.tutor_request = TutorRequest.objects.create(
            full_legal_name="Test Test",
            date_of_birth=tz.datetime.now().date(),
            email_address="test.softskillspace.com",
            whatsapp_number="081234567890",
            name_of_subject_you_teach="Django",
            highest_academic_qualification="PhD, Masters, BSc, HND"
        )

    def test_all_tutor_app_models_are_created(self):
        """
        Test if command creates all tutor models
        """
        self.assertEqual(Tutor.objects.count(), 1)
        self.assertEqual(TutorAvailability.objects.count(), 1)
        self.assertEqual(TutorQualification.objects.count(), 1)
        self.assertEqual(TutorRequest.objects.count(), 1)
        self.assertEqual(TutorSubject.objects.count(), 1)

    def test_subject_creation_form(self):
        """
        Test subject creation payload
        """
        print(self.institution_class)

        self.client.force_login(self.tutor.user)
        valid_payload = {
            'subject': self.subject,
            'levels': self.institution_class
        }

        response = self.client.post(
            reverse_lazy("tutor:subjects"),
            data=valid_payload
        )

        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_if_add_subject_form_context_data_exists(self):
        self.client.force_login(self.tutor.user)

        response = self.client.get(reverse_lazy("tutor:subjects"))
        self.assertTrue("form" in response.context)

    def test_tutor_profile_page(self):
        self.client.force_login(self.tutor.user)
        response = self.client.get(
            reverse_lazy("tutor:profile",
                         args=[self.tutor.user.username]))

        assert response.status_code == 200

    def test_tutor_search_page(self):
        self.client.force_login(self.tutor.user)
        response = self.client.get(reverse_lazy("tutor:search"))

        assert response.status_code == 200

    def test_tutor_subject_page(self):
        self.client.force_login(self.tutor.user)
        response = self.client.get(reverse_lazy("tutor:subjects"))

        assert response.status_code == 200
