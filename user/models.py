from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import MaxValueValidator, MinValueValidator


class UserAccountManager(BaseUserManager):
    def create_user(self, email, username, name, phone=None, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          phone=phone, name=name)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, username, name, phone, password):
        user = self.create_user(email, username, name, phone, password)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    phone = models.PositiveIntegerField(
        blank=True, validators=[MaxValueValidator(9999999999, message="Phone number must be 10 character"), MinValueValidator(1000000000, message="Phone number must be 10 character")])
    name = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone', 'name']

    def __str__(self):
        return self.username
