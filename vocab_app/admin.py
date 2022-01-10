from django.contrib import admin
from .models import QuestionSet, Question
 
# Register your models here.
admin.site.register(QuestionSet)
admin.site.register(Question)
