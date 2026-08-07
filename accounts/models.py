from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom user model with a role field distinguishing students from admins.

    Swapped in via AUTH_USER_MODEL so the role travels with every request as
    `request.user.role`.
    """

    class Role(models.TextChoices):
        STUDENT = 'student', 'Student'
        ADMIN = 'admin', 'Admin'

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.STUDENT,
    )

    @property
    def is_student(self):
        return self.role == self.Role.STUDENT

    @property
    def is_admin(self):
        return self.role == self.Role.ADMIN

    def __str__(self):
        return f'{self.username} ({self.get_role_display()})'
