from django.urls import path
from .views import (
    DepartamentosList,
    DepartamentoCreate,
    DepartamentoUpdate,
    DepartamentoDelete
)
urlpatterns = [
    path('', DepartamentosList.as_view(), name='list_departamentos'),
    path('novo', DepartamentoCreate.as_view(), name='create_departamentos'),
    path('editar/<int:pk>/', DepartamentoUpdate.as_view(), name='update_departamento'),
    path('delete/<int:pk>/', DepartamentoDelete.as_view(), name='delete_departamento'),

]