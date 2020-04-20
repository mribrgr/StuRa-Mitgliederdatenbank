from django.contrib import admin
from .models import Referat
from .models import Unterbereich
from .models import Amt

# Register your models here.
admin.site.register(Referat)
admin.site.register(Unterbereich)
admin.site.register(Amt)
