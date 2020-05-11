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
        'mitglieder': MitgliedAmt.objects.all(),

        'referate_set': [{
            'leitung': {
                'name': 'Varchar Toll',
            },
            'stellvertretung': {'name': 'Marie Johanna'},
            'name': 'Referat 1',
            'bereiche_set': [{
                    'name': 'Bereich 1',
                    'leitung': {'name':'Mary Waves'},
                    'stellvertretung': {'name':'Captain Beefart'},
                    'weitere_mitglieder': [
                    {'name': 'Bart Glover'},
                    {'name': 'Lemmy Kilmister'},
                    {'name': 'Bill Newton'}
                    ]
                },
                {
                    'name': 'Bereich 2',
                    'leitung': {'name': 'Mary Waves'},
                    'stellvertretung': {'name': 'Captain Feebart'},
                    'weitere_mitglieder': [
                    {'name': 'Bart Lover'},
                    {'name': 'Lemmy Ilmister'},
                    {'name': 'Bill Ewton'}
                    ]
                },
            ]
        },

        {
            'name': 'Referat 2',
            'leitung': {'name':'Klaus Kleber'},
            'stellvertretung': {'name': 'Jehns Spahn'},
            'bereiche_set': [{
                    'name': 'Bereich 1',
                    'leitung': {'name':'Abbath Doom Occulta'},
                    'stellvertretung': {'name':'Johnny Thunder'},
                    'weitere_mitglieder': [
                    {'name': 'Alexendre Hebert'},
                    {'name': 'Benjamin Mitchner'},
                    {'name': 'Atomfried Müller'}
                    ]
                },
            ]
        },

        {
            'name': 'Referat 3',
            'leitung': {'name':'Alexi Laiho'},
            'stellvertretung': {'name': 'Konrad Adenauer'},
            'bereiche_set': [{
                    'name': 'Bereich 1',
                    'leitung': {'name':'Dave Mustaine'},
                    'stellvertretung': {'name':'Ozzy Osbourne'},
                    'weitere_mitglieder': [
                        {'name': 'Chuck Norris'},
                        {'name': 'Tony Stark'},
                    ]
                },
            ]
        },
        ]
    }
    i=0
    for referat in context['referate_set']:
        referat['leitung']['mitid'] = i = i+1
        referat['stellvertretung']['mitid'] = i = i+1
        for bereich in referat['bereiche_set']:
            bereich['leitung']['mitid'] = i = i+1
            bereich['stellvertretung']['mitid'] = i = i+1
            for mitglied in bereich['weitere_mitglieder']:
                mitglied['mitid'] = i = i+1


    return render(request, 'aemter/main_screen.html', context)
