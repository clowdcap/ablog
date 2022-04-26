import folium
from geopy.geocoders import Nominatim
import pandas as pd

mapa = folium.Map(
    zoom_start=14,
    location=[-25.371781,-49.4141514],
    control_scale=True)

ler = pd.read_excel('./tables/locais.xlsx')
ler.drop_duplicates(inplace=True)

locator = Nominatim(user_agent="myGeocoder")
location = locator.geocode(ler['ENDERECO'])

for index, linha in ler.iterrows():
    float(linha['LAT'])
    float(linha['LON'])
    folium.Marker([linha['LAT'], linha["LON"]],
                  popup=f"""Protocolo: {linha["PROTOCOLO"]}\n\n\n{linha["RUA"]} """).add_to(mapa)

mapa.save("templates/folium.html")
