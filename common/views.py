from rest_framework import views, generics, status
from rest_framework.response import Response

from common import models, serializers
from common.models import Company


class CompanyApiView(generics.GenericAPIView):
    serializer_class = serializers.CompanySerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(Company.objects.all().first())
        return Response(serializer.data)


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
        program_info = models.OurProgramInfo.objects.filter(program=program)
        program_serializer = serializers.ProgramInfoSerializer(program_info, many=True)
        serializer = self.serializer_class(program)
        return Response(serializer.data)
