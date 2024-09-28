from modeltranslation.translator import register, TranslationOptions

from common import models


@register(models.WhyUs)
class WhyUsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(models.Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(models.CoursePlan)
class CoursePlanTranslationOptions(TranslationOptions):
    fields = ('theory_text', 'practical_text')


@register(models.CourseModule)
class CourseModuleTranslationOptions(TranslationOptions):
    fields = ('text',)


@register(models.ModuleLesson)
class ModuleLessonTranslationOptions(TranslationOptions):
    fields = ('text',)


@register(models.CourseMentor)
class CourseMentorTranslationOptions(TranslationOptions):
    fields = ('experience', 'projects_involved', 'disciple')

@register(models.OurProgram)
class OurProgramTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(models.OurProgramInfo)
class OurProgramInfoTranslationOptions(TranslationOptions):
    fields = ('text',)


@register(models.StudentFeedback)
class StudentFeedbackTranslationOptions(TranslationOptions):
    fields = ('text', 'course_name')


@register(models.Team)
class TeamTranslationOptions(TranslationOptions):
    fields = ('job',)


@register(models.FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')
