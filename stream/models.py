from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomUserManager(BaseUserManager):
    def _create_user(self, username, password, **kwargs):
        if not username:
            raise ValueError("Please introduce your username")
        if not password:
            raise ValueError('Please introduce your password')

        user = self.model(
            username=username,
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_active', True)
        kwargs.setdefault('is_superuser', False)
        return self._create_user(username, password, **kwargs)

    def create_superuser(self, username, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_active', True)
        kwargs.setdefault('is_superuser', True)
        return self._create_user(username, password, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=15, unique=True, null=True)

    is_staff = models.BooleanField(default=True)  # admin group
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ['username']

    def __str__(self):
        return self.username


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sender', blank=False, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver', blank=False, on_delete=models.CASCADE)
    message = models.TextField(max_length=50, blank=False, null=True)
    subject = models.CharField(max_length=15, blank=False, null=True)
    creation_date = models.DateField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-creation_date']

    def __str__(self):
        return self.subject
