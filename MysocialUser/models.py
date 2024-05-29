from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class MySocialUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El correo electronico es obligatorio')
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Los super usuarios deben tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Los super usuarios deben tener is_superuser=True.')
        
        return self.create_user(username, email, password, **extra_fields)
    
class MySocialUser(AbstractBaseUser):
    username = models.CharField(max_length=70, unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    name = models.CharField(max_length=50)
    surnames = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email =  models.EmailField(max_length=254, verbose_name='correo electronico', unique=True)
    profileimg = models.ImageField(upload_to='profiles/',default='profile_picture.jpeg')
    activation_token = models.CharField(max_length=100, blank=True, null=True)
    objects = MySocialUserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    def __str__(self) -> str:
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser
    
    def has_module_perms(self, app_label):
        return self.is_superuser