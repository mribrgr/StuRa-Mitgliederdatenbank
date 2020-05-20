from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.template import RequestContext

from datetime import datetime

from mitglieder.models import Mitglied, MitgliedMail, MitgliedAmt
from aemter.models import Referat, Unterbereich, Amt, Recht, AmtRecht
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
def list(request):
    # Access restrictions
    if not request.user.is_authenticated:
        messages.error(request, "Du musst angemeldet sein, um diese Seite sehen zu können.")
        return redirect("/")
    if not request.user.is_superuser:
        messages.error(request, "Du musst Admin sein, um diese Seite aufrufen zu können.")
        return redirect("/mitglieder")

    searchterm = request.GET.get('search')

    if searchterm is not None:
        searchterms = searchterm.split(',')
        
        # Create empty QuerySets to unionize against
        mitglieder = Mitglied.history.none()
        mitgliederMails = MitgliedMail.history.none()
        mitgliederAemter = MitgliedAmt.history.none()
        referate = Referat.history.none()
        unterbereiche = Unterbereich.history.none()
        aemter = Amt.history.none()
        rechte = Recht.history.none()
        aemterRechte = AmtRecht.history.none()
        users = User.history.none()

        # Iterate over all given search terms and fetch all entries matching any of the terms
        for term in searchterms:
            term = term.strip()
            mitglieder = mitglieder | Mitglied.history.filter(Q(id__icontains=term) | Q(vorname__icontains=term) | Q(name__icontains=term))
            mitgliederMails =  mitgliederMails | MitgliedMail.history.filter(Q(mitglied__id__icontains=term) | Q(mitglied__vorname__icontains=term) | Q(mitglied__name__icontains=term) | Q(email__icontains=term))
            mitgliederAemter = mitgliederAemter | MitgliedAmt.history.filter(Q(mitglied__id__icontains=term) | Q(mitglied__vorname__icontains=term) | Q(mitglied__name__icontains=term) 
                | Q(amt__id__icontains=term) | Q(amt__bezeichnung__icontains=term) 
                | Q(amt__referat__bezeichnung__icontains=term)
                | Q(amt__unterbereich__bezeichnung__icontains=term))

            referate = referate | Referat.history.filter(Q(id__icontains=term) | Q(bezeichnung__icontains=term))
            unterbereiche = unterbereiche | Unterbereich.history.filter(Q(id__icontains=term) | Q(bezeichnung__icontains=term) | Q(referat__id__icontains=term) | Q(referat__bezeichnung__icontains=term))
            aemter = aemter | Amt.history.filter(Q(id__icontains=term) | Q(bezeichnung__icontains=term) 
                | Q(referat__id__icontains=term) | Q(referat__bezeichnung__icontains=term) 
                | Q(unterbereich__id__icontains=term) | Q(unterbereich__bezeichnung__icontains=term))
            rechte = rechte | Recht.history.filter(Q(id__icontains=term) | Q(bezeichnung__icontains=term))
            aemterRechte = aemterRechte | AmtRecht.history.filter(Q(amt__id__icontains=term) | Q(amt__bezeichnung__icontains=term) 
                | Q(amt__referat__bezeichnung__icontains=term)
                | Q(amt__unterbereich__bezeichnung__icontains=term)
                | Q(recht__id__icontains=term) |Q(recht__bezeichnung__icontains=term))

            users = users | User.history.filter(Q(username__icontains=term) | Q(first_name__icontains=term) | Q(last_name__icontains=term) | Q(email__icontains=term))
    else:
        # Fetch all entries
        mitglieder = Mitglied.history.all()
        mitgliederMails = MitgliedMail.history.all()
        mitgliederAemter = MitgliedAmt.history.all()

        referate = Referat.history.all()
        unterbereiche = Unterbereich.history.all()
        aemter = Amt.history.all()
        rechte = Recht.history.all()
        aemterRechte = AmtRecht.history.all()

        users = User.history.all()

        searchterm=""

    return render(request=request,
                  template_name="historie/list.html",
                  context={"mitglieder":mitglieder,
                           "mitgliederMails":mitgliederMails,
                           "mitgliederAemter":mitgliederAemter,
                           "referate":referate,
                           "unterbereiche":unterbereiche,
                           "aemter":aemter,
                           "rechte":rechte,
                           "aemterRechte":aemterRechte,
                           "users":users,
                           "searchterm":searchterm})
