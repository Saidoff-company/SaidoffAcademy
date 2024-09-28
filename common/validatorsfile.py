from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, URLValidator
import re

phone_validator = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Telefon raqami to'g'ri formatda emas. Format: +998901234567"
)


def facebook_validator(value):
    if not re.match(r'^https?://(www\.)?facebook.com/.+', value):
        raise ValidationError("Facebook URL noto'g'ri. URL www.facebook.com bilan boshlanishi kerak.")


def linkedin_validator(value):
    if not re.match(r'^https?://(www\.)?linkedin.com/.+', value):
        raise ValidationError("LinkedIn URL noto'g'ri. URL www.linkedin.com bilan boshlanishi kerak.")


def instagram_validator(value):
    if not re.match(r'^https?://(www\.)?instagram.com/.+', value):
        raise ValidationError("Instagram URL noto'g'ri. URL www.instagram.com bilan boshlanishi kerak.")


def telegram_validator(value):
    if not re.match(r'^https?://t\.me/.+', value):
        raise ValidationError("Telegram URL noto'g'ri. URL t.me bilan boshlanishi kerak.")
