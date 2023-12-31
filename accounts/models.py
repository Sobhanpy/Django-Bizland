from django.db import models

from django.contrib.auth.models import  AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomeUserManager(BaseUserManager):
    def create_user(self,pelake_mashin,password,**extra_fields):
        if not pelake_mashin:
            raise ValueError ('pelake_mashinet ro bede')
        user = self.model(pelake_mashin=pelake_mashin, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,pelake_mashin,password,**extra_fields):

        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_verified', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError ('superuser must be is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError ('superuser must be is_superuser=True')
        if extra_fields.get('is_verified') is not True:
            raise ValueError ('superuser muse be is_verified=True')
        return self.create_user(pelake_mashin,password,**extra_fields)

class CustomeUser(AbstractBaseUser,PermissionsMixin):
    pelake_mashin = models.CharField(unique=True)
    is_active = models.BooleanField (default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    USERNAME_FIELD = 'pelake_mashin'
    objects = CustomeUserManager()

    def __str__(self):
        return self.pelake_mashin

class Profile(models.Model):
    user = models.ForeignKey(CustomeUser,on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    id_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    address = models.TextField()