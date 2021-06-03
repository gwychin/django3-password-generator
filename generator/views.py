from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/index.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('Uppercase'):
        characters.extend(list('ABCDEFGHIJLMNOPQRSTUVWXYZ'))
    if request.GET.get('Numbers'):
        characters.extend(list('1234567890'))
    if request.GET.get('Special Characters'):
        characters.extend(list('!#$%&*+-./:;<=>?@[\]^_~'))

    length = int(request.GET.get('length',12))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})
