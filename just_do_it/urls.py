from django.urls import path
from .views import index, target_processing, target_archive

urlpatterns = [
    path('', index, name='index'),
    path('target_processing/<int:target_id>/', target_processing, name="target_processing"),
    path('target_archive', target_archive, name='target_archive')
]