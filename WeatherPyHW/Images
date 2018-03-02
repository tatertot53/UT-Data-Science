
Observations
Analysis of this random dataset of 500 cities and countries reveals a few details about how weather is affected as it relates to latitude and ultimately, distance from the equator. 
Clearly, max temperature is almost directly affected by distance from the equator. One factor not directly revealed by the data gathered in this observation is the slight skew of temperature to one hemisphere of the globe. This can be inferred as having to do with the tilt of the earth on its axis, generating more warmth on one hemisphere as compared to the other. In this case, the southern hemisphere is definitely showing warmer maximum temperatures, indicating the earth is tilted so the northern hemisphere is further from the sun.
Cloud cover has almost no relationship to distance from the equator, as the data show a randomly distributed scatterplot. This indicates a low correlation between the two factors. Wind speed is not directly affected by latitudinal position. Both comparisons in this respect do provide clear pictures of where a majority of the cities in the world sit on average and frequency in terms of wind speed and cloud cover.
Humidity also does not show a great deal of correlation as it relates to latitude. Because humidity is often strongly associated with distance from large bodies of water, and that the earth is over 70% water, it makes sense that the data skews to the higher end of the scale here.
Overall, geography as it relates to latitude does have an affect on the local weather, however given the small sample size in terms of time, the only clear direct relationship that can be inferred, in my opinion, are that temperature extremes depend a great deal on a city’s distance from the equator.


DEPENDENCIES


```python
import json
import pandas as pd
import requests as req
import random
from citipy import citipy
import seaborn as sns
import csv
import numpy as np
import time
from datetime import datetime
import matplotlib.pyplot as plt
sns.set(style="darkgrid", color_codes=True)
```

CONFIG VARIABLES


```python
api_key = "d3cfde203de9c80b7b1bab1e8e60ab91"
url = "http://api.openweathermap.org/data/2.5/weather?"
units = "Imperial"
```

GENERATING RANDOM LATITUDE AND LONGITUDE DATA


```python
location = pd.DataFrame()
location['lat'] = pd.unique([np.random.uniform(-90,90) for x in range(1000)])
location['lon'] = pd.unique([np.random.uniform(-180, 180) for x in range(1000)])

location.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>lat</th>
      <th>lon</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>53.995415</td>
      <td>136.910796</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.827802</td>
      <td>100.131317</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-44.709328</td>
      <td>86.839330</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-4.456784</td>
      <td>95.307876</td>
    </tr>
    <tr>
      <th>4</th>
      <td>55.583738</td>
      <td>95.400485</td>
    </tr>
  </tbody>
</table>
</div>



ASSIGNING LAT AND LON TO CITY & COUNTRY ID WITH CITIPY


```python
location['city'] = ""
location['country'] = ""

count = 0
for index, row in location.iterrows():
    city = citipy.nearest_city(row['lat'], row['lon']).city_name
    country = citipy.nearest_city(row['lat'], row['lon']).country_code
    location.set_value(index,"city",city)
    location.set_value(index,"country",country)
location.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>lat</th>
      <th>lon</th>
      <th>city</th>
      <th>country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>53.995415</td>
      <td>136.910796</td>
      <td>imeni poliny osipenko</td>
      <td>ru</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.827802</td>
      <td>100.131317</td>
      <td>rantauprapat</td>
      <td>id</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-44.709328</td>
      <td>86.839330</td>
      <td>busselton</td>
      <td>au</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-4.456784</td>
      <td>95.307876</td>
      <td>padang</td>
      <td>id</td>
    </tr>
    <tr>
      <th>4</th>
      <td>55.583738</td>
      <td>95.400485</td>
      <td>irbeyskoye</td>
      <td>ru</td>
    </tr>
  </tbody>
</table>
</div>




```python
len(location)
```




    1000



CREATING LISTS


```python
location['Max Temp'] = ""
location['Humidity'] = ""
location['Cloudiness'] = ""
location['Wind Speed'] = ""
location["Date"] = ""
location["ID"] = ""
```


```python
location_clean = location.dropna()
location_clean = location.sample(n=500)
len(location_clean)
```




    500



API LOOP & OUTPUT


```python
api_call_count = 0

for index, row in location_clean.iterrows():
    city = row["city"]
    country = row["country"]
    query = url + "appid=" + api_key + "&units=" + units + "&q=" + city 
    

    try:
        response = req.get(query).json()
        latitude = response["coord"]["lat"]
        longitude = response["coord"]["lon"]
        date = response["dt"]
        temp = response["main"]["temp_max"]
        humid = response["main"]["humidity"]
        cloud = response["clouds"]["all"]
        wind = response["wind"]["speed"]
        city_number = response["id"]
        location_clean.set_value(index,"Max Temp",temp)
        location_clean.set_value(index,"Cloudiness",cloud)
        location_clean.set_value(index,"Latitude",latitude)
        location_clean.set_value(index,"Longitude",longitude)
        location_clean.set_value(index,"Date",date)
        location_clean.set_value(index,"ID",city_number)
        location_clean.set_value(index,"Humidity",humid)
        location_clean.set_value(index,"Wind Speed",wind)
        print("Data Gathered for %s, %s, %s" % (city_number,city,query))
    except KeyError:
        print("Not Enough Info for %s, %s" % (city, country))
    api_call_count += 1
    if api_call_count % 50 == 0:
        time.sleep(60)

```

    Data Gathered for 934322, mahebourg, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=mahebourg
    Data Gathered for 1113217, zabol, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=zabol
    Data Gathered for 3347019, namibe, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=namibe
    Data Gathered for 4020109, atuona, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=atuona
    Not Enough Info for vaitupu, wf
    Data Gathered for 3874787, punta arenas, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=punta arenas
    Data Gathered for 5606187, saint anthony, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=saint anthony
    Data Gathered for 3833367, ushuaia, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ushuaia
    Data Gathered for 2610343, vestmanna, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=vestmanna
    Data Gathered for 1651810, airai, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=airai
    Data Gathered for 4696310, harper, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=harper
    Data Gathered for 1715015, dicabisagan, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=dicabisagan
    Data Gathered for 1106677, bambous virieux, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=bambous virieux
    Data Gathered for 1688687, san quintin, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=san quintin
    Data Gathered for 2110227, butaritari, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=butaritari
    Data Gathered for 481548, troitsko-pechorsk, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=troitsko-pechorsk
    Data Gathered for 962367, richards bay, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=richards bay
    Not Enough Info for olafsvik, is
    Data Gathered for 1633419, padang, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=padang
    Data Gathered for 3366880, hermanus, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=hermanus
    Data Gathered for 2022129, kichera, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=kichera
    Data Gathered for 2156643, mount gambier, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=mount gambier
    Not Enough Info for saleaula, ws
    Data Gathered for 2075265, busselton, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=busselton
    Data Gathered for 6540432, cervia, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=cervia
    Data Gathered for 3357804, eenhana, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=eenhana
    Data Gathered for 4030556, rikitea, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=rikitea
    Data Gathered for 4944903, nantucket, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=nantucket
    Data Gathered for 6089245, norman wells, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=norman wells
    Data Gathered for 3631878, moron, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=moron
    Not Enough Info for olafsvik, is
    Data Gathered for 4020109, atuona, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=atuona
    Data Gathered for 1168312, pasni, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=pasni
    Data Gathered for 3397763, jacareacanga, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=jacareacanga
    Data Gathered for 962367, richards bay, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=richards bay
    Data Gathered for 3374210, sao filipe, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=sao filipe
    Data Gathered for 4030556, rikitea, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=rikitea
    Not Enough Info for belushya guba, ru
    Data Gathered for 3874787, punta arenas, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=punta arenas
    Data Gathered for 1015776, bredasdorp, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=bredasdorp
    Data Gathered for 3833367, ushuaia, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ushuaia
    Data Gathered for 2396518, port-gentil, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=port-gentil
    Data Gathered for 5880568, bethel, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=bethel
    Data Gathered for 3514843, vega de alatorre, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=vega de alatorre
    Data Gathered for 3874787, punta arenas, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=punta arenas
    Data Gathered for 2122493, omsukchan, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=omsukchan
    Data Gathered for 1014034, carnarvon, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=carnarvon
    Data Gathered for 4021858, guerrero negro, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=guerrero negro
    Data Gathered for 1282256, hithadhoo, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=hithadhoo
    Data Gathered for 3833859, tres arroyos, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=tres arroyos
    Data Gathered for 3355672, luderitz, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=luderitz
    Data Gathered for 6255012, flinders, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=flinders
    Data Gathered for 7626384, hovd, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=hovd
    Data Gathered for 3372707, ribeira grande, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ribeira grande
    Data Gathered for 3514843, vega de alatorre, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=vega de alatorre
    Data Gathered for 2618795, klaksvik, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=klaksvik
    Data Gathered for 2023584, imeni poliny osipenko, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=imeni poliny osipenko
    Data Gathered for 3652462, san cristobal, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=san cristobal
    Data Gathered for 2075265, busselton, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=busselton
    Data Gathered for 2022572, khatanga, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=khatanga
    Data Gathered for 3137469, sorland, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=sorland
    Data Gathered for 3526756, isla mujeres, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=isla mujeres
    Data Gathered for 1056151, mananjary, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=mananjary
    Data Gathered for 3616584, san ramon, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=san ramon
    Data Gathered for 1788852, xining, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=xining
    Data Gathered for 1106677, bambous virieux, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=bambous virieux
    Data Gathered for 2612500, stovring, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=stovring
    Data Gathered for 4030556, rikitea, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=rikitea
    Data Gathered for 2013865, ust-uda, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ust-uda
    Data Gathered for 1852357, shimoda, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=shimoda
    Data Gathered for 3391220, presidente dutra, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=presidente dutra
    Data Gathered for 3026644, souillac, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=souillac
    Data Gathered for 2025256, chumikan, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=chumikan
    Data Gathered for 2450173, taoudenni, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=taoudenni
    Data Gathered for 2122605, okhotsk, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=okhotsk
    Data Gathered for 1791636, weinan, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=weinan
    Not Enough Info for grand river south east, mu
    Not Enough Info for mys shmidta, ru
    Data Gathered for 1861280, itoman, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=itoman
    Data Gathered for 2377457, nouadhibou, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=nouadhibou
    Data Gathered for 1733782, victoria, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=victoria
    Data Gathered for 5960603, geraldton, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=geraldton
    Data Gathered for 5855927, hilo, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=hilo
    Data Gathered for 1805733, jinchang, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=jinchang
    Data Gathered for 3833367, ushuaia, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ushuaia
    Data Gathered for 2189343, kaeo, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=kaeo
    Data Gathered for 162627, yabrud, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=yabrud
    Data Gathered for 2013459, verkh-usugli, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=verkh-usugli
    Data Gathered for 4020109, atuona, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=atuona
    Data Gathered for 6201424, mataura, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=mataura
    Data Gathered for 4030556, rikitea, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=rikitea
    Data Gathered for 1490256, talnakh, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=talnakh
    Data Gathered for 3833367, ushuaia, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ushuaia
    Data Gathered for 3374210, sao filipe, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=sao filipe
    Not Enough Info for barentsburg, sj
    Data Gathered for 3838859, rio gallegos, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=rio gallegos
    Data Gathered for 3833367, ushuaia, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ushuaia
    Data Gathered for 3833367, ushuaia, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ushuaia
    Data Gathered for 2075265, busselton, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=busselton
    Data Gathered for 3369157, cape town, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=cape town
    Data Gathered for 3833367, ushuaia, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ushuaia
    Data Gathered for 3985710, cabo san lucas, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=cabo san lucas
    Data Gathered for 6185377, yellowknife, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=yellowknife
    Data Gathered for 5106834, albany, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=albany
    Data Gathered for 5848280, kapaa, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=kapaa
    Data Gathered for 3685702, cravo norte, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=cravo norte
    Not Enough Info for halalo, wf
    Data Gathered for 362973, abnub, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=abnub
    Data Gathered for 217834, bukama, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=bukama
    Data Gathered for 2123814, leningradskiy, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=leningradskiy
    Data Gathered for 2027487, arkhara, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=arkhara
    Data Gathered for 1688687, san quintin, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=san quintin
    Data Gathered for 5915327, cap-aux-meules, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=cap-aux-meules
    Data Gathered for 3863379, mar del plata, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=mar del plata
    Data Gathered for 3652764, puerto ayora, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=puerto ayora
    Data Gathered for 4275070, marion, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=marion
    Data Gathered for 371745, kutum, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=kutum
    Data Gathered for 2163355, hobart, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=hobart
    Data Gathered for 4030556, rikitea, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=rikitea
    Data Gathered for 3833367, ushuaia, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ushuaia
    Data Gathered for 6201424, mataura, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=mataura
    Data Gathered for 2171465, clarence town, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=clarence town
    Data Gathered for 3453439, ponta do sol, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ponta do sol
    Data Gathered for 2023333, kachug, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=kachug
    Data Gathered for 3833367, ushuaia, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ushuaia
    Data Gathered for 2069194, jamestown, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=jamestown
    Data Gathered for 1507390, dikson, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=dikson
    Data Gathered for 3920736, chimore, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=chimore
    Data Gathered for 4501427, port elizabeth, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=port elizabeth
    Data Gathered for 3382160, cayenne, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=cayenne
    Data Gathered for 2175403, bluff, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=bluff
    Data Gathered for 157429, kilindoni, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=kilindoni
    Data Gathered for 5972291, havre-saint-pierre, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=havre-saint-pierre
    Data Gathered for 3386213, touros, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=touros
    Data Gathered for 2069194, jamestown, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=jamestown
    Data Gathered for 3688689, villa maria, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=villa maria
    Data Gathered for 5779548, payson, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=payson
    Data Gathered for 2110227, butaritari, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=butaritari
    Data Gathered for 3418910, upernavik, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=upernavik
    Data Gathered for 2018214, ovsyanka, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ovsyanka
    Not Enough Info for mys shmidta, ru
    Data Gathered for 3652764, puerto ayora, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=puerto ayora
    Data Gathered for 3985710, cabo san lucas, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=cabo san lucas
    Data Gathered for 777682, skjervoy, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=skjervoy
    Data Gathered for 1152377, lat yao, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=lat yao
    Data Gathered for 4267710, sitka, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=sitka
    Data Gathered for 4036284, alofi, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=alofi
    Data Gathered for 964432, port alfred, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=port alfred
    Data Gathered for 3351014, camacupa, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=camacupa
    Data Gathered for 7671223, kloulklubed, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=kloulklubed
    Data Gathered for 6201424, mataura, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=mataura
    Data Gathered for 2517679, fortuna, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=fortuna
    Data Gathered for 1252783, yarada, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=yarada
    Data Gathered for 338554, dubti, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=dubti
    Data Gathered for 4035715, avarua, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=avarua
    Data Gathered for 2873499, mariental, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=mariental
    Not Enough Info for deh rawud, af
    Data Gathered for 1271891, fazilka, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=fazilka
    Data Gathered for 4020109, atuona, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=atuona
    Data Gathered for 1273574, vaini, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=vaini
    Data Gathered for 964432, port alfred, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=port alfred
    Data Gathered for 2075265, busselton, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=busselton
    Data Gathered for 1282256, hithadhoo, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=hithadhoo
    Data Gathered for 4020109, atuona, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=atuona
    Data Gathered for 1106677, bambous virieux, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=bambous virieux
    Data Gathered for 3833367, ushuaia, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ushuaia
    Data Gathered for 3867427, mayor pablo lagerenza, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=mayor pablo lagerenza
    Data Gathered for 344979, lebu, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=lebu
    Data Gathered for 4557109, chambersburg, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=chambersburg
    Data Gathered for 3191648, zlobin, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=zlobin
    Data Gathered for 2729907, longyearbyen, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=longyearbyen
    Data Gathered for 4267710, sitka, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=sitka
    Data Gathered for 4470244, havelock, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=havelock
    Data Gathered for 2175403, bluff, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=bluff
    Data Gathered for 3833859, barrow, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=barrow
    Data Gathered for 1733782, victoria, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=victoria
    Data Gathered for 3372707, ribeira grande, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ribeira grande
    Data Gathered for 3521972, panaba, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=panaba
    Data Gathered for 2155415, new norfolk, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=new norfolk
    Not Enough Info for fatikchhari, bd
    Data Gathered for 3874787, punta arenas, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=punta arenas
    Data Gathered for 4372777, vardo, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=vardo
    Data Gathered for 1006984, east london, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=east london
    Data Gathered for 1507390, dikson, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=dikson
    Not Enough Info for meyungs, pw
    Data Gathered for 1576303, lao cai, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=lao cai
    Data Gathered for 3030057, brignoles, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=brignoles
    Data Gathered for 3421765, nanortalik, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=nanortalik
    Data Gathered for 5848280, kapaa, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=kapaa
    Data Gathered for 146639, lasa, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=lasa
    Data Gathered for 2022572, khatanga, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=khatanga
    Data Gathered for 3833367, ushuaia, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ushuaia
    Data Gathered for 2075265, busselton, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=busselton
    Data Gathered for 2737599, saldanha, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=saldanha
    Data Gathered for 3874787, punta arenas, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=punta arenas
    Data Gathered for 3567869, banes, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=banes
    Data Gathered for 3421719, narsaq, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=narsaq
    Data Gathered for 6173361, vanderhoof, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=vanderhoof
    Data Gathered for 2175403, bluff, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=bluff
    Data Gathered for 990930, kimberley, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=kimberley
    Data Gathered for 1337612, dhidhdhoo, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=dhidhdhoo
    Data Gathered for 5106834, albany, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=albany
    Data Gathered for 5301067, kingman, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=kingman
    Data Gathered for 2075265, busselton, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=busselton
    Not Enough Info for lolua, tv
    Data Gathered for 3833367, ushuaia, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ushuaia
    Data Gathered for 515175, oparino, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=oparino
    Data Gathered for 2180815, tuatapere, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=tuatapere
    Not Enough Info for nizhneyansk, ru
    Data Gathered for 866062, iskateley, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=iskateley
    Data Gathered for 2122783, nogliki, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=nogliki
    Data Gathered for 3369157, cape town, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=cape town
    Data Gathered for 1688696, san policarpo, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=san policarpo
    Data Gathered for 2163355, hobart, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=hobart
    Data Gathered for 6078372, moose factory, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=moose factory
    Data Gathered for 3874787, punta arenas, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=punta arenas
    Data Gathered for 3985710, cabo san lucas, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=cabo san lucas
    Data Gathered for 2344082, george, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=george
    Data Gathered for 5855927, hilo, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=hilo
    Data Gathered for 2092164, lorengau, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=lorengau
    Not Enough Info for tsihombe, mg
    Data Gathered for 3378644, georgetown, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=georgetown
    Data Gathered for 3420768, qasigiannguit, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=qasigiannguit
    Data Gathered for 3355624, maltahohe, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=maltahohe
    Data Gathered for 3356343, karasburg, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=karasburg
    Data Gathered for 2075265, busselton, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=busselton
    Not Enough Info for bairiki, ki
    Data Gathered for 3369157, cape town, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=cape town
    Data Gathered for 2126710, beringovskiy, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=beringovskiy
    Data Gathered for 3105522, bereda, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=bereda
    Data Gathered for 2077895, alice springs, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=alice springs
    Data Gathered for 2121025, srednekolymsk, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=srednekolymsk
    Data Gathered for 2136825, isangel, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=isangel
    Data Gathered for 5106834, albany, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=albany
    Data Gathered for 2136825, isangel, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=isangel
    Data Gathered for 3833367, ushuaia, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ushuaia
    Data Gathered for 1254046, tura, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=tura
    Not Enough Info for tapaua, br
    Data Gathered for 2172880, byron bay, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=byron bay
    Data Gathered for 344979, lebu, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=lebu
    Not Enough Info for barentsburg, sj
    Data Gathered for 3833367, ushuaia, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ushuaia
    Data Gathered for 3015546, gourdon, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=gourdon
    Data Gathered for 1528998, yumen, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=yumen
    Data Gathered for 2121385, severo-kurilsk, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=severo-kurilsk
    Data Gathered for 3366880, hermanus, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=hermanus
    Data Gathered for 3369157, cape town, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=cape town
    Data Gathered for 3833367, ushuaia, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ushuaia
    Not Enough Info for hakvik, no
    Not Enough Info for louisbourg, ca
    Data Gathered for 2163355, hobart, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=hobart
    Data Gathered for 587450, juba, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=juba
    Data Gathered for 3440777, rocha, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=rocha
    Data Gathered for 3896218, castro, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=castro
    Data Gathered for 5848280, kapaa, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=kapaa
    Data Gathered for 3471451, arraial do cabo, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=arraial do cabo
    Data Gathered for 6201424, mataura, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=mataura
    Data Gathered for 1706889, puro, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=puro
    Data Gathered for 3833367, ushuaia, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ushuaia
    Data Gathered for 3366880, hermanus, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=hermanus
    Data Gathered for 5106834, albany, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=albany
    Data Gathered for 3369157, cape town, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=cape town
    Data Gathered for 3451241, rio brilhante, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=rio brilhante
    Data Gathered for 4030556, rikitea, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=rikitea
    Data Gathered for 1848373, fukue, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=fukue
    Data Gathered for 2163355, hobart, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=hobart
    Data Gathered for 2022572, khatanga, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=khatanga
    Data Gathered for 6165406, thompson, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=thompson
    Data Gathered for 5380437, pacific grove, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=pacific grove
    Data Gathered for 1661950, ban nahin, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ban nahin
    Data Gathered for 3874787, punta arenas, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=punta arenas
    Data Gathered for 3381538, grand-santi, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=grand-santi
    Data Gathered for 1865309, katsuura, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=katsuura
    Not Enough Info for taolanaro, mg
    Data Gathered for 2069194, jamestown, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=jamestown
    Data Gathered for 3833367, ushuaia, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ushuaia
    Data Gathered for 5848280, kapaa, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=kapaa
    Data Gathered for 4020109, atuona, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=atuona
    Data Gathered for 2155415, new norfolk, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=new norfolk
    Data Gathered for 6167817, torbay, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=torbay
    Data Gathered for 1496421, krasnomayskiy, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=krasnomayskiy
    Data Gathered for 2069194, jamestown, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=jamestown
    Not Enough Info for attawapiskat, ca
    Data Gathered for 2013279, vostok, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=vostok
    Not Enough Info for bengkulu, id
    Data Gathered for 3932145, pisco, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=pisco
    Data Gathered for 2618795, klaksvik, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=klaksvik
    Data Gathered for 5919850, chapais, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=chapais
    Data Gathered for 1514792, gazojak, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=gazojak
    Data Gathered for 2180815, tuatapere, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=tuatapere
    Data Gathered for 5379439, ontario, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ontario
    Data Gathered for 262462, saint george, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=saint george
    Data Gathered for 3833367, ushuaia, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ushuaia
    Data Gathered for 3833367, ushuaia, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ushuaia
    Data Gathered for 6148373, sioux lookout, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=sioux lookout
    Data Gathered for 2194098, ahipara, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ahipara
    Data Gathered for 294117, avdon, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=avdon
    Not Enough Info for belushya guba, ru
    Data Gathered for 1855476, kushima, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=kushima
    Data Gathered for 4470244, havelock, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=havelock
    Data Gathered for 6165406, thompson, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=thompson
    Data Gathered for 934322, mahebourg, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=mahebourg
    Data Gathered for 2169535, dalby, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=dalby
    Not Enough Info for belushya guba, ru
    Data Gathered for 4030556, rikitea, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=rikitea
    Data Gathered for 5919850, chapais, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=chapais
    Data Gathered for 3421319, nuuk, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=nuuk
    Data Gathered for 2180815, tuatapere, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=tuatapere
    Data Gathered for 5989403, kapuskasing, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=kapuskasing
    Not Enough Info for bantry, ie
    Data Gathered for 3423146, ilulissat, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ilulissat
    Data Gathered for 3833367, ushuaia, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ushuaia
    Data Gathered for 6201424, mataura, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=mataura
    Data Gathered for 2158744, margate, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=margate
    Data Gathered for 5855927, hilo, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=hilo
    Data Gathered for 2075265, busselton, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=busselton
    Data Gathered for 3874787, punta arenas, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=punta arenas
    Not Enough Info for barentsburg, sj
    Data Gathered for 3451138, rio grande, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=rio grande
    Data Gathered for 1242110, kalmunai, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=kalmunai
    Data Gathered for 1714733, dingle, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=dingle
    Data Gathered for 2069194, jamestown, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=jamestown
    Data Gathered for 964432, port alfred, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=port alfred
    Data Gathered for 1691355, sabang, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=sabang
    Data Gathered for 2026160, borogontsy, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=borogontsy
    Data Gathered for 2180815, tuatapere, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=tuatapere
    Data Gathered for 240498, mongo, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=mongo
    Not Enough Info for nizhneyansk, ru
    Data Gathered for 3421719, narsaq, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=narsaq
    Not Enough Info for taolanaro, mg
    Data Gathered for 1637001, biak, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=biak
    Data Gathered for 2036892, hohhot, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=hohhot
    Data Gathered for 3471451, arraial do cabo, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=arraial do cabo
    Data Gathered for 72181, marzuq, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=marzuq
    Data Gathered for 2017155, saskylakh, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=saskylakh
    Data Gathered for 2110227, butaritari, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=butaritari
    Not Enough Info for mahadday weyne, so
    Data Gathered for 1735634, kuching, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=kuching
    Data Gathered for 5961417, gimli, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=gimli
    Data Gathered for 5380420, pacifica, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=pacifica
    Data Gathered for 2122090, pevek, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=pevek
    Data Gathered for 5961417, husavik, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=husavik
    Data Gathered for 3374210, sao filipe, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=sao filipe
    Data Gathered for 262462, saint george, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=saint george
    Data Gathered for 3403251, canto do buriti, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=canto do buriti
    Data Gathered for 3874787, punta arenas, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=punta arenas
    Not Enough Info for louisbourg, ca
    Data Gathered for 3530097, champerico, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=champerico
    Data Gathered for 1624725, tarakan, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=tarakan
    Data Gathered for 2175403, bluff, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=bluff
    Data Gathered for 3833367, ushuaia, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ushuaia
    Data Gathered for 2517679, fortuna, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=fortuna
    Data Gathered for 3369157, cape town, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=cape town
    Data Gathered for 296852, erzin, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=erzin
    Data Gathered for 3530097, champerico, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=champerico
    Data Gathered for 3378644, georgetown, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=georgetown
    Data Gathered for 4004293, ixtapa, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ixtapa
    Data Gathered for 1006984, east london, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=east london
    Data Gathered for 220448, aketi, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=aketi
    Data Gathered for 6201424, mataura, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=mataura
    Data Gathered for 608324, shetpe, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=shetpe
    Data Gathered for 3369157, cape town, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=cape town
    Data Gathered for 3833367, ushuaia, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ushuaia
    Not Enough Info for nizhneyansk, ru
    Data Gathered for 2340451, gombe, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=gombe
    Data Gathered for 2027042, batagay-alyta, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=batagay-alyta
    Data Gathered for 1273574, vaini, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=vaini
    Data Gathered for 3424607, tasiilaq, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=tasiilaq
    Data Gathered for 858701, shamilkala, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=shamilkala
    Data Gathered for 1651810, airai, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=airai
    Data Gathered for 2160063, codrington, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=codrington
    Data Gathered for 1852357, shimoda, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=shimoda
    Data Gathered for 231947, katakwi, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=katakwi
    Data Gathered for 154097, mgandu, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=mgandu
    Not Enough Info for illoqqortoormiut, gl
    Data Gathered for 3874787, punta arenas, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=punta arenas
    Data Gathered for 6144312, sept-iles, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=sept-iles
    Data Gathered for 6185377, yellowknife, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=yellowknife
    Data Gathered for 5960603, geraldton, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=geraldton
    Data Gathered for 2017155, saskylakh, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=saskylakh
    Data Gathered for 3378644, georgetown, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=georgetown
    Data Gathered for 5106834, albany, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=albany
    Data Gathered for 5106834, albany, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=albany
    Data Gathered for 3424607, tasiilaq, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=tasiilaq
    Data Gathered for 4021858, guerrero negro, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=guerrero negro
    Data Gathered for 2013279, vostok, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=vostok
    Data Gathered for 3366880, hermanus, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=hermanus
    Data Gathered for 1259385, port blair, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=port blair
    Data Gathered for 2075265, busselton, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=busselton
    Data Gathered for 178443, wajir, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=wajir
    Data Gathered for 2729907, longyearbyen, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=longyearbyen
    Not Enough Info for ngukurr, au
    Data Gathered for 5380437, pacific grove, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=pacific grove
    Data Gathered for 60019, eyl, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=eyl
    Data Gathered for 2729907, longyearbyen, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=longyearbyen
    Data Gathered for 4035715, avarua, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=avarua
    Data Gathered for 3874787, punta arenas, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=punta arenas
    Data Gathered for 3874787, punta arenas, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=punta arenas
    Data Gathered for 2075265, busselton, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=busselton
    Data Gathered for 1263942, manavalakurichi, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=manavalakurichi
    Data Gathered for 5855927, hilo, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=hilo
    Data Gathered for 4984075, alpena, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=alpena
    Data Gathered for 3896218, castro, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=castro
    Data Gathered for 5017822, bemidji, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=bemidji
    Data Gathered for 1054329, vangaindrano, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=vangaindrano
    Data Gathered for 5106834, albany, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=albany
    Not Enough Info for belushya guba, ru
    Not Enough Info for belushya guba, ru
    Data Gathered for 4020109, atuona, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=atuona
    Data Gathered for 1168700, ormara, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ormara
    Data Gathered for 4267710, sitka, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=sitka
    Data Gathered for 5880568, bethel, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=bethel
    Data Gathered for 2180815, tuatapere, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=tuatapere
    Data Gathered for 2121385, severo-kurilsk, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=severo-kurilsk
    Data Gathered for 1697332, ocampo, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ocampo
    Data Gathered for 2168943, devonport, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=devonport
    Not Enough Info for sentyabrskiy, ru
    Data Gathered for 2158744, margate, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=margate
    Data Gathered for 4030556, rikitea, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=rikitea
    Data Gathered for 2163355, hobart, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=hobart
    Data Gathered for 2063036, port lincoln, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=port lincoln
    Data Gathered for 2075265, busselton, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=busselton
    Data Gathered for 1633419, padang, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=padang
    Data Gathered for 4030556, rikitea, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=rikitea
    Data Gathered for 588365, vao, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=vao
    Not Enough Info for liapades, gr
    Data Gathered for 5106834, albany, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=albany
    Data Gathered for 3378644, georgetown, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=georgetown
    Data Gathered for 3424607, tasiilaq, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=tasiilaq
    Data Gathered for 2618795, klaksvik, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=klaksvik
    Data Gathered for 292968, abu dhabi, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=abu dhabi
    Data Gathered for 4031574, provideniya, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=provideniya
    Data Gathered for 6201424, mataura, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=mataura
    Data Gathered for 2126199, cherskiy, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=cherskiy
    Data Gathered for 5712169, baker city, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=baker city
    Data Gathered for 3465745, conceicao do mato dentro, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=conceicao do mato dentro
    Data Gathered for 1848373, fukue, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=fukue
    Data Gathered for 964432, port alfred, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=port alfred
    Data Gathered for 6201424, mataura, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=mataura
    Data Gathered for 964432, port alfred, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=port alfred
    Data Gathered for 5855927, hilo, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=hilo
    Data Gathered for 6167817, torbay, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=torbay
    Data Gathered for 2656067, broome, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=broome
    Not Enough Info for illoqqortoormiut, gl
    Data Gathered for 4035715, avarua, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=avarua
    Data Gathered for 1254046, tura, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=tura
    Data Gathered for 4031742, egvekinot, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=egvekinot
    Data Gathered for 3939761, hualmay, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=hualmay
    Data Gathered for 3833367, ushuaia, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ushuaia
    Data Gathered for 3453439, ponta do sol, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ponta do sol
    Data Gathered for 3874787, punta arenas, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=punta arenas
    Data Gathered for 1267239, hosakote, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=hosakote
    Data Gathered for 3831208, qaanaaq, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=qaanaaq
    Not Enough Info for camana, pe
    Data Gathered for 2022572, khatanga, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=khatanga
    Data Gathered for 4035715, avarua, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=avarua
    Data Gathered for 2140558, koumac, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=koumac
    Data Gathered for 2075265, busselton, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=busselton
    Data Gathered for 6185377, yellowknife, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=yellowknife
    Data Gathered for 3369157, cape town, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=cape town
    Data Gathered for 4501427, port elizabeth, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=port elizabeth
    Data Gathered for 5106834, albany, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=albany
    Data Gathered for 3356343, karasburg, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=karasburg
    Data Gathered for 2026126, borzya, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=borzya
    Data Gathered for 530196, malyye derbety, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=malyye derbety
    Data Gathered for 2012530, zhigansk, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=zhigansk
    Data Gathered for 5919815, channel-port aux basques, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=channel-port aux basques
    Data Gathered for 2126123, chokurdakh, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=chokurdakh
    Data Gathered for 3833367, ushuaia, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=ushuaia
    Data Gathered for 3026644, souillac, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=souillac
    Data Gathered for 5880568, bethel, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=bethel
    Data Gathered for 6170031, tuktoyaktuk, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=tuktoyaktuk
    Data Gathered for 3894426, coihaique, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=coihaique
    Not Enough Info for illoqqortoormiut, gl
    Data Gathered for 3412093, vestmannaeyjar, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=vestmannaeyjar
    Data Gathered for 4020109, atuona, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=atuona
    Data Gathered for 2450173, taoudenni, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=taoudenni
    Data Gathered for 4501427, port elizabeth, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=port elizabeth
    Data Gathered for 1028434, quelimane, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=quelimane
    Data Gathered for 2112802, hasaki, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=hasaki
    Data Gathered for 2297810, mumford, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=mumford
    Data Gathered for 6201424, mataura, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=mataura
    Data Gathered for 3424607, tasiilaq, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=tasiilaq
    Data Gathered for 1015776, bredasdorp, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=bredasdorp
    Data Gathered for 3831208, qaanaaq, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=qaanaaq
    Data Gathered for 6138908, saint-philippe, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=saint-philippe
    Data Gathered for 6201424, mataura, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=mataura
    Not Enough Info for palabuhanratu, id
    Not Enough Info for saleaula, ws
    Data Gathered for 3466980, caravelas, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=caravelas
    Data Gathered for 3471451, arraial do cabo, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=arraial do cabo
    Data Gathered for 3831208, qaanaaq, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=qaanaaq
    Data Gathered for 3374210, sao filipe, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=sao filipe
    Data Gathered for 2126199, cherskiy, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=cherskiy
    Data Gathered for 608324, shetpe, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=shetpe
    Not Enough Info for urumqi, cn
    Data Gathered for 1015776, bredasdorp, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=bredasdorp
    Data Gathered for 2022572, khatanga, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=khatanga
    Not Enough Info for umzimvubu, za
    Data Gathered for 3831208, qaanaaq, http://api.openweathermap.org/data/2.5/weather?appid=d3cfde203de9c80b7b1bab1e8e60ab91&units=Imperial&q=qaanaaq
    

FORMATTING COLUMNS


```python
location_clean["lat"] = location_clean["lat"].map("{0:.2f}".format)
location_clean["lon"] = location_clean["lon"].map("{0:.2f}".format)
location_clean["Humidity"] = pd.to_numeric(location_clean["Humidity"])
location_clean["Cloudiness"] = pd.to_numeric(location_clean["Cloudiness"])
location_clean["Date"] = pd.to_datetime(location_clean['Date'],unit='s')
location_clean = location_clean.dropna()
len(location_clean)
```




    454



CLEAN DATA FOR EXPORT


```python
location_final = location_clean[["city","Cloudiness","country",
                                 "Date","Humidity","lat","lon",
                                 "Max Temp","Wind Speed"]]
location_final.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>Cloudiness</th>
      <th>country</th>
      <th>Date</th>
      <th>Humidity</th>
      <th>lat</th>
      <th>lon</th>
      <th>Max Temp</th>
      <th>Wind Speed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>22</th>
      <td>mahebourg</td>
      <td>75.0</td>
      <td>mu</td>
      <td>2018-03-02 06:00:00</td>
      <td>79.0</td>
      <td>-40.78</td>
      <td>76.92</td>
      <td>84.2</td>
      <td>16.11</td>
    </tr>
    <tr>
      <th>734</th>
      <td>zabol</td>
      <td>0.0</td>
      <td>ir</td>
      <td>2018-03-02 06:00:00</td>
      <td>56.0</td>
      <td>31.61</td>
      <td>60.25</td>
      <td>68</td>
      <td>6.93</td>
    </tr>
    <tr>
      <th>428</th>
      <td>namibe</td>
      <td>20.0</td>
      <td>ao</td>
      <td>2018-03-02 06:36:30</td>
      <td>100.0</td>
      <td>-13.12</td>
      <td>6.70</td>
      <td>73.19</td>
      <td>4.76</td>
    </tr>
    <tr>
      <th>839</th>
      <td>atuona</td>
      <td>64.0</td>
      <td>pf</td>
      <td>2018-03-02 06:36:30</td>
      <td>97.0</td>
      <td>-3.31</td>
      <td>-139.14</td>
      <td>82.01</td>
      <td>18.07</td>
    </tr>
    <tr>
      <th>152</th>
      <td>punta arenas</td>
      <td>75.0</td>
      <td>cl</td>
      <td>2018-03-02 06:00:00</td>
      <td>71.0</td>
      <td>-72.38</td>
      <td>-99.39</td>
      <td>53.6</td>
      <td>17.22</td>
    </tr>
  </tbody>
</table>
</div>




```python
location_final.to_csv("weatherPyHWData.csv", encoding="utf-8", index=False,header=True)
```

CITY LATITUDE VS. MAX TEMPERATURE PLOT


```python
x_val = location_final["lat"]
y_val = location_final["Max Temp"]
plt.scatter(x_val,y_val)
plt.title("City Latitude vs. Max Temperature (03/01/2018)")
plt.ylabel("Max Temperature (F)")
plt.xlabel("Latitude")
plt.savefig("latVsMaxTemp.png")
plt.show()

```


![png](output_21_0.png)


CITY LATITUDE VS. HUMIDITY PLOT


```python
x_val = location_final["lat"]
y_val = location_final["Humidity"]
plt.scatter(x_val,y_val,color= 'blue', edgecolors = 'black', label = 'Lat vs. Humidity')
plt.title("City Latitude vs. Humidity (03/01/2018)")
plt.ylabel("Humidity (%)")
plt.xlabel("Latitude")
plt.savefig("latVsHumidity.png")
plt.show()
```


![png](output_23_0.png)


CITY LATITUDE VS. CLOUDINESS PLOT


```python
x_val = location_final["lat"]
y_val = location_final["Cloudiness"]
plt.scatter(x_val,y_val,color= 'blue', edgecolors = 'black', label = 'Lat vs. Cloudiness')
plt.title("City Latitude vs. Cloudiness (03/01/2018)")
plt.ylabel("Cloudiness (%)")
plt.xlabel("Latitude")
plt.savefig("latVsCloudiness.png")
plt.show()
```


![png](output_25_0.png)


CITY LATITUDE VS. WIND SPEED PLOT


```python
x_val = location_final["lat"]
y_val = location_final["Wind Speed"]
plt.scatter(x_val,y_val,color= 'blue', edgecolors = 'black', label = 'Lat vs. Wind Speed')
plt.title("City Latitude vs. Wind Speed (03/01/2018)")
plt.ylabel("Wind Speed (MPH)")
plt.xlabel("Latitude")
plt.savefig("latVsWindSpeed.png")
plt.show()
```


![png](output_27_0.png)

