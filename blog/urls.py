from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
]
