from django.contrib.auth.forms import UserCreationForm as UCF
from .models import User

class UserCreationForm(UCF):
  class Meta():
    model = User
    fields = ['email']