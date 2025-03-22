from django.contrib import admin

from restapp.models import Students


# Register your models here.

class Admin_Student(admin.ModelAdmin):
    list_display =('name','course')



admin.site.register(Students,Admin_Student)
#admin2
#1234
