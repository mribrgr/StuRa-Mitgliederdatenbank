from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.template import RequestContext

from datetime import datetime

from mitglieder.models import Mitglied, MitgliedMail, MitgliedAmt
from aemter.models import Referat, Unterbereich, Amt, Recht, AmtRecht

# Create your views here.
def list(request):
    # Access restrictions
    if not request.user.is_authenticated:
        messages.error(request, "Du musst angemeldet sein, um diese Seite sehen zu können.")
        return redirect("/")
    if not request.user.is_superuser:
        messages.error(request, "Du musst Admin sein, um diese Seite aufrufen zu können.")
        return redirect("/mitglieder")

    # Fetch data
    mitglieder = Mitglied.history.all()

    return render(request=request,
                  template_name="historie/list.html",
                  context={"mitglieder":mitglieder})
