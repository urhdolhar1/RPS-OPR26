"https://open-meteo.com/en/docs"
import requests 

def trenutna_temp(lat,lon):
    base_url= f"https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m"
    call= requests.get(base_url).json()
    print(call["current"]["temperature_2m"])


trenutna_temp(45.12, 14.5)