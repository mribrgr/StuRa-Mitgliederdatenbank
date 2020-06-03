from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Referat, Unterbereich, Amt
from mitglieder.models import MitgliedAmt

# Create your views here.
def main_screen(request):
    if not request.user.is_authenticated:
        messages.error(request, "Du musst angemeldet sein, um diese Seite sehen zu können.")
        return redirect("/")

    context = {
        'referate': Referat.objects.all(),
        'unterbereiche': Unterbereich.objects.all(),
        'aemter': Amt.objects.all(),
        'mitglieder': MitgliedAmt.objects.all()
    }

    return render(request, 'aemter/main_screen.html', context)
