from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def consul_check_app(request):
    return HttpResponse(status=200)
