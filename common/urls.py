from django.urls import path
from common import views

urlpatterns = [
    path('why-us/', views.WhyUsApiView.as_view(), name='why-us'),
    path('course/', views.CourseListApiView.as_view(), name='course'),
    path('partner/', views.PartnerListApiView.as_view(), name='partner'),
    path('our-program/', views.OurProgramListApiView.as_view(), name='our-program'),
    path('student-feedback/', views.StudentFeedbackListApiView.as_view(), name='student-feedback'),
    path('team/', views.TeamListApiView.as_view(), name='team'),
    path('contact/', views.UserContactApplicationCreateAPIView.as_view(), name='contact'),
    path('faq/', views.FAQListApiView.as_view(), name='faq'),
    path('our-program/<int:id>/', views.OurProgramDetailApiView.as_view(), name='our-program-info'),
    path('course/<int:id>/', views.CourseDetailApiView.as_view(), name='course'),
]