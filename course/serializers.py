from django.shortcuts import get_object_or_404
from rest_framework import serializers

from course.models import Course, Paying, CourseSubscription
from lesson.models import Lesson
from user.models import User


class PayingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Paying
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    paying = PayingSerializer(many=True)
    is_subscribed = serializers.SerializerMethodField()

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        subscribed = CourseSubscription.objects.filter(course=obj, user=user, is_subscribed=True).exists()
        return subscribed

    def create(self, validated_data):
        payings_data = validated_data.pop('paying')
        lessons_data = validated_data.pop('lessons')
        course = Course.objects.create(**validated_data)

        course.lessons.set(lessons_data)

        for paying_data in payings_data:
            Paying.objects.create(course=course, **paying_data)

        return course

    class Meta:
        model = Course
        fields = ['id', 'name', 'preview', 'description', 'lessons', 'paying', 'is_subscribed']



class CourseSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSubscription
        fields = ['user', 'course', 'is_subscribed']