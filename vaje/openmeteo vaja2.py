"https://open-meteo.com/en/docs"
import requests 
mesta_knj= {"Ljubljana": {lat":46.051,"lng":14.505},
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

    for mesto in mesta:
        vnos= input("mesto:")
        if vnos in mesta:
            print(mesta_knj)

