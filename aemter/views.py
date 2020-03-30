from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


# Create your views here.
def main_screen(request):
    context = {
        'referate_set': [{
            'name': 'Referat1',
            'leitung': 'Mary Waves',
            'stellvertretung': 'Captain Beefart',
            'mitglieder': [
                {'name': 'Bart Glover'},
                {'name': 'Lemmy Kilmister'},
                {'name': 'Bill Newton'}
                ]
            }, 
            {'name': 'Referat2',
            'leitung': 'Karel Heavy',
            'stellvertretung': 'Gerald Trost',
            'mitglieder': [
                {'name': 'Alexendre Hebert'},
                {'name': 'Benjamin Mitchner'},
                {'name': 'Atomfried Müller'}
                ]
            },
            {'name': 'Referat3',
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
