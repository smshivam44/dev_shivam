from django.db import models
from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.core.mail import EmailMessage
from django.contrib.postgres.fields import ArrayField

import jwt
from rest_framework_jwt.utils import jwt_payload_handler



# Create your models here.


class AppUserManager(BaseUserManager):
    """
    Inherits BaseUserManager class
    """

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


# Base User Table used same for Authentication Purpose

class AppUser(AbstractBaseUser, PermissionsMixin):
    """
    docstring for AppUser
    """
    name = models.CharField('Name', max_length=20, blank=True, null=True)
    email = models.EmailField('Email', max_length=60, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AppUserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return str(self.email)

    def create_jwt(self):
        """Function for creating JWT for Authentication Purpose"""
        payload = jwt_payload_handler(self)
        token = jwt.encode(payload, settings.SECRET_KEY)
        auth_token = token.decode('unicode_escape')
        return auth_token

   
    def get_full_name(self):
        return "self.name"

    def get_short_name(self):
        return "self.name"

    def send_welcome_mail(self, message):
        """
        Defines welcome mail when the user is created
        """
        email = EmailMessage('Activate your account.', message, 'Dekore App<a@a.com>', to=[self.email])
        email.content_subtype = "html"
        email.send()

    class Meta:
        """docstring for meta"""
        verbose_name = "user"
        verbose_name_plural = "User Details"
