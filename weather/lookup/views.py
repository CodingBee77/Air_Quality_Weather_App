from django.shortcuts import render
import requests
import json
from django.conf import settings

def get_category(api):
    category_description = ""
    category_color = ""
    if api['current']['indexes'][0]['level'] == "VERY_LOW":
        category_description = "(0 - 20) - Very low air pollution"
        category_color = "very_low"
    elif api['current']['indexes'][0]['level'] == "LOW":
        category_description = "( 20-50 ) - Low air pollution"
        category_color = "low"
    elif api['current']['indexes'][0]['level'] == "MEDIUM":
        category_description = "( 50-70 ) - Medium air pollution"
        category_color = "medium"
    elif api['current']['indexes'][0]['level'] == "HIGH":
        category_description = "( 70-90 ) - High air pollution"
        category_color = "high"
    elif api['current']['indexes'][0]['level'] == "VERY_HIGH":
        category_description = "( 90-100 ) - Very high air pollution"
        category_color = "very_high"
    elif api['current']['indexes'][0]['level'] == "EXTREME":
        category_description = "( 100-130 ) - Extremely high air pollution"
        category_color = "extreme"
    elif api['current']['indexes'][0]['level'] == "AIRMAGGEDON":
        category_description = "(>130) - Dangerous air pollution"
        category_color = "airmaggedon"

    return category_description, category_color


def get_installation(lat, long):
    api_request = requests.get(
        "https://airapi.airly.eu/v2/installations/nearest?lat=" + lat + "&lng=" + long + "&maxDistanceKM=2&maxResults=1",
        headers={'apikey': settings.AIRLY_API_KEY})

    city = ""
    latitude = ""
    longitude = ""

    try:
        api = json.loads(api_request.content)
        latitude = str(api[0]['location']['latitude'])
        longitude = str(api[0]['location']['longitude'])
        city = api[0]['address']['city']


    except Exception as e:
        api = "Error..."


    return city, latitude, longitude


def get_measurements(lat, long):
    api_request = requests.get(
        "https://airapi.airly.eu/v2/measurements/nearest?lat=" + lat + "&lng=" +
        long + "&maxDistanceKM=2",
        headers={'apikey': settings.AIRLY_API_KEY})

    api = ""
    try:
        api = json.loads(api_request.content)


    except Exception as e:
        api = "Error..."

    return api


def render_for_coordinates(request, lat, long):
    city, latitude, longitude = get_installation(lat, long)
    measurements = get_measurements(latitude, longitude)

    category_description, category_color = get_category(measurements)

    return render(request, 'home.html', {'api': measurements, 'category_description': category_description,
                                         'category_color': category_color, 'city': city})


def home(request):
    if request.method == "POST":
        coordinates = request.POST['coordinates']
        return render_for_coordinates(request, coordinates.split(',')[0], coordinates.split(',')[1])

    else:
        return render_for_coordinates(request, "50.062006", "19.940984")


def about(request):
    return render(request, 'about.html', {})
