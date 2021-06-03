from django.contrib import admin
import api.models as api_models

# Register your models here.

admin.site.register(api_models.User)
admin.site.register(api_models.Course)
admin.site.register(api_models.Lecture)

