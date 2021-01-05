from django.contrib import admin
from .models import Resume, Skill, Education, Experience
# Register your models here.

admin.site.register(Resume)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Experience)