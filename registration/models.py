"Custom Models"
from django.db import models

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class CustomUserManaer(BaseUserManager):
    def create_user(self, email, username, password):
        """Creates and saves a user given an email, username and password
        """
        if not email:
            raise ValueError('Users must have an email adress')
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, password):
        """Creates and saves a user given an email, username and password
        """
        user = self.create_user(
            username=username,
            email=email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True
        )
    username = models.CharField(
        verbose_name="username",
        max_length=255,
        unique=True
    )
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    is_admin = models.BooleanField(default=False)
    object = CustomUserManaer()    
    def __str__(self):              # __unicode__ on Python 2
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
