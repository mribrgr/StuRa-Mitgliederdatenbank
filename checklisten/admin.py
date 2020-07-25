from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import Checkliste, Aufgabe, ChecklisteAufgabe, ChecklisteRecht

admin.site.register(Checkliste, SimpleHistoryAdmin)
admin.site.register(Aufgabe, SimpleHistoryAdmin)
admin.site.register(ChecklisteAufgabe, SimpleHistoryAdmin)
admin.site.register(ChecklisteRecht, SimpleHistoryAdmin)
