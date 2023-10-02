from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


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
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


class SignupPageTests(TestCase):
    username = 'newuser'
    email = 'newuser@email.com'
    password='super_secret_password'
    
    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)
        self.User = get_user_model()
    
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
            self.response, 
            'Hi there! I should not be on the page.'
        )
    
    def test_signup_form(self):
        self.User.objects.create_user(
            username=self.username,
            email=self.email,
            password=self.password
        )
        self.assertEqual(self.User.objects.all().count(), 1)
        self.assertEqual(
            self.User.objects.all()[0].username, 
            self.username
        )
        self.assertEqual(
            self.User.objects.all()[0].email, 
            self.email
        )