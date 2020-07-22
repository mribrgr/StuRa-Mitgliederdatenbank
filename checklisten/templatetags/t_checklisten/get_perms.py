from django import template

from checklisten.models import ChecklisteRecht

register = template.Library()

@register.filter
def get_perms(checklist_id):
    perms = ChecklisteRecht.objects.filter(checkliste_id=checklist_id)
    return perms