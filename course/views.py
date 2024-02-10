from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from course.models import Course, Paying, CourseSubscription
from course.paginators import CustomPaginator
from course.permissions import CoursePermission
from course.serializers import CourseSerializer, PayingSerializer, CourseSubscriptionSerializer
from lesson.models import Lesson

from rest_framework import serializers, viewsets



class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    # permission_classes = [CoursePermission]
    pagination_class = CustomPaginator

    def perform_create(self, serializer):
        lessons_data = self.request.data.get('lessons', [])

        new_course = serializer.save(author=self.request.user)

        for lesson_id in lessons_data:
            lesson = Lesson.objects.get(pk=lesson_id)
            new_course.lessons.add(lesson)


class PayingListView(generics.ListAPIView):
    serializer_class = PayingSerializer
    queryset = Paying.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'method_to_pay',)
    ordering_fields = ('date_to_pay',)

class PayingCreateView(generics.CreateAPIView):
    serializer_class = PayingSerializer


class CourseSubscriptionViewSet(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, course_id):
        try:
            course = Course.objects.get(id=course_id)
            subscription, created = CourseSubscription.objects.get_or_create(user=request.user, course=course)

            if not subscription.is_subscribed:
                subscription.is_subscribed = True
                subscription.save()
                print("You have just successfully subscribed")
            else:
                subscription.is_subscribed = False
                subscription.save()
                print("You have successfully cancelled subscribing")

            serializer = CourseSubscriptionSerializer(subscription)
            return Response(serializer.data, status=200)
        except Course.DoesNotExist:
            return Response(status=404)