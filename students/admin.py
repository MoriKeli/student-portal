from django.contrib import admin
from .models import Assignment, StudentProfile, AcademicProfile, Units

admin.site.register(StudentProfile)
admin.site.register(AcademicProfile)
admin.site.register(Units)
admin.site.register(Assignment)
