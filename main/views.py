from django.shortcuts import render

def home(request):
    latitude = 11.987649978084008
    longitude = 8.419178940425969
    
    context = {
        'latitude': latitude,
        'longitude': longitude
    }
    
    return render(request, 'index.html', context)
