from django.urls import path
from .views import index, target_processing, target_archive, login_user, logout_user, register

urlpatterns = [
    path('', index, name='index'),
    path('reigster', register, name='register'),
    path('login', login_user, name='login_user'),
    path('logout', logout_user, name='logout_user'),
    path('target_processing/<int:target_id>/', target_processing, name='target_processing'),
    path('target_archive', target_archive, name='target_archive')
]
