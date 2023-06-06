from django.shortcuts import render

def home(request):
    latitude = 11.977501252244648
    longitude = 8.420809723501117
   
    context = {
        'latitude': latitude,
        'longitude': longitude
    }
    
    return render(request, 'index.html', context)
