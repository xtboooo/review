from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello_view_func(request):
  return HttpResponse("<h1>hello world</h1>")