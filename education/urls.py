from django.urls import path
from rest_framework.routers import DefaultRouter

from education.apps import EducationConfig
from education.views import (
  SectionViewSet,
  MaterialListAPIView,
  MaterialRetrieveAPIView,
  MaterialCreateAPIView,
  MaterialUpdateAPIView,
  MaterialDestroyAPIView)

app_name = EducationConfig.name

router = DefaultRouter()
router.register(r'section', SectionViewSet, basename='section')

urlpatterns = [
  # Список материалов
  path('material_list/',
       MaterialListAPIView.as_view(), name='material_list'),

  # Детальная информация по материалу
  path('material_retrieve/<int:pk>/',
       MaterialRetrieveAPIView.as_view(), name='material_retrieve'),

  # Создание материала
  path('material_create/',
       MaterialCreateAPIView.as_view(), name='material_create'),

  # Редактирование материала
  path('material_update/<int:pk>/',
       MaterialUpdateAPIView.as_view(), name='material_update'),

  # Удаление материала
  path('material_destroy/<int:pk>/',
       MaterialDestroyAPIView.as_view(), name='material_destroy'),

] + router.urls  # Присоединяем разделы
