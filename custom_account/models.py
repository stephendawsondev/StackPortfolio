from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class ParentUserManager(BaseUserManager):
    """
    Create a custom user manager class that
    extends BaseUserManager.
    """

    def create_user(
            self,
            email,
            username,
            first_name,
            last_name,
            password=None,
            town_city=None,
            display_town_city=False,
            country=None,
            display_email=False,
            website=None,
            phone_number=None,
            display_phone_number=False,
            profile_image=None,
            bio=None,
            work_title=None,
            company=None,
            linkedin_username=None,
            twitter_handle=None,
    ):
        """
        Create and return a `ParentUser` with an email, username,
        first name, last name, and password.
        """
        if email is None:
            raise TypeError('Users must have an email address.')
        if username is None:
            raise TypeError('Users must have a username.')
        if first_name is None:
            raise TypeError('Users must have a first name.')
        if last_name is None:
            raise TypeError('Users must have a last name.')

        user = self.model(
            # normalize_email() is used to lowercase
            # the domain part of the email address.
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
            self,
            email,
            username,
            first_name,
            last_name,
            password=None):
        """
        Create and return a `ParentUser` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(
            email, username, first_name, last_name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class ParentUser(AbstractBaseUser, PermissionsMixin):
    """
    Create a custom user model that uses
    Django's User model as a base.
    """
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=60, unique=True)
    first_name = models.CharField(max_length=40, blank=False, null=False)
    last_name = models.CharField(max_length=40, blank=False, null=False)
    town_city = models.CharField(max_length=85, blank=True, null=True)
    display_town_city = models.BooleanField(default=False)
    country = models.CharField(max_length=60, blank=True, null=True)
    display_email = models.BooleanField(default=False)
    website = models.URLField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    display_phone_number = models.BooleanField(default=False)
    profile_image = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    work_title = models.CharField(max_length=80, blank=True, null=True)
    company = models.CharField(max_length=80, blank=True, null=True)
    linkedin_username = models.CharField(max_length=80, blank=True, null=True)
    twitter_handle = models.CharField(max_length=80, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = ParentUserManager()