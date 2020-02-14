from django.shortcuts import render, HttpResponse

# Create your views here
import docker

client = docker.from_env()


def index(request):
    return HttpResponse("Django nginx Test Accomplished!! + secret = "+client.secrets.list())