from django.db import models


class ContactType(models.TextChoices):
    CALL = ('call', 'Call')
    EMAIL = ('email', 'E-mail')
    MEETING = ('meeting', 'Meeting')
