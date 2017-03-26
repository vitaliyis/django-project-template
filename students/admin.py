from django.contrib import admin
from .models import Student, Group

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Student._meta.fields]

    class Meta:
        model = Student

admin.site.register(Student, StudentAdmin)

class GroupAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Group._meta.fields]

    class Meta:
        model = Group
admin.site.register(Group, GroupAdmin)
