import requests
from pprint import pprint
import html
 
vpr = int(input("Koliko vprašanj želiš? "))
url = f"https://opentdb.com/api.php?amount={vpr}&type=multiple"
klic = requests.get(url).json()
 
vprasanja = klic["results"]
 
for v in vprasanja:10
    print("-"*80)
    pprint(v)
    print("-"*80)
 
    print(html.unescape(v["question"]))  #odstrani HTML znake
    print(v["correct_answer"])
    print(v["incorrect_answers"])
 
prav = "A"
odgovori = ["A", "B", "C", "D"] #random.shuffle(list)
for i, o in enumerate(odgovori):
    print(f"{i+1} - {o}")
odgovor = int(input("Odgovor: "))
print(prav == odgovori[odgovor-1]) # -1