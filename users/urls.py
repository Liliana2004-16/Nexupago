from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
]
