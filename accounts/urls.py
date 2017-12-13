from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),
    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    path('register/', views.RegisterFormView.as_view(), name='register'),
    path('profile/', TemplateView.as_view(template_name='accounts/profile.html'), name='profile'),
    path('profile/delete/', views.UserDeleteView.as_view(), name='delete'),
]
