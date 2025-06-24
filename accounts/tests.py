from django.contrib.auth import get_user_model
from .models import Country, Device, Profile
from django.test import TestCase
from datetime import datetime
import uuid


User = get_user_model()

class AccountTests(TestCase):
    @classmethod
    def setUpTestData(cls):

        cls.country = Country.objects.create(
            name='Iran',
            abbr='IR'
        )

        cls.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password123'
        )

        cls.profile = Profile.objects.create(
            user=cls.user,
            phone_number='09121234567',
            country=cls.country
        )

        cls.device = Device.objects.create(
            user=cls.user,
            device_uuid=uuid.uuid4(),
            last_login=datetime.now(),
            device_type=Device.ANDROID,
            device_os='Android 13',
            device_model='Samsung S21',
            app_version='1.2.3'
        )

    def test_profile_created(self):
        self.assertEqual(self.profile.user.username, 'testuser')
        self.assertEqual(self.profile.country.abbr, 'IR')

    def test_device_created(self):
        self.assertEqual(self.device.user.email, 'test@example.com')
        self.assertEqual(self.device.device_type, Device.ANDROID)
        self.assertEqual(self.device.device_model, 'Samsung S21')
        self.assertEqual(self.device.app_version, '1.2.3')
        self.assertIsNotNone(self.device.device_uuid)
