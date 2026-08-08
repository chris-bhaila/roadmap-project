from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class AdminPanelAccessTests(TestCase):
    def setUp(self):
        self.url = reverse('admin_panel:dashboard')

    def test_anonymous_redirected_to_login(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('accounts:login'), response.url)

    def test_non_staff_user_redirected(self):
        User.objects.create_user(username='student', password='pass12345')
        self.client.login(username='student', password='pass12345')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('accounts:login'), response.url)

    def test_staff_user_allowed(self):
        User.objects.create_user(username='staffer', password='pass12345', is_staff=True)
        self.client.login(username='staffer', password='pass12345')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
