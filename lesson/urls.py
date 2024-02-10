from django.urls import path

from lesson.views import LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonDestroyAPIView, \
    LessonUpdateAPIView

app_name = 'lesson'


urlpatterns = [
    path('/', LessonListAPIView.as_view(), name='lesson-list'),
    path('create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-retrieve'),
    path('<int:pk>/delete/', LessonDestroyAPIView.as_view(), name='lesson-delete'),
    path('<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson-update'),
]
