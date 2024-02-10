from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from .models import CourseSubscription, Course
from user.models import User

from .serializers import CourseSubscriptionSerializer


class CourseSubscriptionSerializerTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='testuser@example.com', phone='123456789')

        self.course = Course.objects.create(name='Test Course')
        self.subscription_data = {
            'user': self.user.id,
            'course': self.course.id,
            'is_subscribed': True
        }

    def test_valid_data(self):
        serializer = CourseSubscriptionSerializer(data=self.subscription_data)
        self.assertTrue(serializer.is_valid())
        instance = serializer.save()
        self.assertIsInstance(instance, CourseSubscription)
        self.assertEqual(instance.user, self.user)
        self.assertEqual(instance.course, self.course)
        self.assertTrue(instance.is_subscribed)

    def test_missing_required_fields(self):

        data = self.subscription_data.copy()
        del data['course']
        serializer = CourseSubscriptionSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('course', serializer.errors)

    def test_invalid_data(self):
        # Test invalid 'user' field
        data = self.subscription_data.copy()
        data['user'] = 'invalid_user_id'
        serializer = CourseSubscriptionSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('user', serializer.errors)

        # Test invalid 'course' field
        data = self.subscription_data.copy()
        data['course'] = 'invalid_course_id'
        serializer = CourseSubscriptionSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('course', serializer.errors)




