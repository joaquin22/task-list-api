from django.db import IntegrityError
from apps.user.models import UserAccount
from django.test import TestCase


class TestUserModel(TestCase):

    def setUp(self) -> None:
        self.email = "test@mail.com"
        self.first_name = "Joaquin"
        self.last_name = "Huaman"

    def test_create_user(self) -> None:
        user = UserAccount.objects.create(email=self.email)
        self.assertEqual(user.email, self.email)

    def test_email_unique(self) -> None:
        user = UserAccount.objects.create(email=self.email)
        with self.assertRaises(IntegrityError):
            UserAccount.objects.create(email=self.email)

    def test_get_full_name(self) -> None:
        user = UserAccount.objects.create(
            email=self.email, first_name=self.first_name, last_name=self.last_name
        )

        full_name = f"{self.first_name} {self.last_name}"

        self.assertEqual(user.get_full_name(), full_name)
