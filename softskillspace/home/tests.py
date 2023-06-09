from django.test import TestCase
from django.urls import reverse_lazy
from softskillspace.utils.tests import create_user
from home.models import CustomUser


class Test(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        run this setup before any test
        """
        create_user(cls)

    def test_user_is_created(self):
        """
        Test if command creates user
        """
        self.assertEqual(CustomUser.objects.count(), 1)

    def test_real_user_can_login(self):
        """
        Test if login url works and a user with valid credentials can sign-in
        """
        res = self.client.post(
            reverse_lazy("account_login"),
            data={"login": self.user.email, "password": "testpassword"},
        )

        self.assertEqual(res.status_code, 302)
        self.assertTrue(res.wsgi_request.user.is_authenticated)

    def test_fake_user_cannot_login(self):
        """
        Test if a user with invalid credentials is unable to sign in
        """
        res = self.client.post(
            reverse_lazy("account_login"),
            data={"login": "daniel", "password": "password"},
        )
        # print(res.content)
        self.assertFalse(res.wsgi_request.user.is_authenticated)
        self.assertEqual(res.status_code, 200)

    def test_term_of_use_page(self):
        """
        Test if terms of use page works
        """
        res = self.client.get(reverse_lazy("home:terms-of-use"))
        self.assertEqual(res.status_code, 200)
