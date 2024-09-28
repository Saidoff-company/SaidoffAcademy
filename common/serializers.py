from rest_framework import serializers

from common import models


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = '__all__'


class WhyUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WhyUs
        fields = ['id', 'image', 'title', 'description']


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['id', 'title', 'description', 'image']


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Partner
        fields = ['id', 'image', 'link']


class OurProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OurProgram
        fields = ['id', 'image', 'title', 'description']


class StudentFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentFeedback
        fields = ['id', 'full_name', 'text', 'image', 'course_name']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Team
        fields = ['id', 'image', 'job', 'full_name']


class UserContactApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserContactApplication
        fields = ['id', 'phone', 'name', 'course']


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FAQ
        fields = ['id', 'question', 'answer']


class ProgramInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OurProgramInfo
        fields = ['id', 'order', 'text']


class OurProgramInfoSerializer(serializers.ModelSerializer):
    program_info = ProgramInfoSerializer(many=True, source='our_program_infos')

    class Meta:
        model = models.OurProgram
        fields = ['id', 'title', 'program_info']


class CoursePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CoursePlan
        fields = ['id', 'course_duration_time', 'theory_duration_time', 'theory_text', 'practical_duration_time', 'practical_text']


class PlaceOfWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PlaceOfWork
        fields = ['id', 'logo']


class CourseMentorSerializer(serializers.ModelSerializer):
    place_of_work = PlaceOfWorkSerializer(many=True, source='places')

    class Meta:
        model = models.CourseMentor
        fields = ['id', 'image', 'experience', 'projects_involved', 'disciple', 'place_of_work']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModuleLesson
        fields = ['id', 'text', 'course_module']


class CourseModuleSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(source='modules', many=True)

    class Meta:
        model = models.CourseModule
        fields = ['id', 'text', 'lesson']


class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Computer
        fields = ['id', 'processor', 'CPU', 'GPU', 'display',]


class CourseSerializer(serializers.ModelSerializer):
    course_mentor = CourseMentorSerializer(read_only=True)
    course_plan = CoursePlanSerializer(read_only=True)

    class Meta:
        model = models.Course
        fields = ['id', 'title', 'description', 'image', 'course_mentor', 'course_plan']