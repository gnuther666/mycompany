from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def test_basehttp_response(request):
    return HttpResponse('88888')