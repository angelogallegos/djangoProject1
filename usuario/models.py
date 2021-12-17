from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# clases para el contrlol de cuentas personalizada

class MyAccountManager(BaseUserManager):
    # sobreescribir funciones del baseusermanager para que funcione la abstracbaseuser personalizada
    def create_user(self, email, username, nombres, apellidos, password=None):
        if not email:
            raise ValueError("El email es requerido")
        if not username:
            raise ValueError("Es necesario establecer un usuario")
        if not nombres:
            raise ValueError("Completa este campo")
        if not apellidos:
            raise ValueError("Completa este campo")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            nombres=nombres,
            apellidos=apellidos
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, nombres, apellidos, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            nombres=nombres,
            apellidos=apellidos
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True, default='')
    username = models.CharField(max_length=30, unique=True, default='')
    nombres = models.CharField(max_length=100, blank=False, null=False, default='')
    apellidos = models.CharField(max_length=100, blank=False, null=False, default='')

    # campos propios del abstract model

    date_joined = models.DateTimeField(verbose_name='date_joined', auto_now=True)
    last_login = models.DateTimeField(verbose_name='last_login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # definir con se desea logear al sistema, en este caso con el email

    USERNAME_FIELD = 'username'
    # Que campos seran requeridos al registrarse

    REQUIRED_FIELDS = ['nombres', 'apellidos']

    objects = MyAccountManager()

    def __str__(self):
        return self.username


    # funciomes propias y necesarias para que funcione el custom user model
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True