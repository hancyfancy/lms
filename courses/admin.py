from django.contrib import admin
from courses.models import Course, Material, Content, UserCourseMaterial

admin.site.register(Course)
admin.site.register(Material)
admin.site.register(Content)
admin.site.register(UserCourseMaterial)
