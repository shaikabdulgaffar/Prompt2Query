from django.test import TestCase
from django.contrib.auth.models import User
from .models import DatabaseConnection

class DatabaseConnectionTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='testpass')
        self.db_conn = DatabaseConnection.objects.create(
            user=self.user,
            db_type='postgresql',
            host='localhost',
            port=5432,
            username='postgres',
            password='password',
            db_name='testdb'
        )

    def test_db_connection_str(self):
        self.assertIn('postgresql', str(self.db_conn))