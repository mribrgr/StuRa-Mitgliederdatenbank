from django.shortcuts import render, get_object_or_404
import random


# Create your views here.
def main_screen(request):
    context = {
        'aemter_set': [{
            'name': 'Verwaltung',
            'leitung': 'Mary Waves',
            'stellvertretung': 'Captain Beefart',
            'mitglieder': [
                {'name': 'Bart Glover'},
                {'name': 'Lemmy Kilmister'},
                {'name': 'Bill Newton'}
                ]
            }, 
            {'name': 'Kultur',
            'leitung': 'Karel Heavy',
            'stellvertretung': 'Gerald Trost',
            'mitglieder': [
                {'name': 'Alexendre Hebert'},
                {'name': 'Benjamin Mitchner'},
                {'name': 'Atomfried Müller'}
                ]
            },
            {'name': 'Personal',
            'leitung': 'Dave Mustaine',
            'stellvertretung': 'Ozzy Osbourne',
            'mitglieder': [
                {'name': 'Chuck Norris'},
                {'name': 'Tony Stark'},
                ]
            }
        ]
    }


    return render(request, 'aemter/main_screen.html', context)
