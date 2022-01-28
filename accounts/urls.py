from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
  path('', LoginView.as_view(template_name='index.html'), name='login'),
  path('add/', views.add, name='add')
]