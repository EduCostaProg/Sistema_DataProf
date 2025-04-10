from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, profile

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', profile, name='profile'),
]
