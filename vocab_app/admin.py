from django.contrib import admin
from .models import QuestionSet, Question
 
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0

class QuestionSetAdmin(admin.ModelAdmin):
    inlines = [QuestionInline, ]

# Register your models here.
admin.site.register(QuestionSet, QuestionSetAdmin)
admin.site.register(Question)
