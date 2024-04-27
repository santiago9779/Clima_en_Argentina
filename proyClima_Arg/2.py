import requests, pandas as pd, json

url = "https://apis.datos.gob.ar/georef/api/provincias"
response = requests.get(url)
rtext = response.text

#Para formato json

rjson = response.json()
# print(rtext)

#Guardar data en DF

df = pd.DataFrame(rjson)