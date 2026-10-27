from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from catalog.models import ConsultationRequest


class UserAuthenticationUITest(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = "test_client"
        self.password = "SecurePass123!"
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password,
            email="client@example.com"
        )

    def test_user_login_success(self):
        login_url = reverse("catalog:login")
        response_get = self.client.get(login_url)
        self.assertEqual(response_get.status_code, 200)
        self.assertContains(response_get, "Вхід")

        response_post = self.client.post(
            login_url,
            {"username": self.username, "password": self.password},
            follow=True
        )
        self.assertEqual(response_post.status_code, 200)
        self.assertTrue(response_post.context["user"].is_authenticated)
        self.assertContains(response_post, f"Раді бачити Вас знову, {self.username}!")


class ConsultationRequestUITest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_consultation_form_submission_success(self):
        consultation_url = reverse("catalog:consultation")
        response_get = self.client.get(consultation_url)
        self.assertEqual(response_get.status_code, 200)
        self.assertContains(response_get, "Консультація")

        form_data = {
            "client_name": "Олена Мельник",
            "phone": "+380501234567",
            "email": "olena@example.com",
            "occasion_description": "Річниця весілля",
            "preferences": "Ніжні рожеві півонії та евкаліпт"
        }
        response_post = self.client.post(consultation_url, data=form_data, follow=True)
        self.assertEqual(response_post.status_code, 200)
        self.assertContains(response_post, "Дякуємо, Олена Мельник!")
        self.assertTrue(
            ConsultationRequest.objects.filter(phone="+380501234567").exists()
        )
