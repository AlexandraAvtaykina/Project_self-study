from rest_framework import status
from rest_framework.test import APITestCase

from education.models import Material, Section
from users.models import User


class LessonApiTestCase(APITestCase):
    """ Тесты на CRUD материала"""

    def setUp(self) -> None:
        user = User.objects.create(email='test@test.test', is_active=True)
        user.set_password('test_password')
        user.save()
        response = self.client.post(
            '/users/api/token/',
            data={"email": "test@test.test", "password": "test_password"})
        self.token = response.json()["access"]

        self.user = user

    def test_create_material(self):
        """ Тестирование создания материала"""

        heard = {
            "Authorization": f"Bearer {self.token}"
        }
        section = Section.objects.create(
            title='Тестовый раздел',
            description='Тест'
        )

        data = {
            "title": "Test",
            "description": "Test",
            "section": section.id
        }

        response = self.client.post(
            '/education/material_create/',
            data=data,
            headers=heard
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(Material.objects.all().exists())

    def test_list_material(self):
        """ Тестирование вывода списка материалов """

        section = Section.objects.create(
            title='Тестовый раздел',
            description='Тест',
        )

        Material.objects.create(
            title='Тестовый материал',
            description='Тест',
            url=section,
            author=self.user
        )

        heard = {
            "Authorization": f"Bearer {self.token}"
        }

        response = self.client.get(
            '/education/material_list/',
            headers=heard
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_retrieve_material(self):
        """Тестирование вывода одного материала"""

        course = Section.objects.create(
            title='Тестовый раздел',
            description='Тест',
        )
        material = Material.objects.create(
            title='Тестовый материал',
            description='Тест',
            url=course,
            author=self.user
        )
        heard = {
            "Authorization": f"Bearer {self.token}"
        }

        response = self.client.get(
            f'/education/material_retrieve/{material.id}/',
            headers=heard
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_material(self):
        """Тестирование редактирования материала"""

        section = Section.objects.create(
            title='Тестовый раздел',
            description='Тест',
        )
        material = Material.objects.create(
            title='Тестовый материал',
            description='Тест',
            url=section,
            author=self.user
        )

        heard = {
            "Authorization": f"Bearer {self.token}"
        }
        data = {
            'title': 'Test material update'
        }

        response = self.client.patch(
            f'/education/material_update/{material.id}/',
            data=data,
            headers=heard
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()['title'],
            'Test material update'
        )

    def test_delete_material(self):
        """Тестирование удаления материла"""

        section = Section.objects.create(
            title='Тестовый раздел',
            description='Тест',
        )
        material = Material.objects.create(
            title='Тестовый материал',
            description='Тест',
            url=section,
            author=self.user
        )
        heard = {
            "Authorization": f"Bearer {self.token}"
        }

        response = self.client.delete(
            f'/education/material_destroy/{material.id}/',
            headers=heard
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
