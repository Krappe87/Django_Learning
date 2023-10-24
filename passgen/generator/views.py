from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def passgen(request):    
    characters = list('abcdefghijklmnopqrstuvwxyz') 
    numbers = '0123456789'
    capitals = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    symbols = '!@#$%^&*,;:./<>?()'
    thepassword = ''                                
    length = int(request.GET.get('length', 12))     #12 is the default value if the home page was bypassed
    if request.GET.get('Numbers'):                  #Each IF statement is a checkbox
        characters.extend(list(numbers))            #and the function goes down then, adding
    if request.GET.get('UCLetter'):                 #each option the user selected
        characters.extend(list(capitals))
    if request.GET.get('SpecChar'):
        characters.extend(list(symbols))    
    for x in range(length):
        thepassword += random.choice(characters)      
    return render(request, 'generator/passgen.html',{'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')