from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

class LanguageChoices(models.TextChoices):
    ENGLISH = 'english', _('English')
    GERMAN = 'german', _('German')
    CZECH = 'czech', _('Czech')
    SPANISH = 'spanish', _('Spanish')

class QuestionSet(models.Model):
    topic_name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    questions_language = models.CharField(
        max_length=200, 
        choices=LanguageChoices.choices, 
        default=LanguageChoices.ENGLISH
    )
    answer_language = models.CharField(max_length=200, choices=LanguageChoices.choices)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.topic_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.topic_name} {self.questions_language}-{self.answer_language}'


class Question(models.Model):
    set = models.ForeignKey(
        QuestionSet,
        on_delete=models.SET_NULL,
        related_name='set',
        null=True
    )
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    is_noun = models.BooleanField(default=True)
    article = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.question