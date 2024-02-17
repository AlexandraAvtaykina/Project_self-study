from rest_framework import viewsets
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView,
    CreateAPIView, UpdateAPIView, DestroyAPIView)

from education.models import Section, Material
from education.paginations import MyPaginator
from education.serializers import SectionSerializer, MaterialSerializer


class SectionViewSet(viewsets.ModelViewSet):
    """ Простой ViewSet-класс для вывода информации """
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    pagination_class = MyPaginator

    """ Функция привязывает автора к его разделу"""
    def perform_create(self, serializer):
        serializer.save()
        self.request.user.course_set.add(serializer.instance)

    """ Если юзер не модератор, функция показывает только его разделы"""
    def get_queryset(self):
        if not self.request.user.is_staff:
            return Section.objects.filter(autor=self.request.user)
        elif self.request.user.is_staff:
            return Section.objects.all()


class MaterialListAPIView(ListAPIView):
    """ Отвечает за отображение списка сущностей (Generic-класс)"""

    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
    pagination_class = MyPaginator


class MaterialRetrieveAPIView(RetrieveAPIView):
    """ Отвечает за отображение одной сущности (Generic-класс)"""

    serializer_class = MaterialSerializer
    queryset = Material.objects.all()


class MaterialCreateAPIView(CreateAPIView):
    """ Отвечает за создание сущности (Generic-класс)"""

    serializer_class = MaterialSerializer
    queryset = Material.objects.all()

    """ Функция привязывает автора к его материалу"""
    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.author = self.request.user
        new_lesson.save()


class MaterialUpdateAPIView(UpdateAPIView):
    """ Отвечает за редактирование сущности (Generic-класс)"""

    serializer_class = MaterialSerializer
    queryset = Material.objects.all()


class MaterialDestroyAPIView(DestroyAPIView):
    """ Отвечает за удаление сущности (Generic-класс)"""

    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
