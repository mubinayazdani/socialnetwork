from django.contrib.auth.models import User
from django.conf import settings
from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=50)
    abbr = models.CharField(max_length=5)
    is_active = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'country'
        verbose_name_plural = 'countries'
        db_table = 'countries'


class Profile(models.Model):
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=40,blank=True, null=True, unique=True)
    country = models.ForeignKey(to=Country, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, upload_to='profile_avatars/')


class Device(models.Model):
    WEB = 1
    IOS = 2
    ANDROID = 3
    PC = 4

    DEVICE_TYPE_CHOICES = (
        (WEB, 'web'),
        (IOS, 'ios'),
        (ANDROID, 'android'),
        (PC, 'ps')
    )

    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='devices', on_delete=models.CASCADE)
    device_uuid = models.UUIDField('device UUID', null=True)
    last_login = models.DateTimeField('last login date', null=True)
    device_type = models.PositiveSmallIntegerField(choices=DEVICE_TYPE_CHOICES, default=ANDROID)
    device_os = models.CharField(max_length=50, blank=True)
    device_model = models.CharField(max_length=50, blank=True)
    app_version = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = 'device'
        verbose_name_plural = 'devices'
        db_table = 'user_devices'
