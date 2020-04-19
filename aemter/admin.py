from django.contrib import admin

from mitglieder.models import Mitglied
from aemter.models import Amt

admin.site.register(Mitglied)
admin.site.register(Amt)
