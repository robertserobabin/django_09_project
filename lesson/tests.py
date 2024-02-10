from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from .models import Lesson

class LessonCRUDTests(APITestCase):
    def setUp(self):
        super().setUp()

        self.lesson = Lesson.objects.create(
            name='Test Lesson',
            preview=None,
            description='Test Lesson Description',
            link='https://www.youtube.com/watch?v=1234567890'
        )

        self.lesson_serializer_data = {
            'name': 'New Lesson',
            'preview': None,
            'description': 'New Lesson Description',
            'link': 'https://www.youtube.com/watch?v=1234567890'
        }

    def test_create_lesson(self):
        url = reverse('lesson:lesson-create')
        self.lesson_serializer_data['preview'] = ''
        response = self.client.post(url, self.lesson_serializer_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.count(), 2)
        self.assertEqual(Lesson.objects.last().name, 'New Lesson')

    def test_retrieve_lesson(self):
        url = reverse('lesson:lesson-retrieve', args=[self.lesson.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Lesson')

    def test_update_lesson(self):
        lesson = Lesson.objects.create(id=1, name='Lesson 1', preview='Some preview')
        url = reverse('lesson:lesson-update', kwargs={'pk': 1})
        self.lesson_serializer_data['preview'] = ''
        response = self.client.put(url, self.lesson_serializer_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        lesson.refresh_from_db()
        self.assertEqual(lesson.name, 'New Lesson')