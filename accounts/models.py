from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name,username, email, password=None):
        if not email:
            raise ValueError('User must have an email addrss')
        if not username:
            raise ValueError('User must have an username addrss')
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            
        )
        
        user.set_password(password)
        user.save(using = self.db)
        return user
    
    def create_superuser(self, first_name, last_name, username, email, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        
        user.is_admin = True
        user.is_active = True
        user.is_superadmin = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    

class Account(AbstractBaseUser):
    email = models.EmailField(max_length=50, unique=True)  
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=50, unique=True)
    Phone_number = models.CharField(max_length=50)
    
# required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login= models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name', 'last_name']
    object = MyAccountManager()
    
    def __self__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True