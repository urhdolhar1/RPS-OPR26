import requests
imena= ["Bine", "Luka"]
url= f"https://api.agify.io?name={imena}"

call = requests.get(url)
response = call.json()
#ugotovi katero ime je najstarejše
for i in imena: