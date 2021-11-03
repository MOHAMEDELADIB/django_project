# serializers.py
from rest_framework import serializers

from .models import Course

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'university', 'state', 'campus', 'description', 'learningOutcomes', 'fees', 'yearlyFees', 'guaranteedAtar', 'duration', 'units', 'uniRanking', 'url')