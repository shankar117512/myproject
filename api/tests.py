from django.test import TestCase, Client
from django.urls import reverse


class HealthCheckTestCase(TestCase):
    """Tests for health check endpoint."""

    def setUp(self):
        self.client = Client()

    def test_health_check_returns_200(self):
        """Health endpoint must return 200 on healthy system."""
        response = self.client.get('/health/')
        self.assertEqual(response.status_code, 200)

    def test_health_check_json_response(self):
        """Health endpoint must return valid JSON with status field."""
        response = self.client.get('/health/')
        data = response.json()
        self.assertIn('status', data)
        self.assertEqual(data['status'], 'ok')

    def test_health_check_database_field(self):
        """Health endpoint must include database status."""
        response = self.client.get('/health/')
        data = response.json()
        self.assertIn('database', data)
        self.assertEqual(data['database'], 'healthy')

    def test_admin_accessible(self):
        """Admin URL must be accessible (redirect to login)."""
        response = self.client.get('/admin/')
        self.assertIn(response.status_code, [200, 301, 302])
