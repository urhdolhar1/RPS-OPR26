"https://open-meteo.com/en/docs"
import requests 
mesta= [{"name":"Ljubljana","lat":46.051,"lng":14.505},
  {"name":"Maribor","lat":46.556,"lng":15.646},
  {"name":"Kranj","lat":46.239,"lng":14.356},
  {"name":"Celje","lat":46.231,"lng":15.260},
  {"name":"Koper","lat":45.548,"lng":13.730},
  {"name":"Velenje","lat":46.357,"lng":15.113},
  {"name":"Novo Mesto","lat":45.804,"lng":15.169},
  {"name":"Ptuj","lat":46.420,"lng":15.870},
  {"name":"Kamnik","lat":46.226,"lng":14.612},
  {"name":"Jesenice","lat":46.432,"lng":14.062}]

def trenutna_temp(lat,lon):
    base_url= f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m"
    call= requests.get(base_url).json()
    print(call["current"]["temperature_2m"])

    
    for mesto in mesta:
        mesto_vnos= input("vnesi mesto:")
        if mesto["name"].lower() == mesto_vnos.lower():
            trenutna_temp(mesto["lat"], mesto["lng"])
            break
        else:
            print("Mesto ni na seznamu.")

