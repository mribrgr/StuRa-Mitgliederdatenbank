from django import template

from checklisten.models import ChecklisteAufgabe

register = template.Library()

@register.filter
def get_tasks(checklist_id):
    tasks = ChecklisteAufgabe.objects.filter(checkliste_id=checklist_id)
    return tasks
