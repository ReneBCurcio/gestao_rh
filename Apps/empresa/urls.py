from django.urls import path, include
from .views import empresaCreate

urlpatterns = [
    path('novo', empresaCreate.as_view(), name='criar empresa'),
]