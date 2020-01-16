from django.shortcuts import render, get_object_or_404
from .models import Letter
# Create your views here.

def home(request):
    return render(request, 'myapp/home.html')


def showlist(request):
    letters = Letter.objects
    return render(request, 'myapp/showlist.html', {'letters' : letters})

    
def read(request, letter_id):
    letter_detail = get_object_or_404(Letter, pk = letter_id) 
    return render(request, 'myapp/read.html', {'letter':letter_detail})

def write(request):
    return render(request, 'myapp/write.html')

def reply(request):
    return render(request, 'myapp/reply.html')