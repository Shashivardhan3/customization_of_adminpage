from django.contrib import admin

# Register your models here.

from app.models import *


class CustomStudent(admin.ModelAdmin):
    list_display=['Sname','Sid','Semail']
    list_display_links=["Sid"]
    list_editable=['Sname','Semail',]
    list_per_page=2
    list_filter=['Semail']
    search_fields=['Sname']
admin.site.register(Student,CustomStudent)
