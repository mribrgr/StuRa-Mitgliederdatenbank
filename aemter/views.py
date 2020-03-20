from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def main_screen(request):
    return HttpResponse("This is the aemter screen")