from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = "usuarios"

urlpatterns = [
    path('', views.login_view, name='login'),  # Usa LoginView directamente
    path('inicio/', views.index, name='index'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]