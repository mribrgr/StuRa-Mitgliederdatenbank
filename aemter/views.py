from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


# Create your views here.
def main_screen(request):
    context = {
        'referate_set': [{
            'leitung': 'Varchar Toll',
            'stellvertretung': 'Marie Johanna',
            'name': 'Referat 1',
            'bereiche_set': [{
                    'name': 'Bereich 1',
                    'leitung': 'Mary Waves',
                    'stellvertretung': 'Captain Beefart',
                    'weitere_mitglieder': [
                    {'name': 'Bart Glover'},
                    {'name': 'Lemmy Kilmister'},
                    {'name': 'Bill Newton'}
                    ]
                },
                {
                    'name': 'Bereich 2',
                    'leitung': 'Mary Waves',
                    'stellvertretung': 'Captain Feebart',
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
            'leitung': 'Klaus Kleber',
            'stellvertretung': 'Jehns Spahn',
            'bereiche_set': [{
                    'leitung': 'Abbath Doom Occulta',
                    'stellvertretung': 'Johnny Thunder',
                    'name': 'Bereich 1',
                    'leitung': 'Karel Heavy',
                    'stellvertretung': 'Gerald Trost',
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
            'leitung': 'Alexi Laiho',
            'stellvertretung': 'Konrad Adenauer',
            'bereiche_set': [{
                    'name': 'Bereich 1',
                    'leitung': 'Dave Mustaine',
                    'stellvertretung': 'Ozzy Osbourne',
                    'weitere_mitglieder': [
                        {'name': 'Chuck Norris'},
                        {'name': 'Tony Stark'},
                    ]
                },
            ]
        },
        ]
    }

    return render(request, 'aemter/main_screen.html', context)




    
