from rest_framework import views, generics, status
from rest_framework.response import Response

from common import models, serializers


class WhyUsApiView(generics.ListAPIView):
    serializer_class = serializers.WhyUsSerializer
    queryset = models.WhyUs.objects.all()


class CourseListApiView(generics.ListAPIView):
    serializer_class = serializers.CourseListSerializer
    queryset = models.Course.objects.all()


class PartnerListApiView(generics.ListAPIView):
    serializer_class = serializers.PartnerSerializer
    queryset = models.Partner.objects.all()


class OurProgramListApiView(generics.ListAPIView):
    serializer_class = serializers.OurProgramSerializer
    queryset = models.OurProgram.objects.all()


class StudentFeedbackListApiView(generics.ListAPIView):
    serializer_class = serializers.StudentFeedbackSerializer
    queryset = models.StudentFeedback.objects.all()


class TeamListApiView(generics.ListAPIView):
    serializer_class = serializers.TeamSerializer
    queryset = models.Team.objects.all()


class UserContactApplicationCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.UserContactApplicationSerializer
    queryset = models.UserContactApplication.objects.all()


class FAQListApiView(generics.ListAPIView):
    serializer_class = serializers.FAQSerializer
    queryset = models.FAQ.objects.all()


class OurProgramDetailApiView(generics.RetrieveAPIView):
    serializer_class = serializers.OurProgramInfoSerializer

    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        program = models.OurProgram.objects.get(id=id)
        programs = models.OurProgram.objects.exclude(id=id)
        programs_serializer = serializers.OurProgramSerializer(programs, many=True)
        program_info = models.OurProgramInfo.objects.filter(program=program)
        program_serializer = serializers.ProgramInfoSerializer(program_info, many=True)
        serializer = self.serializer_class(program)
        data = {
            'program': serializer.data,
            'programs': [programs_serializer.data],
        }
        return Response(data)


class CourseDetailApiView(generics.RetrieveAPIView):
    serializer_class = serializers.CourseSerializer

    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        course = models.Course.objects.get(id=id)
        course_plan = models.CoursePlan.objects.filter(course=course).first()
        course_mentor = models.CourseMentor.objects.filter(course=course).first()
        course_module = models.CourseModule.objects.filter(course=course)
        computer = models.Computer.objects.filter(course=course).first()
        who_field_for = models.WhoFieldFor.objects.filter(course=course)
        computer_serializer = serializers.ComputerSerializer(computer)
        course_module_serializer = serializers.CourseModuleSerializer(course_module, many=True)
        course_mentor_serializer = serializers.CourseMentorSerializer(course_mentor)
        course_plan_serializer = serializers.CoursePlanSerializer(course_plan)
        who_field_for_serializer = serializers.WhoFieldForSerializer(who_field_for, many=True)
        course_serializer = serializers.CourseSerializer(course)
        data = {
            'course': course_serializer.data,
            'course_plan': course_plan_serializer.data,
            'course_mentor': course_mentor_serializer.data,
            'course_module': course_module_serializer.data,
            'computer': computer_serializer.data,
            'who_field_for': who_field_for_serializer.data,
        }
        return Response(data)
