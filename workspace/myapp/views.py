from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello world, you are at blog index")

def home(request):
    return render(request, 'index.html')