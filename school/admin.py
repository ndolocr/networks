from django.contrib import admin
from school.models import County, School, StudentClass, Parent, Student, Teacher

# Register your models here.
admin.site.register(County)
admin.site.register(School)
admin.site.register(Parent)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(StudentClass)
