from django.urls import path, include
from .views import Colaboradoreslist

urlpatterns = [
    path('', Colaboradoreslist.as_view(), name='list_colaboradores'),
]
