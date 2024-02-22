from rest_framework import viewsets
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView,
    CreateAPIView, UpdateAPIView, DestroyAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from education.models import Section, Material, Test
from education.paginations import MyPaginator
from education.serializers import (SectionSerializer, MaterialSerializer,
                                   TestSerializer)


class SectionViewSet(viewsets.ModelViewSet):
    """ ViewSet-класс для работы с разделами """
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    pagination_class = MyPaginator
    permission_classes = [IsAuthenticated]

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
    """ Отвечает за отображение списка материалов"""

    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
    pagination_class = MyPaginator
    permission_classes = [IsAuthenticated]


class MaterialRetrieveAPIView(RetrieveAPIView):
    """ Отвечает за отображение одного материала"""

    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
    permission_classes = [IsAuthenticated]


class MaterialCreateAPIView(CreateAPIView):
    """ Отвечает за создание материала"""

    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
    permission_classes = [IsAuthenticated]

    """ Функция привязывает автора к его материалу"""
    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.author = self.request.user
        new_lesson.save()


class MaterialUpdateAPIView(UpdateAPIView):
    """ Отвечает за редактирование материала"""

    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
    permission_classes = [IsAuthenticated]


class MaterialDestroyAPIView(DestroyAPIView):
    """ Отвечает за удаление материала """

    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
    permission_classes = [IsAuthenticated]


class TestViewSet(viewsets.ModelViewSet):
    """ ViewSet-класс для работы с тестами """

    serializer_class = TestSerializer
    queryset = Test.objects.all()
    permission_classes = [IsAuthenticated]


class TestAPIView(APIView):
    """ Отвечает за ввод ответа на тест и показ правильного ответа """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        answer_input = request.POST.get('answer_input')
        id_test = request.POST.get('id_test')
        test = Test.objects.get(id=id_test)

        if answer_input != test.answer:
            return Response(f'Неверно, правильный ответ - {test.answer}')
        else:
            return Response('Верный ответ!')
