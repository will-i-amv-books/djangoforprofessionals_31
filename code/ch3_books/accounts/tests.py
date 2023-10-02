from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='user_1',
            email='user_1@email.com',
            password='super_secret_password'
        )
        self.assertEqual(user.username, 'user_1')
        self.assertEqual(user.email, 'user_1@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


def test_create_superuser(self):
    User = get_user_model()
    user = User.objects.create_superuser(
        username='super_user_1',
        email='super_user_1@email.com',
        password='super_secret_password'
    )
    self.assertEqual(user.username, 'super_user_1')
    self.assertEqual(user.email, 'super_user_1@email.com')
    self.assertTrue(user.is_active)
    self.assertFalse(user.is_staff)
    self.assertFalse(user.is_superuser)
