from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def main_screen(request):

    numbers = [1, 2, 3, 4, 5]

    return render(request=request,
                  template_name="mitglieder/mitglieder.html",
                  context = {"data":numbers})

#
# TODO: Richtige Probe Datensätze
# TODO: Preview Fesnster mit mehr inhalten
# 