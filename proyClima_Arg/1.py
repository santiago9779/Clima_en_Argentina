import requests, pandas as pd
from io import StringIO  # Esto es para cargar los datos desde una cadena

url ='https://apis.datos.gob.ar/georef/api/provincias.json'

response = requests.get(url)

print(response.status_code)

# Datos JSON
data = {
    "cantidad": 24,
    "inicio": 0,
    "parametros": {},
    "provincias": [
        {"centroide":{"lat":-26.8753965086829,"lon":-54.6516966230371},"id":"54","nombre":"Misiones"},{"centroide":{"lat":-33.7577257449137,"lon":-66.0281298195836},"id":"74","nombre":"San Luis"},{"centroide":{"lat":-30.8653679979618,"lon":-68.8894908486844},"id":"70","nombre":"San Juan"},{"centroide":{"lat":-32.0588735436448,"lon":-59.2014475514635},"id":"30","nombre":"Entre Ríos"},{"centroide":{"lat":-48.8154851827063,"lon":-69.9557621671973},"id":"78","nombre":"Santa Cruz"},{"centroide":{"lat":-40.4057957178801,"lon":-67.229329893694},"id":"62","nombre":"Río Negro"},{"centroide":{"lat":-43.7886233529878,"lon":-68.5267593943345},"id":"26","nombre":"Chubut"},{"centroide":{"lat":-32.142932663607,"lon":-63.8017532741662},"id":"14","nombre":"Córdoba"},{"centroide":{"lat":-34.6298873058957,"lon":-68.5831228183798},"id":"50","nombre":"Mendoza"},{"centroide":{"lat":-29.685776298315,"lon":-67.1817359694432},"id":"46","nombre":"La Rioja"},{"centroide":{"lat":-27.3358332810217,"lon":-66.9476824299928},"id":"10","nombre":"Catamarca"},{"centroide":{"lat":-37.1315537735949,"lon":-65.4466546606951},"id":"42","nombre":"La Pampa"},{"centroide":{"lat":-27.7824116550944,"lon":-63.2523866568588},"id":"86","nombre":"Santiago del Estero"},{"centroide":{"lat":-28.7743047046407,"lon":-57.8012191977913},"id":"18","nombre":"Corrientes"},{"centroide":{"lat":-30.7069271588117,"lon":-60.9498369430241},"id":"82","nombre":"Santa Fe"},{"centroide":{"lat":-26.9478001830786,"lon":-65.3647579441481},"id":"90","nombre":"Tucumán"},{"centroide":{"lat":-38.6417575824599,"lon":-70.1185705180601},"id":"58","nombre":"Neuquén"},{"centroide":{"lat":-24.2991344492002,"lon":-64.8144629600627},"id":"66","nombre":"Salta"},{"centroide":{"lat":-26.3864309061226,"lon":-60.7658307438603},"id":"22","nombre":"Chaco"},{"centroide":{"lat":-24.894972594871,"lon":-59.9324405800872},"id":"34","nombre":"Formosa"},{"centroide":{"lat":-23.3200784211351,"lon":-65.7642522180337},"id":"38","nombre":"Jujuy"},{"centroide":{"lat":-34.6144934119689,"lon":-58.4458563545429},"id":"02","nombre":"Ciudad Autónoma de Buenos Aires"},{"centroide":{"lat":-36.6769415180527,"lon":-60.5588319815719},"id":"06","nombre":"Buenos Aires"},{"centroide":{"lat":-82.52151781221,"lon":-50.7427486049785},"id":"94","nombre":"Tierra del Fuego, Antártida e Islas del Atlántico Sur"}
    ],
    "total": 24
}

# Extrae la lista de provincias del JSON
provincias = data["provincias"]

# Crea el DataFrame a partir de la lista de provincias
df = pd.DataFrame(provincias)

# Datos de población
poblacion = {
    "Buenos Aires": 17569053,
    "Córdoba": 3978984,
    "Santa Fe": 3556522,
    "Ciudad de Buenos Aires": 3120612,
    "Mendoza": 2014533,
    "Tucumán": 1703186,
    "Salta": 1440672,
    "Entre Ríos": 1426426,
    "Misiones": 1280960,
    "Corrientes": 1197553,
    "Chaco": 1142963,
    "Santiago del Estero": 1054028,
    "San Juan": 818234,
    "Jujuy": 797955,
    "Río Negro": 762067,
    "Nequén": 726590,
    "Formosa": 606041,
    "Chubut": 603120,
    "San Luis": 540905,
    "Catamarca": 429556,
    "La Rioja": 384607,
    "La Pampa": 366022,
    "Santa Cruz": 333473,
    "Tierra del Fuego, Antártida e Islas del Atlántico Sur": 190641
}

# Datos de las provincias y sus superficies
provincias_superficie = {
    "Ciudad Autónoma de Buenos Aires": 205.9,
    "Buenos Aires": 305907.4,
    "Catamarca": 101486.1,
    "Chaco": 99763.3,
    "Chubut": 224302.3,
    "Córdoba": 164707.8,
    "Corrientes": 89123.3,
    "Entre Ríos": 78383.7,
    "Formosa": 75488.3,
    "Jujuy": 53244.2,
    "La Pampa": 143492.5,
    "La Rioja": 91493.7,
    "Mendoza": 149069.2,
    "Misiones": 29911.4,
    "Neuquén": 94422.0,
    "Río Negro": 202168.6,
    "Salta": 155340.5,
    "San Juan": 88296.2,
    "San Luis": 75347.1,
    "Santa Cruz": 244457.5,
    "Santa Fe": 133249.1,
    "Santiago del Estero": 136934.3,
    "Tierra del Fuego, Antártida e Islas del Atlántico Sur": 910324.4,
    "Tucumán": 22592.1
}

# Agregar población manualmente a Neuquén y Ciudad Autónoma de Buenos Aires
poblacion_manual = {
    "Neuquén": 600005,  
    "Ciudad Autónoma de Buenos Aires": 3205000  
}
#no logro agregar valores..

# Actualizar el DataFrame con los valores de población manual
df['poblacion'] = df['nombre'].map(poblacion_manual)

# Muestra el DataFrame actualizado
print(df)

#agregar superfice a DF
df['prov_superf'] = df['nombre'].map(provincias_superficie)

# Agregar la población al DataFrame
df['poblacion'] = df['nombre'].map(poblacion)

#agregms data para el clima
clima_data = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septimbre','Octubre','Noviembre','Diciembre'],
    "Buenos Aires": [28, 27, 25, 21, 18, 15, 14, 16, 18, 21, 24, 27],
    "San Miguel de Tucumán": [31, 30, 28, 25, 22, 19, 20, 23, 26, 29, 30, 31],
    "Ciudad de Mendoza": [31, 30, 27, 22, 18, 15, 15, 17, 21, 25, 28, 31],
    "Ushuaia": [13, 13, 11, 8, 6, 4, 4, 5, 7, 9, 11, 12],
}

# Crear un DataFrame a partir de los datos climáticos
df_clima = pd.DataFrame(clima_data)

# df = pd.concat([df, df_clima], axis=1)

# Guarda el DataFrame en un archivo CSV
df.to_excel('provincias.xlsx', index=False)
# df_clima.to_csv('clima.csv', index=False)


# Tu código para crear el DataFrame que deseas agregar como otra hoja

# Cargar el archivo 'provincias.csv'
with pd.ExcelWriter('provincias.xlsx', engine='openpyxl', mode='a') as writer:
    # Guardar el nuevo DataFrame en una nueva hoja (se creará una nueva hoja)
    df_clima.to_excel(writer, sheet_name='DatosClima', index=False)


# Muestra el DataFrame resultante
print(df)










# # Verificar si hay valores nulos en el DataFrame
# valores_nulos = df.isnull().any()

# # Mostrar las columnas con valores nulos
# columnas_con_nulos = valores_nulos[valores_nulos].index

# # Mostrar los resultados
# if len(columnas_con_nulos) > 0:
#     print("Columnas con valores nulos:")
#     for columna in columnas_con_nulos:
#         print(columna)
# else:
#     print("No hay valores nulos en el DataFrame")