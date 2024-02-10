from django.urls import path
from rest_framework.routers import DefaultRouter
from course.apps import CourseConfig
from course.views import CourseViewSet, PayingListView, PayingCreateView, CourseSubscriptionViewSet

app_name = CourseConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')


urlpatterns = [

    path('paying/', PayingListView.as_view(), name='paying-list'),
    path('paying/create/', PayingCreateView.as_view(), name='paying-create'),
    path('api/course-subscriptions/<int:course_id>/set_subscription/', CourseSubscriptionViewSet.as_view()),
    ] + router.urls