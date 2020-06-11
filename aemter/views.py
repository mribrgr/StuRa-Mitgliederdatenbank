from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Organisationseinheit, Unterbereich, Funktion
from mitglieder.models import MitgliedAmt

# Create your views here.
def main_screen(request):
    if not request.user.is_authenticated:
        messages.error(request, "Du musst angemeldet sein, um diese Seite sehen zu können.")
        return redirect("/")

    referate = Organisationseinheit.objects.all().order_by('id')
    paginator = Paginator(referate, 15) # Show 15 entries per page
    page_number = request.GET.get('page') # Get page number from request
    referate_page = paginator.get_page(page_number) # Get entries for that page
    referat_ids = referate_page.object_list.values_list('id', flat=True) # Get IDs of those entries

    # Only get associated data for current page
    unterbereiche = Unterbereich.objects.filter(referat__id__in=referat_ids)
    aemter = Funktion.objects.filter(referat__id__in=referat_ids)
    amt_ids = aemter.values_list('id', flat=True)
    mitglieder = MitgliedAmt.objects.filter(funktion__id__in=amt_ids)

    context = {
        'referate': referate_page,
        'unterbereiche': unterbereiche,
        'aemter': aemter,
        'mitglieder': mitglieder
    }

    return render(request, 'aemter/main_screen.html', context)
