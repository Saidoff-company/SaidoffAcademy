from django.db import models
from django.utils.translation import gettext_lazy as _
from common.validatorsfile import *
from django.core.validators import RegexValidator, URLValidator


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Company(BaseModel):
    phone = models.CharField(max_length=20, validators=[phone_validator])
    location_text = models.CharField(max_length=255)
    facebook = models.URLField(validators=[URLValidator(), facebook_validator])
    linkedin = models.URLField([URLValidator(), linkedin_validator])
    instagram = models.URLField([URLValidator(), instagram_validator])
    telegram = models.URLField([URLValidator(), telegram_validator])

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')


class WhyUs(BaseModel):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(_("title"), max_length=255)
    description = models.TextField(_("description"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('WhyUs')
        verbose_name_plural = _('WhyUs')


class Course(BaseModel):
    title = models.CharField(_("title"), max_length=100)
    description = models.TextField(_("description"))
    image = models.ImageField(upload_to='courses/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('course')
        verbose_name_plural = _('courses')


class CoursePlan(BaseModel):
    course_duration_time = models.CharField(max_length=100)
    theory_duration_time = models.CharField(max_length=100)
    theory_text = models.TextField(_("practical_text"))
    practical_duration_time = models.CharField(max_length=100)
    practical_text = models.TextField(_("practical_text"))
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.course_duration_time

    class Meta:
        verbose_name = _("course plan")
        verbose_name_plural = _("course plans")


class CourseModule(BaseModel):
    text = models.CharField(_("text"), max_length=250)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = _("course module")
        verbose_name_plural = _("course modules")


class ModuleLesson(BaseModel):
    text = models.CharField(_("text"), max_length=250)
    course_module = models.ForeignKey(CourseModule, on_delete=models.CASCADE, related_name='modules')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = _("module lesson")
        verbose_name_plural = _("module lessons")


class CourseMentor(BaseModel):
    image = models.ImageField(upload_to="course_mentor/%Y/%m/%d")
    experience = models.TextField(_("experience"))
    projects_involved = models.TextField()
    disciple = models.TextField(_("disciple"))
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['course', 'id']
        verbose_name = _("course mentor")
        verbose_name_plural = _("course mentors")


class PlaceOfWork(BaseModel):
    logo = models.ImageField(upload_to="logos/")
    course_mentor = models.ForeignKey(CourseMentor, on_delete=models.CASCADE, related_name='places')

    class Meta:
        verbose_name = _("place of work")
        verbose_name_plural = _("places of work")


class UserContactApplication(BaseModel):
    name = models.CharField(_("name"), max_length=100)
    phone = models.CharField(max_length=100, validators=[phone_validator])
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('user contact application')
        verbose_name_plural = _('user contact applications')


class OurProgram(BaseModel):
    image = models.ImageField(upload_to="programs/")
    title = models.CharField(_("title"), max_length=100)
    description = models.TextField(_("description"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('our program')
        verbose_name_plural = _('our programs')


class OurProgramInfo(BaseModel):
    order = models.IntegerField(default=1)
    text = models.TextField(_("text"))
    program = models.ForeignKey(OurProgram, on_delete=models.CASCADE, related_name='our_program_infos')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = _('Our program info')
        verbose_name_plural = _('Our program infos')


class StudentFeedback(BaseModel):
    text = models.TextField(_("text"))
    full_name = models.CharField(max_length=100)
    course_name = models.CharField(_("course_name"), max_length=100)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _("Student Feedback")
        verbose_name_plural = _("Student Feedback")


class Partner(BaseModel):
    image = models.ImageField(upload_to="partners/")
    link = models.URLField()

    class Meta:
        verbose_name = _("partner")
        verbose_name_plural = _("partners")


class Team(BaseModel):
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="teams/")
    job = models.CharField(_("job"), max_length=100)

    class Meta:
        verbose_name = _("team")
        verbose_name_plural = _("teams")

    def __str__(self):
        return self.full_name


class FAQ(BaseModel):
    question = models.CharField(_("question"), max_length=250)
    answer = models.TextField(_("answer"))

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = _("FAQ")
        verbose_name_plural = _("FAQs")


class Computer(BaseModel):
    processor = models.CharField(_("processor"), max_length=100)
    CPU = models.CharField(_("CPU"), max_length=100)
    GPU = models.CharField(_("GPU"), max_length=100)
    display = models.CharField(_("display"), max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.processor

    class Meta:
        verbose_name = _("computer")
        verbose_name_plural = _("computers")
