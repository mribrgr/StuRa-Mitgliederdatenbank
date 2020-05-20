from django import template

from mitglieder.models import Mitglied, MitgliedMail, MitgliedAmt
from aemter.models import Referat, Unterbereich, Amt, Recht, AmtRecht

register = template.Library()

@register.simple_tag
def get_associated_data(desiredInfo, queryType, primaryKey, timestamp):
    if(desiredInfo == "Mitglied"): foreignClass = Mitglied
    if(desiredInfo == "Amt"): foreignClass = Amt
    if(desiredInfo == "Unterbereich"): foreignClass = Unterbereich
    if(desiredInfo == "Referat"): foreignClass = Referat
    if(desiredInfo == "Recht"): foreignClass = Recht

    if primaryKey == "": return None

    if queryType == "latest":
        # If the referenced object is still in the database
        associatedEntry = foreignClass.objects.filter(id=primaryKey).first()
        if associatedEntry == None:
            # If the referenced object has been deleted
            associatedEntry = foreignClass.history.filter(id=primaryKey).order_by("-history_date").first()

    if queryType == "historical":
        # If the referenced object is still in the database
        instance = foreignClass.objects.filter(id=primaryKey).first()
        if instance != None:
            try:
                associatedEntry = instance.history.as_of(timestamp)
            except:
                # If the referenced object has been created before history was tracked
                associatedEntry = None
        else:
            # If the referenced object has been deleted
            associatedEntry = foreignClass.history.filter(id=primaryKey).filter(history_date__lte=timestamp).order_by("-history_date").first()

    return associatedEntry
