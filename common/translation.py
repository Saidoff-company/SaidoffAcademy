from modeltranslation.translator import register, TranslationOptions

from common import models


@register(models.WhyUs)
class WhyUsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
