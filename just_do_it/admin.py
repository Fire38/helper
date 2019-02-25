from django.contrib import admin
from .models import Task, Target, Rubric


# Register your models here.
admin.site.register(Task)
admin.site.register(Target)
admin.site.register(Rubric)