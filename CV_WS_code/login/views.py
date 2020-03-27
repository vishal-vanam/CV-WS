from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("You're at signin page, where signup button is present and also validation of user profile is done")
