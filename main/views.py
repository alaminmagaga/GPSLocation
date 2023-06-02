from django.shortcuts import render
import firebase_admin
from firebase_admin import db, credentials

# Set the Firebase service account credentials
cred = credentials.Certificate('static/esp-firebase-demo.json')
# Initialize the app with the credentials and the database URL
firebase_admin.initialize_app(cred, options={
    'databaseURL': 'https://esp-firebase-demo-f3d33-default-rtdb.firebaseio.com/'
})

def home(request):
    # Reference to the GPS location data in the database
    gps_ref = db.reference('UsersData/uJaTyhyuAaTGk4yTgigMjO05OH43/readings')
    
    # Get the latest GPS location data
    latest_reading = gps_ref.order_by_key().limit_to_last(1).get()
    
    # Extract latitude, longitude, and timestamp from the latest reading
    latitude = list(latest_reading.values())[0].get('latitude')
    longitude = list(latest_reading.values())[0].get('longitude')
    timestamp = list(latest_reading.keys())[0]
    
    # Pass the data to the template
    context = {
        'latitude': latitude,
        'longitude': longitude,
        'timestamp': timestamp
    }
    
    return render(request, 'index.html', context)
