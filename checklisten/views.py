from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def main_screen(request):
    context = {
        'mitglieder': [{
                'name': 'Angela Merkel',
                'aufgaben': [
                    {'name': 'Mailverteiler'},
                    {'name': 'Schließberechtigung'},
                    {'name': 'Berechtigung Website'}
                ]
            },
            {
                'name': 'Jesus Christus',
                'aufgaben': [
                    {'name': 'Schließberechtigung'},
                    {'name': 'Berechtigung Website'}
                ]
            },
            {
                'name': 'Steve Harris',
                'aufgaben': [
                    {'name': 'Mailverteiler'},
                    {'name': 'Berechtigung Website'}
                ]
            },
            {
                'name': 'Dave Lombardo',
                'aufgaben': [
                    {'name': 'Mailverteiler'},
                    {'name': 'Schließberechtigung'},
                ]
            },
            {
                'name': 'Kerry King',
                'aufgaben': [
                    {'name': 'Berechtigung Website'}
                ]
            },
            {
                'name': 'Otto Normalverbraucher',
                'aufgaben': [
                    {'name': 'Mailverteiler'}
                ]
            },
            {
                'name': 'Odowakar Rakawodo',
                'aufgaben': [
                    {'name': 'Schließberechtigung'}
                ]
            }
        ]
    }
    return render(request, 'checklisten/main_screen.html', context)