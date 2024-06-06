from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):

    # dest1 = Destination()
    # dest1.name = 'Mumbai'
    # dest1.desc = 'The City Never Sleeps'
    # dest1.img = 'destination_1.jpg'
    # dest1.price = 700
    # dest1.offer = False

    # dest2 = Destination()
    # dest2.name = 'Hyderabad'
    # dest2.desc = 'First Biryani Then Shervani'
    # dest2.img = 'destination_2.jpg'
    # dest2.price = 650
    # dest2.offer = True
    # dests = [dest1, dest2, dest3]

    dests = Destination.objects.all()
   


    return render(request, 'index.html',{ 'dests': dests}) 

