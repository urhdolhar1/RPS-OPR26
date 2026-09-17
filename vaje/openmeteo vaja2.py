"https://open-meteo.com/en/docs"
import requests 
#VAJA1
#Izpiši trenutno temperaturo.
#Izpiši temperature za naslednjih 7 dni.
#Ugotovi, kateri dan bo najtoplejši oz. najhladnejši, in izpiši datum ter temperaturo.
#Ugotovi, kateri dan ima največjo razliko med dnevno in nočno temperaturo.

mesta_knj= {"Ljubljana": {"lat":46.051,"lng":14.505},
    "Maribor": {"lat":46.556,"lng":15.646},
    "Kranj": {"lat":46.239,"lng":14.356},
    "Celje": {"lat":46.231,"lng":15.260},
    "Koper": {"lat":45.548,"lng":13.730},
    "Velenje": {"lat":46.357,"lng":15.113},
    "Novo Mesto": {"lat":45.804,"lng":15.169},
    "Ptuj": {"lat":46.420,"lng":15.870},
    "Kamnik": {"lat":46.226,"lng":14.612},
    "Jesenice": {"lat":46.432,"lng":14.062}
}

vnos= input("mesto:")
if vnos in mesta_knj:
    lat = mesta_knj[vnos]["lat"]
    lng = mesta_knj[vnos]["lng"]

source= f"https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&daily=temperature_2m_max,temperature_2m_min&current=temperature_2m&timezone=auto"

base_url= "https://api.open-meteo.com/v1/forecast"
params= {"latitude" : lat,
         "longitude" : lng,
         "daily" : ["temperature_2m_max","temperature_2m_min"],
         "current" : "temperature_2m",
         "timezone" : "auto" }

call = requests.get(base_url, params=params)
response = call.json()

daily_temp= response["daily"]["temperature_2m_max"]
datum= response["daily"]["time"]

#Izpiši trenutno temperaturo.
print("trenutna:",response["current"]["temperature_2m"])

#Izpiši temperature za naslednjih 7 dni.
print("--- Napoved za 7 dni ---")
for i in range(7):
    print(f"{datum[i]}: {daily_temp[i]} °C")

#Ugotovi, kateri dan bo najtoplejši oz. najhladnejši, in izpiši datum ter temperaturo.

topli= response["daily"]["temperature_2m_max"]
hladni= response["daily"]["temperature_2m_min"]
datum= datum

najtoplejsi= max(topli)
najhladnejsi= min(hladni)


najtoplejsi_indeks = topli.index(max(topli))
najtoplejsi_datum = datum[najtoplejsi_indeks]
najtoplejsa_temp = topli[najtoplejsi_indeks]

print(f"Najtoplejši dan: {najtoplejsi_datum}, temperatura: {najtoplejsa_temp} °C")


najhladnejsi_indeks = hladni.index(min(hladni))
najhladnejsi_datum = datum[najhladnejsi_indeks]
najhladnejsa_temp = hladni[najhladnejsi_indeks]

print(f"Najhladnejši dan: {najhladnejsi_datum}, temperatura: {najhladnejsa_temp} °C")

#Ugotovi, kateri dan ima največjo razliko med dnevno in nočno temperaturo.




#Med 10 največjimi slovenskimi mesti poišči tisto;
#ki bo danes najtoplejše oz. najhladnejše,
#ki bo imelo najmanj oz. največ dežja,
#ki bo imelo najmanj oz. največ vetra.