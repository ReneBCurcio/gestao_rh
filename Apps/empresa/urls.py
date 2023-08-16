from django.urls import path, include
from .views import empresaCreate, editEmpresa


urlpatterns = [
    path('novo', empresaCreate.as_view(), name='criar empresa'),
    path('editar/<int:pk>', editEmpresa.as_view(), name='edite_empresa'),
]