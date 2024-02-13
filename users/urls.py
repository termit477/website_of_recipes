from django.urls import path
from django.contrib.auth import views as auth_views
from .views import logout, profile, registration

urlpatterns = [
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]