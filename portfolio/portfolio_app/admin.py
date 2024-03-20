from django.contrib import admin
from .models import Education, Certification, WorkExperience, Project, Blog, ContactForm
# Register your models here.

admin.site.register(Education)
admin.site.register(Certification)
admin.site.register(WorkExperience)
admin.site.register(Project)
admin.site.register(Blog)
admin.site.register(ContactForm)