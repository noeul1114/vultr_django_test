from django.shortcuts import render, HttpResponse

# Create your views here


def index(request):
    return HttpResponse("Django nginx Test Accomplished!! with Docker swarm!! ")