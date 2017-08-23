

```python
# Dependencies
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
import seaborn as sns
from citipy import citipy as cp
from datetime import datetime
from random import uniform
import random as rd

np.random.seed(sum(map(ord, "aesthetics")))

# My Google API Key
gkey="AIzaSyBxoHPgXoiBQ1TuPrFX7JjBatqNud9gems"

# Created my api key for openweathermap.org/api   key name = myOWM
# Used my comcast email id and chrisg4owm
api_owmkey = "b28cc4b4c0a1d1d9ff4c2d9e808f9a5a"

# Created 2nd api key for openweathermap.org/api   key name = OWM1
# Used my gmail id and chrisg4owm2
#api_owmkey = "694332937bad44a33dd12de17c5e78e8"  

# Created 2nd api key for openweathermap.org/api   key name = OWM2
# Used my gmail id and chrisg4owm2
#api_owmkey = "44db84fb592301e3b8e80fd68c27e847"  
```


```python
# Background Information on Latitude and Longitude:

# Latitudes-
# In geography, latitude is a geographic coordinate that specifies 
# the north–south position of a point on the Earth's surface. 
# Latitude is an angle (defined below) which ranges from 0° at the 
# Equator to 90° (North or South) at the poles.
#
# While lines of latitude run across a map east-west, the point of 
# latitude makes the n0rth-south position of a point on earth.  
# Lines of latitude start at 0 degrees at the equator and end a 90 
# degrees at the North and South Poles.  Everything north of the 
# equator is known as the Northern Hemisphere and everything south 
# of the equator is known as the Southern Hemisphere.
#
# Lines of latitude are called parallels and in total there are 180 
# degrees of latitude.  The distance between each degree of 
# latitude is about 69 miles (110 kilometers).  The five major 
# parallels of latitudes from north to south are called: Arctic 
# Circle, Tropic of Cancer, Equator, Tropic of Capricorn, and the 
# Antarctic Circle. On a maps where the orientation of the map is 
# either due north or due south, latitude appears as horizontal lines.
#
# Longitude-
# Longitude is the measurement east or west of the prime meridian. 
# Longitude is measured by imaginary lines that run around the Earth 
# vertically (up and down) and meet at the North and South Poles. 
# These lines are known as meridians.
#
# Longitude lines run north-south and mark the position east-west of 
# a point. Lines of longitude are known as meridians.  These lines run 
# from pole to pole, crossing the equator at right angles. There are 
# 360 degrees of latitude and the latitude line of 0 degrees is known 
# as the Prime Meridian and it divides the world into the Eastern 
# Hemisphere and the Western Hemisphere (-180 degrees degrees of 
# longitude west and 180 degrees of longitude east).
#
# The distance between longitudes narrows the further away from the 
# equator.  The distance between longitudes at the equator is the same 
# as latitude, roughly 69 miles. At 45 degrees north or south, the 
# distance between is about 49 miles (79 km). The distance between 
# longitudes reaches zero at the poles as the lines of meridian 
# converge at that point.
#
# The Prime Meridian is at 0 degrees longitude, just as the equator is at 
# 0 degrees latitude
#
```


```python
# Weather Plot Trend Analysis 

# Source Data Comments: 
# The assignment required creating our own data, and the most difficult 
# part was remembering geography lessons from too many years ago.  I 
# choose a method of dividing the earth into quadrants using the image at
# this link: http://i37.tinypic.com/345izb4.jpg as an example.  From the 
# image, I used the x-axis as latitude -180.0 to 180.0(Far West to 
# Far East), and the y-axis was -90.0 to 90.0.  Finding unique city geo 
# coordinates proved to be the difficult part, but I know there has got 
# to be a much better way to go about gathering the cities.  Learning 
# activities are necessary, but it is good to learn real world knowledge 
# and experience in the area of data gathering because I am finding that 
# I spend a large amount of time just gathering data.
#
# Data Trend Analysis:
# I think the charts would have been more informative with longitude as the 
# y-axis and the choosen y-axis (temperature in this case) as a third 
# variable.  This would make a better picture of the distribution because I
# could tell where the city was on the line of longitude.  
#
# So, with temperature as the y-axis, I can tell where a city lies in terms
# of latitude in relation to the prime meridian which allows me to make some
# assumptions because I know the continents and where the prime meridian
# cuts across the continents.  From this I would say the trend shows that 
# cities are concentrated in areas of moderate climate.  Cities avoid the 
# extreme cold of the north and south poles, there are fewer cities in areas
# above 80 degrees and below 60 degrees fahrenheit.  If I look at the wind, 
# humidity, and temperature together, I think they confirm the clustering 
# trend of cities and therefore the most people in moderate climate areas.
#
# I found the cloudiness chart interesting, but the least informative of the 
# four charts.  While there was a good concentration of cities with 0% 
# cloudiness, it was cloudy in a lot of cities to some degree which is good 
# because clouds are necessary for rain and water is necessary for life.  So
# it is difficult to decipher a trend other than there are more cities with
# cloudy weather than there are with no clouds at all.  I think I also 
# learned from this exercise that one or two more variables could make a big
# difference in what information could be conveyed.
#
# The biggest take-away was that it was difficult to draw conclusions, pictures,
# or trends using current data. Also, this wasn't really interesting, gripping 
# or extreme data.  It was the daily weather report for 500+ cities.
#
# If I look at the humidity and wind speed charts I get two pieces of information.
# One was that humidity is more widespread than I thought because I have this 
# mistaken idea that if humidity isn't sticky and yucky then it doesn't exist.
# That's wrong, so I thought the humidity chart was useful and conveyed valid
# and important information.  And two, the wind speed chart confirmed weather 
# information consistent with my area which is that winds up to 20 mph are normal
# and occur for a large number of cities.  There are fewer cities experiencing wind
# speeds above 20 mph.  Higher gusts can occur, like at higher elevations, but 
# these are usually mentioned as outliers not as the wind speed for the area.
#
# The overall lesson for me was in understanding the data (in my case, in 
# geo-coordinate terms), and to understand what questions you are trying to
# answer.  Also, I encountered limitation with free data because my api key stopped
# working.  As I acquired a new key, I was wondering about legal and ethical use 
# of other people's data.  That hasn't been covered in class, although, plagiarism in 
# the professional and educational world has been in the news the last few 
# years, and was a part of my recent experience as a TA for an Accounting 
# Information Systems class.  This was a good homework assignment.   
```


```python
# Divide the earth into quadrants- see image http://i37.tinypic.com/345izb4.jpg
# 
#                     Latitude = x     Longitude = y            
#                   ----------------  ---------------   
# Quad4-far west  = (-180.0 | -90.0)  (-90.0 | 90.0)
# Quad3-near west =  (-90.0 | 0.0)    (-90.0 | 90.0)
# Quad2-near east =  (0.0   |  90.0)  (-90.0 | 90.0)
# Quad1-far east  =  (90.0  | 180.0)  (-90.0 | 90.0)
```


```python
# # Generate a list of 500+ unique cities from all around the earth.
# # Divide the earth into quadrants.  See http://i37.tinypic.com/345izb4.jpg
# #
# #-----------------------------------------------------------------------
# #--- Declare Variables

# Set to True for print statements
Debug = False

list_length = 275

#final data frame
city_wdf = pd.DataFrame() #creates a new dataframe that's empty
city_wdf["city"] = ""
city_wdf["country"] = ""

load_count = 0   # used for loading geo coordinates 
clean_count = 0  # max number of iterations per quadrant

# list of latitude range tuples Far West to Far East
quad_lat = [(-180,-90), (-90,0), (0,90), (90,180)]

# ----------------------------------------------------------------------

#Loop thru latitude tuples
for a in quad_lat:
    # working data frame
    city_tmp = pd.DataFrame() # creates a new dataframe that's empty
    city_tmp["city"] = ""
    city_tmp["country"] = ""
        
    clean_count = 0  # prevents infinite loop
    counter = 0      # used to set the index for city_tmp
    
    # Pass these tuple values into while loop
    b,c = a[0], a[1]
    print("Current tuple ", a)
    print("b = " + str(b) + " c = " + str(c))
    print("Pass b, c to while loop...")
    
    while len(city_tmp.index)<= list_length:
        
        geo_list = []  # create empty geo_list
        load_count = counter
        if Debug:
            print("Length city_tmp ", len(city_tmp.index))
            print("counter is ", counter)
            print("load_count is ", load_count)
        
        # Append tuples of coordinates to the geo_list
        while load_count <= list_length:
            tup = ()
                  # latitudes    # longitudes
            x,y = uniform(b,c), uniform(-90, 90)
            x = np.round(x,2)
            y = np.round(y,2)
            if Debug:
                print("x ", x)
                print("y ", y)
            tup = (x,y)
            geo_list.append(tup)
            load_count += 1
        
        if Debug:
            print("Length of geo_list ",len(geo_list))
        
        # get the list of city, country values and update working data frame
        for i in range(0, len(geo_list)):
            x,y = geo_list[i]
            city = cp.nearest_city(x, y)
            if Debug:
                print(city.city_name,end=", ")     
                print(city.country_code)  
            city_tmp.set_value(counter,"city", city.city_name)
            city_tmp.set_value(counter,"country", city.country_code)
            counter += 1
        if Debug:
            print("Length of city_tmp ",len(city_tmp))
            print("Before clean up ", city_tmp)
            
        # Clean up the data frame
        # Sort the data by city, country
        city_tmp.sort_values(["city","country"],ascending=[True, False], inplace=True) 

        # Remove duplicate city, country rows
        city_tmp = city_tmp.drop_duplicates(subset=["city","country"], 
                                        keep="last").reset_index(drop=True)
        
        # Reset the counter for the next loop
        counter = len(city_tmp.index) + 1
        
        clean_count += 1
        # Prevent infinite loop
        if clean_count == 18:
            break
        
        if Debug:
            print("After clean up length of city_tmp ",len(city_tmp))
            print("After clean up counter is ", counter)
    
    # concatenate working data frame to final data frame
    city_wdf = pd.concat([city_wdf, city_tmp])
    print(len(city_wdf))            
        
            
if Debug:    
    print(len(city_wdf.index))
    print()
    print(city_wdf)
```

    Current tuple  (-180, -90)
    b = -180 c = -90
    Pass b, c to while loop...
    10
    Current tuple  (-90, 0)
    b = -90 c = 0
    Pass b, c to while loop...
    276
    Current tuple  (0, 90)
    b = 0 c = 90
    Pass b, c to while loop...
    551
    Current tuple  (90, 180)
    b = 90 c = 180
    Pass b, c to while loop...
    564
    


```python
# Final clean up of the city data frame
# Sort the data by city, country
city_wdf = city_wdf.sort_values(["city","country"],
                                ascending=[True, False]).reset_index(drop=True)

print(len(city_wdf.index))

# Remove duplicate city, country rows and rebuild the index
city_wdf = city_wdf.drop_duplicates(subset=["city","country"],
                                    keep="last").reset_index(drop=True)

# Add the rest of the columns once we have 500+ cities
city_wdf["date"] = ""
city_wdf["lat"] = 0.0
city_wdf["lng"] = 0.0
city_wdf["max_temperature"] = 0.0
city_wdf["humidity"] = 0.0
city_wdf["cloudiness"] = 0.0
city_wdf["wind_speed"] = 0.0

#print(city_wdf.dtypes)
print(len(city_wdf.index))
city_wdf.head(10)
```

    564
    537
    




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
      <th>country</th>
      <th>date</th>
      <th>lat</th>
      <th>lng</th>
      <th>max_temperature</th>
      <th>humidity</th>
      <th>cloudiness</th>
      <th>wind_speed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>abha</td>
      <td>sa</td>
      <td></td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>acarau</td>
      <td>br</td>
      <td></td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>agirish</td>
      <td>ru</td>
      <td></td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>aksu</td>
      <td>kz</td>
      <td></td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>aksu</td>
      <td>cn</td>
      <td></td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>akureyri</td>
      <td>is</td>
      <td></td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>albany</td>
      <td>au</td>
      <td></td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>alta floresta</td>
      <td>br</td>
      <td></td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>ambilobe</td>
      <td>mg</td>
      <td></td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>ambodifototra</td>
      <td>mg</td>
      <td></td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# # Open Weather Map Example

# # Single Open Weather Map request with json printed "pretty"

# import json
# import requests as req

# # Created my api key for openweathermap.org/api   key   name = myOWM
# api_owmkey = "b28cc4b4c0a1d1d9ff4c2d9e808f9a5a"

# url = "http://api.openweathermap.org/data/2.5/weather?"
# city = "san francisco"
# country = "us"
# units = "imperial"

# # Build query URL
# query_url = url + "appid=" + api_owmkey + "&q=" + city + "," + country \
#             + "&units=" + units
# print(query_url
#      )
# # Get weather data
# weather_response = req.get(query_url)
# weather_json = weather_response.json()

# # Get the temperature from the response
# print("The weather API responded with: " + json.dumps(weather_json, indent=2) + ".")

```


```python
# # Make OpenWeatherMap api calls.  
#
# # http://openweathermap.org/api  - this has the API documentation
#
# # API call: 
# # api.openweathermap.org/data/2.5/weather?q={city},{country}&unit={unit}&APPID={key} 
# # city name and country code divided by comma, (use ISO 3166 country codes)
#
# # API example: city = aasiaat country = gl
# # http://api.openweathermap.org/data/2.5/weather?q=aasiaat,gl&units=imperial&APPID=key
# # Or
# # http://api.openweathermap.org/data/2.5/weather?appid=key&q=aasiaat,gl&units=imperial

import json
import requests as req

# Created my api key for openweathermap.org/api key
#api_owmkey = "b28cc4b4c0a1d1d9ff4c2d9e808f9a5a"
#api_owmkey = "694332937bad44a33dd12de17c5e78e8"
#api_owmkey = "44db84fb592301e3b8e80fd68c27e847"  

error_count = 0

for index, row in city_wdf.iterrows():
    url = "http://api.openweathermap.org/data/2.5/weather?"
    city = row["city"]
    country = row["country"]
    units = "imperial"
    

    # Build query URL
    query_url = url + "q=" + city + "," + country \
                + "&units=" + units + "&APPID=" + api_owmkey 
    
    try:
        # Get weather data
        city_weather = req.get(query_url).json()
        #print("The weather API responded with: " + json.dumps(city_weather, indent=2) \
        #+ ".")
        print("Row index: " + str(index) + " | " + row["city"] + "," + row["country"] +
              " -- query_url: " + query_url)
        
        # # OWM dt (date) = Time of data calculation, unix, UTC 
        friendly_date = datetime.fromtimestamp(int(city_weather["dt"])).strftime('%Y-%m-%d %H:%M:%S')
        
        city_wdf.set_value(index, "date", friendly_date)
        city_wdf.set_value(index, "lat", city_weather["coord"]["lon"])
        city_wdf.set_value(index, "lng", city_weather["coord"]["lat"])
        city_wdf.set_value(index, "max_temperature", city_weather["main"]["temp_max"])
        city_wdf.set_value(index, "humidity", city_weather["main"]["humidity"])
        city_wdf.set_value(index, "cloudiness", city_weather["clouds"]["all"])
        city_wdf.set_value(index, "wind_speed", city_weather["wind"]["speed"])
    
    except KeyError:
        print("The key doesn't exist: " + row["city"] + ", " + row["country"] + "." )
        print(KeyError)
        error_count += 1
        
print("Total errors: ", error_count)
city_wdf.head()
```

    Row index: 0 | abha,sa -- query_url: http://api.openweathermap.org/data/2.5/weather?q=abha,sa&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 1 | acarau,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=acarau,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 2 | agirish,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=agirish,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 3 | aksu,kz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=aksu,kz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 4 | aksu,cn -- query_url: http://api.openweathermap.org/data/2.5/weather?q=aksu,cn&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 5 | akureyri,is -- query_url: http://api.openweathermap.org/data/2.5/weather?q=akureyri,is&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 6 | albany,au -- query_url: http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 7 | alta floresta,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=alta floresta,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 8 | ambilobe,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ambilobe,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 9 | ambodifototra,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ambodifototra,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 10 | amderma,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=amderma,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 11 | ampanihy,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ampanihy,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 12 | ancud,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ancud,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 13 | anjozorobe,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=anjozorobe,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 14 | antalaha,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=antalaha,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 15 | antofagasta,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=antofagasta,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 16 | aquidauana,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=aquidauana,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 17 | archidona,ec -- query_url: http://api.openweathermap.org/data/2.5/weather?q=archidona,ec&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 18 | areia branca,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=areia branca,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 19 | arkhipo-osipovka,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=arkhipo-osipovka,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 20 | arraial do cabo,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=arraial do cabo,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 21 | asfi,ma -- query_url: http://api.openweathermap.org/data/2.5/weather?q=asfi,ma&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 22 | ashqelon,il -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ashqelon,il&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 23 | asuncion,py -- query_url: http://api.openweathermap.org/data/2.5/weather?q=asuncion,py&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 24 | atar,mr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=atar,mr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 25 | attawapiskat,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=attawapiskat,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 26 | axim,gh -- query_url: http://api.openweathermap.org/data/2.5/weather?q=axim,gh&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 27 | bagotville,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bagotville,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 28 | bakel,sn -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bakel,sn&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 29 | balad,iq -- query_url: http://api.openweathermap.org/data/2.5/weather?q=balad,iq&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 30 | bam,ir -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bam,ir&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 31 | bambous virieux,mu -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bambous virieux,mu&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 32 | bandarbeyla,so -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bandarbeyla,so&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 33 | bar harbor,us -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bar harbor,us&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 34 | barawe,so -- query_url: http://api.openweathermap.org/data/2.5/weather?q=barawe,so&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 35 | bardiyah,ly -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bardiyah,ly&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 36 | barentsburg,sj -- query_url: http://api.openweathermap.org/data/2.5/weather?q=barentsburg,sj&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    The key doesn't exist: barentsburg, sj.
    <class 'KeyError'>
    Row index: 37 | barinas,ve -- query_url: http://api.openweathermap.org/data/2.5/weather?q=barinas,ve&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 38 | bathsheba,bb -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bathsheba,bb&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 39 | beira,mz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=beira,mz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 40 | belmonte,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=belmonte,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 41 | beloha,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=beloha,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 42 | belushya guba,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=belushya guba,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 43 | bengkulu,id -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bengkulu,id&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 44 | berea,us -- query_url: http://api.openweathermap.org/data/2.5/weather?q=berea,us&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 45 | bereda,so -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bereda,so&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 46 | berlevag,no -- query_url: http://api.openweathermap.org/data/2.5/weather?q=berlevag,no&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 47 | beyneu,kz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=beyneu,kz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 48 | bhainsdehi,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bhainsdehi,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 49 | bhatkal,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bhatkal,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 50 | birecik,tr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=birecik,tr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 51 | birjand,ir -- query_url: http://api.openweathermap.org/data/2.5/weather?q=birjand,ir&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 52 | bjornevatn,no -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bjornevatn,no&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 53 | blonduos,is -- query_url: http://api.openweathermap.org/data/2.5/weather?q=blonduos,is&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 54 | bolobo,cd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bolobo,cd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 55 | bonavista,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bonavista,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 56 | bondoukou,ci -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bondoukou,ci&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 57 | boueni,yt -- query_url: http://api.openweathermap.org/data/2.5/weather?q=boueni,yt&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 58 | bouza,ne -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bouza,ne&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 59 | boyuibe,bo -- query_url: http://api.openweathermap.org/data/2.5/weather?q=boyuibe,bo&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 60 | brae,gb -- query_url: http://api.openweathermap.org/data/2.5/weather?q=brae,gb&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 61 | bredasdorp,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 62 | bridgetown,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bridgetown,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 63 | brokopondo,sr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=brokopondo,sr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 64 | brunico,it -- query_url: http://api.openweathermap.org/data/2.5/weather?q=brunico,it&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 65 | bubaque,gw -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bubaque,gw&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 66 | bud,no -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bud,no&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 67 | buenos aires,cr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=buenos aires,cr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 68 | buqayq,sa -- query_url: http://api.openweathermap.org/data/2.5/weather?q=buqayq,sa&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 69 | burica,pa -- query_url: http://api.openweathermap.org/data/2.5/weather?q=burica,pa&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 70 | busselton,au -- query_url: http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 71 | butembo,cd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=butembo,cd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 72 | cabedelo,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=cabedelo,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 73 | cacoal,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=cacoal,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 74 | camacari,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=camacari,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 75 | camana,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=camana,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 76 | camapua,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=camapua,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 77 | cambrils,es -- query_url: http://api.openweathermap.org/data/2.5/weather?q=cambrils,es&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 78 | canarana,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=canarana,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 79 | canita,pa -- query_url: http://api.openweathermap.org/data/2.5/weather?q=canita,pa&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 80 | canutama,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=canutama,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 81 | cap malheureux,mu -- query_url: http://api.openweathermap.org/data/2.5/weather?q=cap malheureux,mu&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 82 | cape coast,gh -- query_url: http://api.openweathermap.org/data/2.5/weather?q=cape coast,gh&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 83 | cape town,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 84 | carauari,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=carauari,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 85 | caravelas,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=caravelas,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 86 | carnarvon,au -- query_url: http://api.openweathermap.org/data/2.5/weather?q=carnarvon,au&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 87 | carnot,cf -- query_url: http://api.openweathermap.org/data/2.5/weather?q=carnot,cf&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 88 | carutapera,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=carutapera,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 89 | casa nova,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=casa nova,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 90 | cascais,pt -- query_url: http://api.openweathermap.org/data/2.5/weather?q=cascais,pt&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 91 | castro,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=castro,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 92 | caucaia,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=caucaia,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 93 | caxito,ao -- query_url: http://api.openweathermap.org/data/2.5/weather?q=caxito,ao&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 94 | cayenne,gf -- query_url: http://api.openweathermap.org/data/2.5/weather?q=cayenne,gf&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 95 | cazaje,ao -- query_url: http://api.openweathermap.org/data/2.5/weather?q=cazaje,ao&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 96 | chama,zm -- query_url: http://api.openweathermap.org/data/2.5/weather?q=chama,zm&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 97 | chancay,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=chancay,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 98 | chapleau,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=chapleau,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 99 | chicama,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=chicama,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 100 | chiredzi,zw -- query_url: http://api.openweathermap.org/data/2.5/weather?q=chiredzi,zw&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 101 | chissamba,ao -- query_url: http://api.openweathermap.org/data/2.5/weather?q=chissamba,ao&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 102 | chokwe,mz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=chokwe,mz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 103 | chore,py -- query_url: http://api.openweathermap.org/data/2.5/weather?q=chore,py&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 104 | chuy,uy -- query_url: http://api.openweathermap.org/data/2.5/weather?q=chuy,uy&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 105 | cidreira,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=cidreira,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 106 | clyde river,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=clyde river,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 107 | codrington,ag -- query_url: http://api.openweathermap.org/data/2.5/weather?q=codrington,ag&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 108 | coihaique,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=coihaique,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 109 | conakry,gn -- query_url: http://api.openweathermap.org/data/2.5/weather?q=conakry,gn&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 110 | conde,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=conde,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 111 | consolacion del sur,cu -- query_url: http://api.openweathermap.org/data/2.5/weather?q=consolacion del sur,cu&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 112 | copiapo,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=copiapo,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 113 | coquimbo,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=coquimbo,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 114 | coruripe,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=coruripe,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 115 | coxim,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=coxim,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 116 | cozumel,mx -- query_url: http://api.openweathermap.org/data/2.5/weather?q=cozumel,mx&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 117 | cravo norte,co -- query_url: http://api.openweathermap.org/data/2.5/weather?q=cravo norte,co&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 118 | cumaribo,co -- query_url: http://api.openweathermap.org/data/2.5/weather?q=cumaribo,co&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 119 | cururupu,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=cururupu,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 120 | dalen,no -- query_url: http://api.openweathermap.org/data/2.5/weather?q=dalen,no&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 121 | davlekanovo,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=davlekanovo,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 122 | devrek,tr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=devrek,tr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 123 | dharchula,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=dharchula,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 124 | dharmadam,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=dharmadam,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 125 | dhola,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=dhola,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 126 | diffa,ne -- query_url: http://api.openweathermap.org/data/2.5/weather?q=diffa,ne&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 127 | dikson,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=dikson,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 128 | dingle,ie -- query_url: http://api.openweathermap.org/data/2.5/weather?q=dingle,ie&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 129 | doka,sd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=doka,sd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 130 | dom pedrito,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=dom pedrito,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 131 | dunda,tz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=dunda,tz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 132 | durban,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=durban,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 133 | dwarka,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=dwarka,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 134 | east london,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=east london,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 135 | ekuvukeni,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ekuvukeni,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 136 | elizabeth city,us -- query_url: http://api.openweathermap.org/data/2.5/weather?q=elizabeth city,us&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 137 | emba,kz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=emba,kz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 138 | erithrai,gr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=erithrai,gr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 139 | esmeraldas,ec -- query_url: http://api.openweathermap.org/data/2.5/weather?q=esmeraldas,ec&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 140 | filadelfia,py -- query_url: http://api.openweathermap.org/data/2.5/weather?q=filadelfia,py&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 141 | florianopolis,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=florianopolis,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 142 | fuerte olimpo,py -- query_url: http://api.openweathermap.org/data/2.5/weather?q=fuerte olimpo,py&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 143 | gabu,gw -- query_url: http://api.openweathermap.org/data/2.5/weather?q=gabu,gw&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 144 | gairo,tz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=gairo,tz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 145 | gamba,ga -- query_url: http://api.openweathermap.org/data/2.5/weather?q=gamba,ga&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 146 | gambela,et -- query_url: http://api.openweathermap.org/data/2.5/weather?q=gambela,et&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 147 | gat,ly -- query_url: http://api.openweathermap.org/data/2.5/weather?q=gat,ly&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 148 | general roca,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=general roca,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 149 | georgetown,sh -- query_url: http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 150 | geraldton,au -- query_url: http://api.openweathermap.org/data/2.5/weather?q=geraldton,au&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 151 | goderich,sl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=goderich,sl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 152 | goianesia,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=goianesia,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 153 | gondar,et -- query_url: http://api.openweathermap.org/data/2.5/weather?q=gondar,et&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 154 | grand baie,mu -- query_url: http://api.openweathermap.org/data/2.5/weather?q=grand baie,mu&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 155 | grand gaube,mu -- query_url: http://api.openweathermap.org/data/2.5/weather?q=grand gaube,mu&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 156 | grand river south east,mu -- query_url: http://api.openweathermap.org/data/2.5/weather?q=grand river south east,mu&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 157 | grao mogol,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=grao mogol,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 158 | grindavik,is -- query_url: http://api.openweathermap.org/data/2.5/weather?q=grindavik,is&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 159 | gweta,bw -- query_url: http://api.openweathermap.org/data/2.5/weather?q=gweta,bw&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 160 | hadejia,ng -- query_url: http://api.openweathermap.org/data/2.5/weather?q=hadejia,ng&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 161 | hambantota,lk -- query_url: http://api.openweathermap.org/data/2.5/weather?q=hambantota,lk&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 162 | hamilton,bm -- query_url: http://api.openweathermap.org/data/2.5/weather?q=hamilton,bm&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 163 | harper,lr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=harper,lr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 164 | havelock,us -- query_url: http://api.openweathermap.org/data/2.5/weather?q=havelock,us&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 165 | havoysund,no -- query_url: http://api.openweathermap.org/data/2.5/weather?q=havoysund,no&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 166 | havre-saint-pierre,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=havre-saint-pierre,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 167 | hearst,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=hearst,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 168 | henties bay,na -- query_url: http://api.openweathermap.org/data/2.5/weather?q=henties bay,na&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 169 | hermanus,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 170 | hillsborough,gd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=hillsborough,gd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 171 | hithadhoo,mv -- query_url: http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 172 | hobyo,so -- query_url: http://api.openweathermap.org/data/2.5/weather?q=hobyo,so&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 173 | horizontina,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=horizontina,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 174 | huarmey,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=huarmey,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 175 | iberia,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=iberia,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 176 | ichchapuram,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ichchapuram,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 177 | igbo ora,ng -- query_url: http://api.openweathermap.org/data/2.5/weather?q=igbo ora,ng&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 178 | ikongo,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ikongo,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 179 | ilebo,cd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ilebo,cd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 180 | illoqqortoormiut,gl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=illoqqortoormiut,gl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 181 | ilulissat,gl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ilulissat,gl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 182 | inhambane,mz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=inhambane,mz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 183 | inzer,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=inzer,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 184 | iqaluit,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=iqaluit,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 185 | iquitos,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=iquitos,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 186 | iracemapolis,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=iracemapolis,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 187 | irara,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=irara,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 188 | iskateley,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=iskateley,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 189 | issoire,fr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=issoire,fr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 190 | itarana,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=itarana,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 191 | itarema,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=itarema,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 192 | jacareacanga,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=jacareacanga,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 193 | jalu,ly -- query_url: http://api.openweathermap.org/data/2.5/weather?q=jalu,ly&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 194 | jamestown,sh -- query_url: http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 195 | jinotega,ni -- query_url: http://api.openweathermap.org/data/2.5/weather?q=jinotega,ni&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 196 | joensuu,fi -- query_url: http://api.openweathermap.org/data/2.5/weather?q=joensuu,fi&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 197 | kabare,cd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kabare,cd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 198 | kaka,tm -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kaka,tm&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 199 | kalabo,zm -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kalabo,zm&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 200 | kalachinsk,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kalachinsk,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 201 | kalomo,zm -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kalomo,zm&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 202 | kambove,cd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kambove,cd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 203 | kamina,cd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kamina,cd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 204 | kang,bw -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kang,bw&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 205 | kankon,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kankon,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 206 | karauzyak,uz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=karauzyak,uz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 207 | karema,tz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=karema,tz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 208 | karwar,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=karwar,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 209 | kasongo-lunda,cd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kasongo-lunda,cd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 210 | katete,zm -- query_url: http://api.openweathermap.org/data/2.5/weather?q=katete,zm&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 211 | kathmandu,np -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kathmandu,np&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 212 | katima mulilo,na -- query_url: http://api.openweathermap.org/data/2.5/weather?q=katima mulilo,na&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 213 | kazalinsk,kz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kazalinsk,kz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 214 | kemijarvi,fi -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kemijarvi,fi&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 215 | keti bandar,pk -- query_url: http://api.openweathermap.org/data/2.5/weather?q=keti bandar,pk&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 216 | khakhea,bw -- query_url: http://api.openweathermap.org/data/2.5/weather?q=khakhea,bw&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 217 | kindu,cd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kindu,cd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 218 | kipini,ke -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kipini,ke&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 219 | kiri buru,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kiri buru,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 220 | kirovsk,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kirovsk,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 221 | kisesa,tz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kisesa,tz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 222 | kismayo,so -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kismayo,so&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 223 | kitob,uz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kitob,uz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 224 | klaksvik,fo -- query_url: http://api.openweathermap.org/data/2.5/weather?q=klaksvik,fo&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 225 | kodar,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kodar,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 226 | kodinar,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kodinar,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 227 | korcula,hr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=korcula,hr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 228 | korla,cn -- query_url: http://api.openweathermap.org/data/2.5/weather?q=korla,cn&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 229 | kosonsoy,uz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kosonsoy,uz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 230 | kpandae,gh -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kpandae,gh&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 231 | kruisfontein,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kruisfontein,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 232 | kungur,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kungur,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 233 | kuva,uz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kuva,uz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 234 | la plata,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=la plata,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 235 | la primavera,co -- query_url: http://api.openweathermap.org/data/2.5/weather?q=la primavera,co&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 236 | labrea,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=labrea,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 237 | labutta,mm -- query_url: http://api.openweathermap.org/data/2.5/weather?q=labutta,mm&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 238 | lafia,ng -- query_url: http://api.openweathermap.org/data/2.5/weather?q=lafia,ng&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 239 | lagoa,pt -- query_url: http://api.openweathermap.org/data/2.5/weather?q=lagoa,pt&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 240 | laguna,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=laguna,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 241 | lake city,us -- query_url: http://api.openweathermap.org/data/2.5/weather?q=lake city,us&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 242 | lamu,ke -- query_url: http://api.openweathermap.org/data/2.5/weather?q=lamu,ke&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 243 | lebu,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=lebu,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 244 | lichinga,mz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=lichinga,mz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 245 | lima,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=lima,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 246 | litoral del san juan,co -- query_url: http://api.openweathermap.org/data/2.5/weather?q=litoral del san juan,co&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 247 | lixourion,gr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=lixourion,gr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 248 | loandjili,cg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=loandjili,cg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 249 | locri,it -- query_url: http://api.openweathermap.org/data/2.5/weather?q=locri,it&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 250 | lodja,cd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=lodja,cd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 251 | longyearbyen,sj -- query_url: http://api.openweathermap.org/data/2.5/weather?q=longyearbyen,sj&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 252 | los llanos de aridane,es -- query_url: http://api.openweathermap.org/data/2.5/weather?q=los llanos de aridane,es&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 253 | loukhi,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=loukhi,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 254 | luanda,ao -- query_url: http://api.openweathermap.org/data/2.5/weather?q=luanda,ao&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 255 | luangwa,zm -- query_url: http://api.openweathermap.org/data/2.5/weather?q=luangwa,zm&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 256 | lubango,ao -- query_url: http://api.openweathermap.org/data/2.5/weather?q=lubango,ao&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 257 | luderitz,na -- query_url: http://api.openweathermap.org/data/2.5/weather?q=luderitz,na&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 258 | luena,ao -- query_url: http://api.openweathermap.org/data/2.5/weather?q=luena,ao&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 259 | lusambo,cd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=lusambo,cd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 260 | lysyye gory,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=lysyye gory,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 261 | mabaruma,gy -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mabaruma,gy&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 262 | maceio,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=maceio,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 263 | madre de deus,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=madre de deus,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 264 | mahebourg,mu -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mahebourg,mu&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 265 | mahibadhoo,mv -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mahibadhoo,mv&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 266 | mahon,es -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mahon,es&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 267 | maldonado,uy -- query_url: http://api.openweathermap.org/data/2.5/weather?q=maldonado,uy&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 268 | malinyi,tz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=malinyi,tz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 269 | manakara,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=manakara,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 270 | mancio lima,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mancio lima,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 271 | mangochi,mw -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mangochi,mw&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 272 | mangrol,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mangrol,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 273 | manica,mz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=manica,mz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 274 | maniitsoq,gl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=maniitsoq,gl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 275 | manono,cd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=manono,cd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 276 | manta,ec -- query_url: http://api.openweathermap.org/data/2.5/weather?q=manta,ec&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 277 | mar del plata,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mar del plata,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 278 | maraa,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=maraa,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 279 | marawi,sd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=marawi,sd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 280 | marcona,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=marcona,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 281 | margate,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=margate,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 282 | marovoay,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=marovoay,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 283 | marsa matruh,eg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=marsa matruh,eg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 284 | marsh harbour,bs -- query_url: http://api.openweathermap.org/data/2.5/weather?q=marsh harbour,bs&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 285 | marzuq,ly -- query_url: http://api.openweathermap.org/data/2.5/weather?q=marzuq,ly&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 286 | masuguru,tz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=masuguru,tz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 287 | matara,lk -- query_url: http://api.openweathermap.org/data/2.5/weather?q=matara,lk&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 288 | matay,eg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=matay,eg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 289 | mayor pablo lagerenza,py -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mayor pablo lagerenza,py&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 290 | mazamari,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mazamari,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 291 | mecca,sa -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mecca,sa&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 292 | medina,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=medina,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 293 | mega,et -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mega,et&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 294 | megion,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=megion,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 295 | mehran,ir -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mehran,ir&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 296 | melfi,td -- query_url: http://api.openweathermap.org/data/2.5/weather?q=melfi,td&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 297 | middelkerke,be -- query_url: http://api.openweathermap.org/data/2.5/weather?q=middelkerke,be&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 298 | miraflores,co -- query_url: http://api.openweathermap.org/data/2.5/weather?q=miraflores,co&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 299 | misratah,ly -- query_url: http://api.openweathermap.org/data/2.5/weather?q=misratah,ly&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 300 | mitsamiouli,km -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mitsamiouli,km&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 301 | mizdah,ly -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mizdah,ly&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 302 | moba,cd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=moba,cd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 303 | mocajuba,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mocajuba,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 304 | mocuba,mz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mocuba,mz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 305 | mogadishu,so -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mogadishu,so&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 306 | molina,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=molina,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 307 | montepuez,mz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=montepuez,mz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 308 | moose factory,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=moose factory,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 309 | morganton,us -- query_url: http://api.openweathermap.org/data/2.5/weather?q=morganton,us&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 310 | mozarlandia,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mozarlandia,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 311 | mrirt,ma -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mrirt,ma&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 312 | mtinko,tz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mtinko,tz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 313 | muisne,ec -- query_url: http://api.openweathermap.org/data/2.5/weather?q=muisne,ec&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 314 | mutare,zw -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mutare,zw&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 315 | nahavand,ir -- query_url: http://api.openweathermap.org/data/2.5/weather?q=nahavand,ir&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 316 | namibe,ao -- query_url: http://api.openweathermap.org/data/2.5/weather?q=namibe,ao&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 317 | nangomba,tz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=nangomba,tz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 318 | nanortalik,gl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=nanortalik,gl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 319 | nantucket,us -- query_url: http://api.openweathermap.org/data/2.5/weather?q=nantucket,us&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 320 | narasannapeta,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=narasannapeta,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 321 | nardaran,az -- query_url: http://api.openweathermap.org/data/2.5/weather?q=nardaran,az&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 322 | narsaq,gl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=narsaq,gl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 323 | ndjole,ga -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ndjole,ga&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 324 | nebolchi,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=nebolchi,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 325 | necochea,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=necochea,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 326 | nikitinskiy,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=nikitinskiy,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 327 | nikolsk,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=nikolsk,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 328 | niksic,me -- query_url: http://api.openweathermap.org/data/2.5/weather?q=niksic,me&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 329 | nizwa,om -- query_url: http://api.openweathermap.org/data/2.5/weather?q=nizwa,om&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 330 | norrtalje,se -- query_url: http://api.openweathermap.org/data/2.5/weather?q=norrtalje,se&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 331 | nouadhibou,mr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=nouadhibou,mr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 332 | novo aripuana,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=novo aripuana,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 333 | novopokrovskaya,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=novopokrovskaya,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 334 | nueve de julio,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=nueve de julio,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 335 | okandja,ga -- query_url: http://api.openweathermap.org/data/2.5/weather?q=okandja,ga&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 336 | oksfjord,no -- query_url: http://api.openweathermap.org/data/2.5/weather?q=oksfjord,no&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 337 | olafsvik,is -- query_url: http://api.openweathermap.org/data/2.5/weather?q=olafsvik,is&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 338 | olinda,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=olinda,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 339 | oltu,tr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=oltu,tr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 340 | olyka,ua -- query_url: http://api.openweathermap.org/data/2.5/weather?q=olyka,ua&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 341 | omaruru,na -- query_url: http://api.openweathermap.org/data/2.5/weather?q=omaruru,na&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 342 | omboue,ga -- query_url: http://api.openweathermap.org/data/2.5/weather?q=omboue,ga&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 343 | oranjemund,na -- query_url: http://api.openweathermap.org/data/2.5/weather?q=oranjemund,na&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 344 | oranjestad,aw -- query_url: http://api.openweathermap.org/data/2.5/weather?q=oranjestad,aw&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 345 | ormara,pk -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ormara,pk&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 346 | ornskoldsvik,se -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ornskoldsvik,se&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 347 | oruro,bo -- query_url: http://api.openweathermap.org/data/2.5/weather?q=oruro,bo&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 348 | osorno,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=osorno,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 349 | ouro fino,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ouro fino,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 350 | padang,id -- query_url: http://api.openweathermap.org/data/2.5/weather?q=padang,id&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 351 | paita,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=paita,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 352 | pallasovka,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=pallasovka,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 353 | pangnirtung,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=pangnirtung,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 354 | pangoa,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=pangoa,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 355 | paraisopolis,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=paraisopolis,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 356 | parana,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=parana,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 357 | parrita,cr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=parrita,cr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 358 | paso de carrasco,uy -- query_url: http://api.openweathermap.org/data/2.5/weather?q=paso de carrasco,uy&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 359 | peci,ba -- query_url: http://api.openweathermap.org/data/2.5/weather?q=peci,ba&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 360 | pemba,mz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=pemba,mz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 361 | peniche,pt -- query_url: http://api.openweathermap.org/data/2.5/weather?q=peniche,pt&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 362 | piacabucu,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=piacabucu,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 363 | pimentel,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=pimentel,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 364 | pisco,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=pisco,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 365 | pitsunda,ge -- query_url: http://api.openweathermap.org/data/2.5/weather?q=pitsunda,ge&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    The key doesn't exist: pitsunda, ge.
    <class 'KeyError'>
    Row index: 366 | plettenberg bay,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=plettenberg bay,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 367 | ponta do sol,pt -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ponta do sol,pt&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 368 | ponta do sol,cv -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ponta do sol,cv&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 369 | porosozero,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=porosozero,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 370 | port alfred,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=port alfred,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 371 | port elizabeth,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=port elizabeth,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 372 | port-gentil,ga -- query_url: http://api.openweathermap.org/data/2.5/weather?q=port-gentil,ga&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 373 | porto nacional,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=porto nacional,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 374 | porto velho,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=porto velho,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 375 | porto walter,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=porto walter,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 376 | povenets,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=povenets,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 377 | pozo colorado,py -- query_url: http://api.openweathermap.org/data/2.5/weather?q=pozo colorado,py&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 378 | praia da vitoria,pt -- query_url: http://api.openweathermap.org/data/2.5/weather?q=praia da vitoria,pt&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 379 | puerto ayacucho,ve -- query_url: http://api.openweathermap.org/data/2.5/weather?q=puerto ayacucho,ve&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 380 | puerto leguizamo,co -- query_url: http://api.openweathermap.org/data/2.5/weather?q=puerto leguizamo,co&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 381 | puerto madryn,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=puerto madryn,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 382 | puerto quijarro,bo -- query_url: http://api.openweathermap.org/data/2.5/weather?q=puerto quijarro,bo&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 383 | punta arenas,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 384 | qaanaaq,gl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 385 | qafsah,tn -- query_url: http://api.openweathermap.org/data/2.5/weather?q=qafsah,tn&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 386 | qaqortoq,gl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=qaqortoq,gl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 387 | qasigiannguit,gl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=qasigiannguit,gl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 388 | quatre cocos,mu -- query_url: http://api.openweathermap.org/data/2.5/weather?q=quatre cocos,mu&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 389 | quelimane,mz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=quelimane,mz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 390 | racine,us -- query_url: http://api.openweathermap.org/data/2.5/weather?q=racine,us&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 391 | rawson,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=rawson,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 392 | requena,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=requena,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 393 | reyes,bo -- query_url: http://api.openweathermap.org/data/2.5/weather?q=reyes,bo&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 394 | ribeira grande,pt -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ribeira grande,pt&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 395 | richards bay,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=richards bay,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 396 | rio claro,tt -- query_url: http://api.openweathermap.org/data/2.5/weather?q=rio claro,tt&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 397 | rio gallegos,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=rio gallegos,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 398 | rio grande,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=rio grande,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 399 | rio sereno,pa -- query_url: http://api.openweathermap.org/data/2.5/weather?q=rio sereno,pa&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 400 | riohacha,co -- query_url: http://api.openweathermap.org/data/2.5/weather?q=riohacha,co&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 401 | riom,fr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=riom,fr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 402 | road town,vg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=road town,vg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 403 | roald,no -- query_url: http://api.openweathermap.org/data/2.5/weather?q=roald,no&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 404 | rocha,uy -- query_url: http://api.openweathermap.org/data/2.5/weather?q=rocha,uy&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 405 | rolim de moura,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=rolim de moura,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 406 | romanovskaya,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=romanovskaya,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 407 | rosario,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=rosario,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 408 | rundu,na -- query_url: http://api.openweathermap.org/data/2.5/weather?q=rundu,na&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 409 | rylsk,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=rylsk,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 410 | saint anthony,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=saint anthony,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 411 | saint george,bm -- query_url: http://api.openweathermap.org/data/2.5/weather?q=saint george,bm&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 412 | saint-augustin,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=saint-augustin,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 413 | saint-joseph,re -- query_url: http://api.openweathermap.org/data/2.5/weather?q=saint-joseph,re&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 414 | saint-philippe,re -- query_url: http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 415 | saint-pierre,re -- query_url: http://api.openweathermap.org/data/2.5/weather?q=saint-pierre,re&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 416 | saint-pierre,mq -- query_url: http://api.openweathermap.org/data/2.5/weather?q=saint-pierre,mq&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 417 | salalah,om -- query_url: http://api.openweathermap.org/data/2.5/weather?q=salalah,om&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 418 | saldanha,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=saldanha,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 419 | salinas,ec -- query_url: http://api.openweathermap.org/data/2.5/weather?q=salinas,ec&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 420 | salta,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=salta,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 421 | salto,uy -- query_url: http://api.openweathermap.org/data/2.5/weather?q=salto,uy&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 422 | sambava,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sambava,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 423 | san borja,bo -- query_url: http://api.openweathermap.org/data/2.5/weather?q=san borja,bo&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 424 | san carlos,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=san carlos,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 425 | san ignacio,bo -- query_url: http://api.openweathermap.org/data/2.5/weather?q=san ignacio,bo&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 426 | san lawrenz,mt -- query_url: http://api.openweathermap.org/data/2.5/weather?q=san lawrenz,mt&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 427 | san ramon,bo -- query_url: http://api.openweathermap.org/data/2.5/weather?q=san ramon,bo&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 428 | san-pedro,ci -- query_url: http://api.openweathermap.org/data/2.5/weather?q=san-pedro,ci&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 429 | santa cruz,cr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=santa cruz,cr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 430 | santa fe do sul,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=santa fe do sul,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 431 | santa helena de goias,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=santa helena de goias,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 432 | santa maria,pa -- query_url: http://api.openweathermap.org/data/2.5/weather?q=santa maria,pa&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 433 | santa rosa,bo -- query_url: http://api.openweathermap.org/data/2.5/weather?q=santa rosa,bo&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 434 | santa rosa,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=santa rosa,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 435 | santana do livramento,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=santana do livramento,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 436 | sao filipe,cv -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sao filipe,cv&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 437 | sao gabriel da cachoeira,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sao gabriel da cachoeira,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 438 | sao joao da barra,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sao joao da barra,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 439 | sao jose do belmonte,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sao jose do belmonte,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 440 | sao paulo de olivenca,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sao paulo de olivenca,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 441 | sechura,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sechura,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 442 | sembabule,ug -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sembabule,ug&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 443 | senador pompeu,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=senador pompeu,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 444 | senneterre,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=senneterre,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 445 | seoni malwa,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=seoni malwa,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 446 | shalakusha,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=shalakusha,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 447 | sharjah,ae -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sharjah,ae&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 448 | shelui,tz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=shelui,tz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 449 | siavonga,zm -- query_url: http://api.openweathermap.org/data/2.5/weather?q=siavonga,zm&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 450 | sidrolandia,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sidrolandia,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 451 | sinkat,sd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sinkat,sd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 452 | sinnamary,gf -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sinnamary,gf&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 453 | sipoo,fi -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sipoo,fi&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 454 | sisimiut,gl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sisimiut,gl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 455 | skibbereen,ie -- query_url: http://api.openweathermap.org/data/2.5/weather?q=skibbereen,ie&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 456 | sol-iletsk,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sol-iletsk,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 457 | somerset east,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=somerset east,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 458 | sorland,no -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sorland,no&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 459 | sorvag,fo -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sorvag,fo&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 460 | sosnovka,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sosnovka,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 461 | souillac,mu -- query_url: http://api.openweathermap.org/data/2.5/weather?q=souillac,mu&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 462 | soyo,ao -- query_url: http://api.openweathermap.org/data/2.5/weather?q=soyo,ao&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 463 | strai,no -- query_url: http://api.openweathermap.org/data/2.5/weather?q=strai,no&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 464 | suleja,ng -- query_url: http://api.openweathermap.org/data/2.5/weather?q=suleja,ng&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 465 | sumbe,ao -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sumbe,ao&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 466 | svetlyy,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=svetlyy,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 467 | takaungu,ke -- query_url: http://api.openweathermap.org/data/2.5/weather?q=takaungu,ke&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 468 | talah,tn -- query_url: http://api.openweathermap.org/data/2.5/weather?q=talah,tn&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 469 | talara,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=talara,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 470 | talcahuano,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=talcahuano,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 471 | talnakh,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=talnakh,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 472 | taltal,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=taltal,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 473 | tandalti,sd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tandalti,sd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 474 | tanout,ne -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tanout,ne&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 475 | taolanaro,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=taolanaro,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 476 | taoudenni,ml -- query_url: http://api.openweathermap.org/data/2.5/weather?q=taoudenni,ml&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 477 | taraz,kz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=taraz,kz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 478 | tasiilaq,gl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 479 | tearce,mk -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tearce,mk&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 480 | teguldet,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=teguldet,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 481 | terrak,no -- query_url: http://api.openweathermap.org/data/2.5/weather?q=terrak,no&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 482 | teruel,es -- query_url: http://api.openweathermap.org/data/2.5/weather?q=teruel,es&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 483 | tessalit,ml -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tessalit,ml&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 484 | thaba-tseka,ls -- query_url: http://api.openweathermap.org/data/2.5/weather?q=thaba-tseka,ls&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 485 | thinadhoo,mv -- query_url: http://api.openweathermap.org/data/2.5/weather?q=thinadhoo,mv&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 486 | thompson,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=thompson,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 487 | tikrit,iq -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tikrit,iq&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 488 | tocopilla,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tocopilla,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 489 | toliary,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=toliary,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 490 | tomaszow lubelski,pl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tomaszow lubelski,pl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 491 | tonj,sd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tonj,sd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 492 | torbay,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=torbay,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 493 | touros,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=touros,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 494 | trinec,cz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=trinec,cz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 495 | tsaratanana,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tsaratanana,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 496 | tsihombe,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tsihombe,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 497 | tsiroanomandidy,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tsiroanomandidy,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 498 | tucano,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tucano,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 499 | tucurui,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tucurui,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 500 | tuggurt,dz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tuggurt,dz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 501 | tumannyy,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tumannyy,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 502 | turayf,sa -- query_url: http://api.openweathermap.org/data/2.5/weather?q=turayf,sa&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 503 | turukhansk,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=turukhansk,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 504 | tutoia,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tutoia,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 505 | umm ruwabah,sd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=umm ruwabah,sd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 506 | umzimvubu,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=umzimvubu,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 507 | unnao,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=unnao,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 508 | upernavik,gl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 509 | urengoy,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=urengoy,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 510 | ushuaia,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 511 | vagur,fo -- query_url: http://api.openweathermap.org/data/2.5/weather?q=vagur,fo&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 512 | valdivia,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=valdivia,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 513 | vallenar,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=vallenar,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 514 | vardo,no -- query_url: http://api.openweathermap.org/data/2.5/weather?q=vardo,no&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 515 | vastervik,se -- query_url: http://api.openweathermap.org/data/2.5/weather?q=vastervik,se&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 516 | velizh,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=velizh,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 517 | victoria,sc -- query_url: http://api.openweathermap.org/data/2.5/weather?q=victoria,sc&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 518 | victoria,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=victoria,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 519 | vicuna,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=vicuna,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 520 | viedma,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=viedma,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 521 | vila velha,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=vila velha,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 522 | vilnius,lt -- query_url: http://api.openweathermap.org/data/2.5/weather?q=vilnius,lt&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 523 | vredendal,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=vredendal,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 524 | wajir,ke -- query_url: http://api.openweathermap.org/data/2.5/weather?q=wajir,ke&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 525 | walvis bay,na -- query_url: http://api.openweathermap.org/data/2.5/weather?q=walvis bay,na&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 526 | wattegama,lk -- query_url: http://api.openweathermap.org/data/2.5/weather?q=wattegama,lk&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 527 | waupun,us -- query_url: http://api.openweathermap.org/data/2.5/weather?q=waupun,us&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 528 | willowmore,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=willowmore,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 529 | wundanyi,ke -- query_url: http://api.openweathermap.org/data/2.5/weather?q=wundanyi,ke&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 530 | xai-xai,mz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=xai-xai,mz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 531 | xique-xique,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=xique-xique,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 532 | yambio,sd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=yambio,sd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 533 | yanam,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=yanam,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 534 | yar-sale,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=yar-sale,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 535 | yining,cn -- query_url: http://api.openweathermap.org/data/2.5/weather?q=yining,cn&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 536 | zemio,cf -- query_url: http://api.openweathermap.org/data/2.5/weather?q=zemio,cf&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Total errors:  2
    




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
      <th>country</th>
      <th>date</th>
      <th>lat</th>
      <th>lng</th>
      <th>max_temperature</th>
      <th>humidity</th>
      <th>cloudiness</th>
      <th>wind_speed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>abha</td>
      <td>sa</td>
      <td>2017-08-23 05:00:00</td>
      <td>42.51</td>
      <td>18.22</td>
      <td>89.60</td>
      <td>58.0</td>
      <td>75.0</td>
      <td>9.17</td>
    </tr>
    <tr>
      <th>1</th>
      <td>acarau</td>
      <td>br</td>
      <td>2017-08-23 05:32:32</td>
      <td>-40.12</td>
      <td>-2.89</td>
      <td>85.05</td>
      <td>57.0</td>
      <td>8.0</td>
      <td>18.45</td>
    </tr>
    <tr>
      <th>2</th>
      <td>agirish</td>
      <td>ru</td>
      <td>2017-08-23 05:32:32</td>
      <td>63.02</td>
      <td>61.92</td>
      <td>73.17</td>
      <td>83.0</td>
      <td>24.0</td>
      <td>6.93</td>
    </tr>
    <tr>
      <th>3</th>
      <td>aksu</td>
      <td>kz</td>
      <td>2017-08-23 05:00:00</td>
      <td>69.83</td>
      <td>42.42</td>
      <td>89.60</td>
      <td>17.0</td>
      <td>0.0</td>
      <td>15.66</td>
    </tr>
    <tr>
      <th>4</th>
      <td>aksu</td>
      <td>cn</td>
      <td>2017-08-23 05:32:32</td>
      <td>80.26</td>
      <td>41.12</td>
      <td>54.45</td>
      <td>100.0</td>
      <td>88.0</td>
      <td>4.70</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Save Data to csv
# For data analysis: Export file without index, with header
city_wdf.to_csv("world_cities_weather_hw5.csv", index=False, header=True)
```


```python
# Scatter plot Latitude - Temperature:
# 
# The biggest information that jumps out at me is the concentration
# of cities in the moderate temperature zone.  The cities are concentrated
# in the 60 - 80 degree range with fewer as you move upwards or downwards 
# in temperature.  It would be nice to be able to hover over the circles and
# see more information.  Hidden city information would be helpful but not 
# distracting from the chart.
```


```python
# # https://seaborn.pydata.org/generated/seaborn.regplot.html
# import seaborn as sns; sns.set(color_codes=True)

import seaborn as sns

# Set my default color palette
mycolors = ["magenta", "blue", "red", "green", "cyan", "coral", "skyblue", "gold"]
sns.set_palette(mycolors)

# Add current date to the title
cdate = datetime.now().strftime("(%m/%d/%Y)")

x_axis = city_wdf["lat"]
y_axis = city_wdf["max_temperature"]


sns.regplot(x=x_axis, y=y_axis, color="magenta", marker="o", fit_reg=False, 
            scatter_kws={"s":80, "linewidths":1, "edgecolor":"k"})

sns.set_style("darkgrid")
sns.plt.title("City Latitude vs Temperature %s" % (cdate), weight='bold').set_fontsize('16')
sns.plt.xlabel("Latitude", weight='bold').set_fontsize('14')
sns.plt.ylabel("Max Temperature (F)", weight='bold',).set_fontsize('14')

plt.savefig("lat_temp_scatter.png",bbox_inches="tight")
plt.show()
```


![png](PyWeather_hw5-submit_files/PyWeather_hw5-submit_10_0.png)



```python
# Scatter plot Latitude - Humidity:
# 
# The humidity chart reveals something I don't often remember, being
# from California most of my life, but having experienced east coast 
# humidity, there is a percentage of humidity in all the cities.  That
# tells me that humidity doesn't have to be connected to sticky yucky
# weather.  Humidity doesn't seem to impact the bilding of cities as
# they are spread out relatively well with some concentrations.
```


```python
# https://seaborn.pydata.org/generated/seaborn.regplot.html
# import seaborn as sns; sns.set(color_codes=True)

import seaborn as sns

# Set my default color palette
mycolors = ["magenta", "blue", "red", "green", "cyan", "coral", "skyblue", "gold"]
sns.set_palette(mycolors)


x_axis = city_wdf["lat"]
y_axis = city_wdf["humidity"]

# Add current date to the title
cdate = datetime.now().strftime("(%m/%d/%Y)")

sns.regplot(x=x_axis, y=y_axis, color="cyan", marker="o", fit_reg=False, 
            scatter_kws={"s":80, "linewidths":1, "edgecolor":"k"})

sns.set_style("darkgrid")
sns.plt.title("City Latitude vs Humidity %s" % (cdate), weight='bold').set_fontsize('16')
sns.plt.xlabel("Latitude", weight='bold').set_fontsize('14')
sns.plt.ylabel("Humidity (%)", weight='bold',).set_fontsize('14')

plt.savefig("lat_humidity_scatter.png",bbox_inches="tight")
plt.show()
```


![png](PyWeather_hw5-submit_files/PyWeather_hw5-submit_12_0.png)



```python
# Scatter plot Latitude - Cloudiness:
# 
# I think this is the least informative chart of the group.  I can tell it
# is cloudy in a lot of cities to some degree, and there are a number of 
# cities with no clouds.
```


```python
# # https://seaborn.pydata.org/generated/seaborn.regplot.html
# import seaborn as sns; sns.set(color_codes=True)

import seaborn as sns


# Set my default color palette
mycolors = ["magenta", "blue", "red", "green", "cyan", "coral", "skyblue", "gold"]
sns.set_palette(mycolors)

x_axis = city_wdf["lat"]
y_axis = city_wdf["cloudiness"]

# Add current date to the title
cdate = datetime.now().strftime("(%m/%d/%Y)")

sns.regplot(x=x_axis, y=y_axis, color="gold", marker="o", fit_reg=False, 
            scatter_kws={"s":80, "linewidths":1, "edgecolor":"k"})

sns.set_style("darkgrid")
sns.plt.title("City Latitude vs Cloudiness %s" % (cdate), weight='bold').set_fontsize('16')
sns.plt.xlabel("Latitude", weight='bold').set_fontsize('14')
sns.plt.ylabel("Cloudiness (%)", weight='bold',).set_fontsize('14')

plt.savefig("lat_cloudiness_scatter.png",bbox_inches="tight")
plt.show()
```


![png](PyWeather_hw5-submit_files/PyWeather_hw5-submit_14_0.png)



```python
# Scatter plot Latitude - Wind:
# 
# The latidtude wind chart doesn't hold any surprises for me.  In my
# area, wind up 16 mph is normal with higher gusts at higher elevations.
# Above 25 mph is getting more uncomfortable especially if the wind
# speed is sustained for hours or days.  Our weather window is narrow
# so we can't tell much besides the majority of cities in our population
# are having a normal range of wind speed for the forcast.
```


```python
# https://seaborn.pydata.org/generated/seaborn.regplot.html
# import seaborn as sns; sns.set(color_codes=True)

import seaborn as sns

# Set my default color palette
mycolors = ["magenta", "blue", "red", "green", "cyan", "coral", "skyblue", "gold"]
sns.set_palette(mycolors)

x_axis = city_wdf["lat"]
y_axis = city_wdf["wind_speed"]

# Add current date to the title
cdate = datetime.now().strftime("(%m/%d/%Y)")

sns.regplot(x=x_axis, y=y_axis, color="red", marker="o", fit_reg=False, 
            scatter_kws={"s":80, "linewidths":1, "edgecolor":"k"})

sns.set_style("darkgrid")
sns.plt.title("City Latitude vs Wind Speed %s" % (cdate), weight='bold').set_fontsize('16')
sns.plt.xlabel("Latitude", weight='bold').set_fontsize('14')
sns.plt.ylabel("Max Speed (mph)", weight='bold',).set_fontsize('14')

plt.savefig("lat_windmph_scatter.png",bbox_inches="tight")
plt.show()
```


![png](PyWeather_hw5-submit_files/PyWeather_hw5-submit_16_0.png)



```python
# Create a markdown file of the Jupyter Notebook
```
