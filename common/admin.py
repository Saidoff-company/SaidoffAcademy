from django.contrib import admin
from common import models
from modeltranslation.admin import TranslationAdmin


class CompanyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if models.Company.objects.count() == 0:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class WhyUsAdmin(TranslationAdmin):
    pass


class CoursePlanInline(admin.TabularInline):
    model = models.CoursePlan


class CourseMentorInline(admin.TabularInline):
    model = models.CourseMentor

class CourseModuleInline(admin.TabularInline):
    model = models.CourseModule

class CourseAdmin(admin.ModelAdmin):
    inlines = [CoursePlanInline, CourseMentorInline, CourseModuleInline]


admin.site.register(models.Company, CompanyAdmin)
admin.site.register(models.WhyUs, WhyUsAdmin)
admin.site.register(models.CoursePlan)
admin.site.register(models.ModuleLesson)
admin.site.register(models.CourseModule)
admin.site.register(models.PlaceOfWork)
admin.site.register(models.CourseMentor)
admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.UserContactApplication)
admin.site.register(models.OurProgramInfo)
admin.site.register(models.OurProgram)
admin.site.register(models.StudentFeedback)
admin.site.register(models.Partner)
admin.site.register(models.Team)
admin.site.register(models.FAQ)
admin.site.register(models.Computer)

