from django.contrib.auth.models import AbstractUser
from django.db import models

from core.models import TimeStampMixin, UUIDPrimaryKeyMixin
from users.enums import Role
from users.managers import UserManager


class User(UUIDPrimaryKeyMixin, TimeStampMixin, AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=Role, default=Role.USER)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def is_admin(self):
        return self.role == Role.ADMIN

    @property
    def is_staff_member(self):
        return self.role == Role.STAFF
