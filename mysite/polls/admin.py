from django.contrib import admin
from polls.models import Question


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['question_text']}),
        ('Date information',    {'fields': ['pub_date'], 'classes':
                                 ['collapse']}),
    ]


# Register your models here.
admin.site.register(Question, QuestionAdmin)
