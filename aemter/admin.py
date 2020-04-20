from django.contrib import admin
from .models import Referat, Unterbereich, Amt

# Register your models here.
admin.site.register(Referat)
admin.site.register(Unterbereich)
admin.site.register(Amt)
