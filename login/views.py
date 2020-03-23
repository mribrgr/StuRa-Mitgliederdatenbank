from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def main_screen(request):
    return render(request=request,
                  template_name="login/login.html")