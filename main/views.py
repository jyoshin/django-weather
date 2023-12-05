from django.shortcuts import render
import requests
import datetime

def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Almaty'

    appid = 'a440dfb0ec7bcc037444b8dfef4afa4c'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q':city,'appid':appid, 'units':'metric'}

    r = requests.get(url=URL, params=PARAMS)

    res = r.json()
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']

    day = datetime.date.today()

    return render(request, 'base/base.html', {'description':description, 'icon':icon, 'temp':temp, 'day':day, 'city':city})

