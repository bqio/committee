from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db.models import CharField, EmailField, BooleanField

class UserManager(BaseUserManager):
  def create_user(self, email, last_name, first_name, middle_name, password=None):
    if not email:
      raise ValueError("Users must have an email")
    user = self.model(
      email=self.normalize_email(email),
      first_name=first_name,
      middle_name=middle_name,
      last_name=last_name
    )
    user.set_password(password)
    user.save(using=self._db)
    return user
  def create_superuser(self, email, last_name, first_name, middle_name, password=None):
    user = self.create_user(
      email,
      first_name,
      middle_name,
      last_name,
      password,
    )
    user.is_admin = True
    user.save(using=self._db)
    return user

class User(AbstractBaseUser):
  email = EmailField(unique=True)
  last_name = CharField(max_length=255)
  first_name = CharField(max_length=255)
  middle_name = CharField(max_length=255)
  is_active = BooleanField(default=True)
  is_admin = BooleanField(default=False)

  USERNAME_FIELD = 'email'

  objects = UserManager()

  def __str__(self):
    return self.email

  def has_perm(self, perm, obj=None):
    return True
  
  def has_module_perms(self, app_label):
    return True
  
  @property
  def is_staff(self):
    return self.is_admin
