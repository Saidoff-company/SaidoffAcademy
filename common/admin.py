from django.contrib import admin
from django.utils.safestring import mark_safe

from common import models
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline, TranslationStackedInline


@admin.register(models.WhyUs)
class WhyUsAdmin(TranslationAdmin):
    list_display = ['id', 'title']
    list_display_links = list_display


@admin.register(models.CoursePlan)
class CoursePlanAdmin(admin.ModelAdmin):
    list_display = ['id']
    list_display_links = list_display

    def has_module_permission(self, request):
        return False


class CoursePlanInline(TranslationStackedInline):
    model = models.CoursePlan
    extra = 0


@admin.register(models.PlaceOfWork)
class PlaceOfWorkAdmin(admin.ModelAdmin):
    list_display = ['id', 'logo']

    def has_module_permission(self, request):
        return False


class PlaceOfWorkInline(TranslationStackedInline):
    model = models.PlaceOfWork
    extra = 0


@admin.register(models.CourseMentor)
class CourseMentorAdmin(admin.ModelAdmin):
    inlines = [PlaceOfWorkInline]
    list_display = ['id',]

    def has_module_permission(self, request):
        return False


class CourseMentorInline(TranslationStackedInline):
    model = models.CourseMentor
    extra = 0
    fields = ['link', 'image', 'experience', 'projects_involved', 'disciple']
    readonly_fields = ['link']

    def link(self, instance):
        url = f"/admin/common/coursementor/{instance.id}/change/"
        return mark_safe(f'<a target="_blank" href="{url}">Kirish</a>')


@admin.register(models.ModuleLesson)
class ModuleLessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'text']
    list_display_links = list_display

    def has_module_permission(self, request):
        return False


class ModuleLessonInline(TranslationTabularInline):
    model = models.ModuleLesson
    extra = 0


@admin.register(models.CourseModule)
class CourseModuleAdmin(admin.ModelAdmin):
    list_display = ['id', 'text']
    list_display_links = list_display
    inlines = [ModuleLessonInline]

    def has_module_permission(self, request):
        return False


class CourseModuleInline(TranslationTabularInline):
    model = models.CourseModule
    extra = 0
    fields = ['link', 'text']
    readonly_fields = ['link']

    def link(self, instance):
        url = f"/admin/common/coursemodule/{instance.id}/change/"
        return mark_safe(f'<a target="_blank" href="{url}">Kirish</a>')


@admin.register(models.Computer)
class ComputerAdmin(admin.ModelAdmin):
    list_display = ['id',]

    def has_module_permission(self, request):
        return False


class ComputerInline(TranslationStackedInline):
    model = models.Computer
    extra = 0


@admin.register(models.OurProgramInfo)
class OurProgramInfoAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False


class OurProgramInfoInline(TranslationStackedInline):
    model = models.OurProgramInfo
    extra = 0
    fields = ['link', 'order', 'text']
    readonly_fields = ['link']

    def link(self, instance):
        url = f"/admin/common/ourprograminfo/{instance.id}/change/"
        return mark_safe(f'<a target="_blank" href="{url}">Kirish</a>')


@admin.register(models.OurProgram)
class OurProgramAdmin(admin.ModelAdmin):
    inlines = [OurProgramInfoInline]


@admin.register(models.UserContactApplication)
class UserContactApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_checked']
    list_display_links = list_display
    list_filter = ['is_checked']


@admin.register(models.StudentFeedback)
class StudentFeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name']
    list_display_links = list_display


@admin.register(models.Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name']


@admin.register(models.FAQ)
class FAQAdmin(TranslationAdmin):
    list_display = ['id', 'question']


@admin.register(models.WhoFieldFor)
class WhoFieldFor(TranslationAdmin):
    def has_module_permission(self, request):
        return False


class WhoFieldForInline(TranslationStackedInline):
    model = models.WhoFieldFor
    extra = 0


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = list_display
    inlines = [CoursePlanInline, CourseMentorInline, CourseModuleInline, ComputerInline, WhoFieldForInline]
