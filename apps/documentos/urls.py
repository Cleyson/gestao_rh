from django.urls import path
from .views import DocumentoCreate


urlpatterns = [
    path('novo', DocumentoCreate.as_view(), name='create_documento'),
   # path('delete/<int:pk>/', DocumentoEdit.as_view(), name='edit_Documento'),
]
