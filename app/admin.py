from django.contrib import admin
from .models import services
from .models import blogg
from .models import employee
# Register your models here.

admin.site.register(services)
admin.site.register(blogg)
admin.site.register(employee)
# 