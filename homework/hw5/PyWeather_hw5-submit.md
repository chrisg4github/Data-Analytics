

```python
##Dependencies
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
# gkey="AIzaSyBxoHPgXoiBQ1TuPrFX7JjBatqNud9gems"

# Created my api key for openweathermap.org/api   key name = myOWM
# Used my comcast email id and chrisg4owm
api_owmkey = "b28cc4b4c0a1d1d9ff4c2d9e808f9a5a"

# Created 2nd api key for openweathermap.org/api   key name = OWM1
# Used my gmail id and chrisg4owm2
# api_owmkey = "694332937bad44a33dd12de17c5e78e8"  

# Created 2nd api key for openweathermap.org/api   key name = OWM2
# Used my gmail id and chrisg4owm2
# api_owmkey = "44db84fb592301e3b8e80fd68c27e847"  
```


```python
##Background Information on Latitude and Longitude:

# Latitudes-
# In geography, latitude is a geographic coordinate that specifies 
# the north–south position of a point on the Earth's surface. 
# Latitude is an angle (defined below) which ranges from 0° at the 
# Equator to 90° (North or South) at the poles.

# While lines of latitude run across a map east-west, the point of 
# latitude makes the n0rth-south position of a point on earth.  
# Lines of latitude start at 0 degrees at the equator and end a 90 
# degrees at the North and South Poles.  Everything north of the 
# equator is known as the Northern Hemisphere and everything south 
# of the equator is known as the Southern Hemisphere.

# Lines of latitude are called parallels and in total there are 180 
# degrees of latitude.  The distance between each degree of 
# latitude is about 69 miles (110 kilometers).  The five major 
# parallels of latitudes from north to south are called: Arctic 
# Circle, Tropic of Cancer, Equator, Tropic of Capricorn, and the 
# Antarctic Circle. On a maps where the orientation of the map is 
# either due north or due south, latitude appears as horizontal lines.

# Longitude-
# Longitude is the measurement east or west of the prime meridian. 
# Longitude is measured by imaginary lines that run around the Earth 
# vertically (up and down) and meet at the North and South Poles. 
# These lines are known as meridians.

# Longitude lines run north-south and mark the position east-west of 
# a point. Lines of longitude are known as meridians.  These lines run 
# from pole to pole, crossing the equator at right angles. There are 
# 360 degrees of latitude and the latitude line of 0 degrees is known 
# as the Prime Meridian and it divides the world into the Eastern 
# Hemisphere and the Western Hemisphere (-180 degrees degrees of 
# longitude west and 180 degrees of longitude east).

# The distance between longitudes narrows the further away from the 
# equator.  The distance between longitudes at the equator is the same 
# as latitude, roughly 69 miles. At 45 degrees north or south, the 
# distance between is about 49 miles (79 km). The distance between 
# longitudes reaches zero at the poles as the lines of meridian 
# converge at that point.

# The Prime Meridian is at 0 degrees longitude, just as the equator is at 
# 0 degrees latitude

```


```python
##Weather Plot Trend Analysis 

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

# Data Trend Analysis:
# I think the charts would have been more informative with longitude as the 
# y-axis and the choosen y-axis (temperature in this case) as a third 
# variable.  This would make a better picture of the distribution because I
# could tell where the city was on the line of longitude.  

# So, with temperature as the y-axis, I can tell where a city lies in terms
# of latitude in relation to the prime meridian which allows me to make some
# assumptions because I know the continents and where the prime meridian
# cuts across the continents.  From this I would say the trend shows that 
# cities are concentrated in areas of moderate climate.  Cities avoid the 
# extreme cold of the north and south poles, there are fewer cities in areas
# above 80 degrees and below 60 degrees fahrenheit.  If I look at the wind, 
# humidity, and temperature together, I think they confirm the clustering 
# trend of cities and therefore the most people in moderate climate areas.

# I found the cloudiness chart interesting, but the least informative of the 
# four charts.  While there was a good concentration of cities with 0% 
# cloudiness, it was cloudy in a lot of cities to some degree which is good 
# because clouds are necessary for rain and water is necessary for life.  So
# it is difficult to decipher a trend other than there are more cities with
# cloudy weather than there are with no clouds at all.  I think I also 
# learned from this exercise that one or two more variables could make a big
# difference in what information could be conveyed.

# The biggest take-away was that it was difficult to draw conclusions, pictures,
# or trends using current data. Also, this wasn't really interesting, gripping 
# or extreme data.  It was the daily weather report for 500+ cities.

# If I look at the humidity and wind speed charts I get two pieces of information.
# One was that humidity is more widespread than I thought because I have this 
# mistaken idea that if humidity isn't sticky and yucky then it doesn't exist.
# That's wrong, so I thought the humidity chart was useful and conveyed valid
# and important information.  And two, the wind speed chart confirmed weather 
# information consistent with my area which is that winds up to 20 mph are normal
# and occur for a large number of cities.  There are fewer cities experiencing wind
# speeds above 20 mph.  Higher gusts can occur, like at higher elevations, but 
# these are usually mentioned as outliers not as the wind speed for the area.

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
##Divide the earth into quadrants- see image http://i37.tinypic.com/345izb4.jpg

##                    Latitude = x      Longitude = y            
##                   ----------------  ---------------   
## Quad4-far west  = (-180.0 | -90.0)  (-90.0 | 90.0)
## Quad3-near west =  (-90.0 | 0.0)    (-90.0 | 90.0)
## Quad2-near east =  (0.0   |  90.0)  (-90.0 | 90.0)
## Quad1-far east  =  (90.0  | 180.0)  (-90.0 | 90.0)
```


```python
## Generate a list of 500+ unique cities from all around the earth.
## Divide the earth into quadrants.  See http://i37.tinypic.com/345izb4.jpg
##
##-----------------------------------------------------------------------
##--- Declare Variables

# Set to True for print statements
Debug = False

list_length = 275

# final data frame that's empty
city_wdf = pd.DataFrame() 
city_wdf["city"] = ""
city_wdf["country"] = ""

# used for loading geo coordinates 
load_count = 0   
# max number of iterations per quadrant
clean_count = 0  

# list of latitude range tuples Far West to Far East
quad_lat = [(-180,-90), (-90,0), (0,90), (90,180)]

# ----------------------------------------------------------------------

#Loop thru latitude tuples
for a in quad_lat:
    # working data frame that's empty
    city_tmp = pd.DataFrame()
    city_tmp["city"] = ""
    city_tmp["country"] = ""
    
    # prevents infinite loop
    clean_count = 0
    # used to set the index for city_tmp
    counter = 0      
    
    # Pass these tuple values into while loop
    b,c = a[0], a[1]
    print("Current tuple ", a)
    print("b = " + str(b) + " c = " + str(c))
    print("Pass b, c to while loop...")
    
    while len(city_tmp.index)<= list_length:
        
        geo_list = [] 
        load_count = counter
        if Debug:
            print("Length city_tmp ", len(city_tmp.index))
            print("counter is ", counter)
            print("load_count is ", load_count)
        
        # Append tuples of coordinates to the geo_list
        while load_count <= list_length:
            tup = ()
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
    281
    Current tuple  (0, 90)
    b = 0 c = 90
    Pass b, c to while loop...
    556
    Current tuple  (90, 180)
    b = 90 c = 180
    Pass b, c to while loop...
    567
    


```python
##Final clean up of the city data frame
##Sort the data by city, country
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

print(len(city_wdf.index))
city_wdf.head(10)
```

    567
    541
    




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
      <td>abeche</td>
      <td>td</td>
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
      <td>abu samrah</td>
      <td>qa</td>
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
      <td>acari</td>
      <td>pe</td>
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
      <td>adjumani</td>
      <td>ug</td>
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
      <td>agadir</td>
      <td>ma</td>
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
      <td>aguimes</td>
      <td>es</td>
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
      <td>akdepe</td>
      <td>tm</td>
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
      <th>8</th>
      <td>alakurtti</td>
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
      <th>9</th>
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
  </tbody>
</table>
</div>




```python
## Make OpenWeatherMap api calls.  
## http://openweathermap.org/api  - this has the API documentation
##
## API call: 
## api.openweathermap.org/data/2.5/weather?q={city},{country}&unit={unit}&APPID={key} 
## city name and country code divided by comma, (use ISO 3166 country codes)
##
## API example: city = aasiaat country = gl
## http://api.openweathermap.org/data/2.5/weather?q=aasiaat,gl&units=imperial&APPID=key
## Or
## http://api.openweathermap.org/data/2.5/weather?appid=key&q=aasiaat,gl&units=imperial

import json
import requests as req

## Created my api key for openweathermap.org/api key
# api_owmkey = "b28cc4b4c0a1d1d9ff4c2d9e808f9a5a"
# api_owmkey = "694332937bad44a33dd12de17c5e78e8"
# api_owmkey = "44db84fb592301e3b8e80fd68c27e847"  

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
        #print("The weather API responded with: " + json.dumps(city_weather, indent=2) + ".")
        print("Row index: " + str(index) + " | " + row["city"] + "," + row["country"] +
              " -- query_url: " + query_url)
        
        # OWM dt (date) = Time of data load, GMT Unix timestamp (UTC) 
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

    Row index: 0 | abeche,td -- query_url: http://api.openweathermap.org/data/2.5/weather?q=abeche,td&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 1 | abu samrah,qa -- query_url: http://api.openweathermap.org/data/2.5/weather?q=abu samrah,qa&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 2 | acari,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=acari,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 3 | adjumani,ug -- query_url: http://api.openweathermap.org/data/2.5/weather?q=adjumani,ug&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 4 | agadir,ma -- query_url: http://api.openweathermap.org/data/2.5/weather?q=agadir,ma&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 5 | aguimes,es -- query_url: http://api.openweathermap.org/data/2.5/weather?q=aguimes,es&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 6 | akdepe,tm -- query_url: http://api.openweathermap.org/data/2.5/weather?q=akdepe,tm&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 7 | aksu,cn -- query_url: http://api.openweathermap.org/data/2.5/weather?q=aksu,cn&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 8 | alakurtti,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=alakurtti,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 9 | albany,au -- query_url: http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 10 | albert town,jm -- query_url: http://api.openweathermap.org/data/2.5/weather?q=albert town,jm&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 11 | alcaniz,es -- query_url: http://api.openweathermap.org/data/2.5/weather?q=alcaniz,es&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 12 | alenquer,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=alenquer,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 13 | alexandria,eg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=alexandria,eg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 14 | alpena,us -- query_url: http://api.openweathermap.org/data/2.5/weather?q=alpena,us&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 15 | alta floresta,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=alta floresta,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 16 | altay,cn -- query_url: http://api.openweathermap.org/data/2.5/weather?q=altay,cn&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 17 | alto araguaia,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=alto araguaia,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 18 | alvaraes,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=alvaraes,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 19 | amapa,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=amapa,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 20 | ambilobe,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ambilobe,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 21 | amderma,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=amderma,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 22 | ampanihy,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ampanihy,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 23 | ancud,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ancud,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 24 | andapa,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=andapa,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 25 | antofagasta,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=antofagasta,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 26 | anzio,it -- query_url: http://api.openweathermap.org/data/2.5/weather?q=anzio,it&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 27 | aquin,ht -- query_url: http://api.openweathermap.org/data/2.5/weather?q=aquin,ht&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 28 | araouane,ml -- query_url: http://api.openweathermap.org/data/2.5/weather?q=araouane,ml&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 29 | aripuana,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=aripuana,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 30 | arlit,ne -- query_url: http://api.openweathermap.org/data/2.5/weather?q=arlit,ne&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 31 | arraial do cabo,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=arraial do cabo,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 32 | artigas,uy -- query_url: http://api.openweathermap.org/data/2.5/weather?q=artigas,uy&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 33 | asmar,af -- query_url: http://api.openweathermap.org/data/2.5/weather?q=asmar,af&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 34 | atar,mr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=atar,mr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 35 | attawapiskat,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=attawapiskat,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 36 | avanigadda,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=avanigadda,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 37 | awbari,ly -- query_url: http://api.openweathermap.org/data/2.5/weather?q=awbari,ly&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 38 | axim,gh -- query_url: http://api.openweathermap.org/data/2.5/weather?q=axim,gh&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 39 | balkhash,kz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=balkhash,kz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 40 | bambous virieux,mu -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bambous virieux,mu&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 41 | banda aceh,id -- query_url: http://api.openweathermap.org/data/2.5/weather?q=banda aceh,id&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 42 | bara,sd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bara,sd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 43 | barbar,sd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=barbar,sd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 44 | barcelos,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=barcelos,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 45 | bareli,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bareli,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 46 | barentsburg,sj -- query_url: http://api.openweathermap.org/data/2.5/weather?q=barentsburg,sj&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    The key doesn't exist: barentsburg, sj.
    <class 'KeyError'>
    Row index: 47 | bargal,so -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bargal,so&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 48 | barra,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=barra,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 49 | barra dos coqueiros,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=barra dos coqueiros,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 50 | batangafo,cf -- query_url: http://api.openweathermap.org/data/2.5/weather?q=batangafo,cf&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 51 | bathsheba,bb -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bathsheba,bb&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 52 | beberibe,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=beberibe,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 53 | beitbridge,zw -- query_url: http://api.openweathermap.org/data/2.5/weather?q=beitbridge,zw&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 54 | belmonte,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=belmonte,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 55 | beloha,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=beloha,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 56 | belousovka,kz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=belousovka,kz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 57 | belushya guba,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=belushya guba,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 58 | bengkulu,id -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bengkulu,id&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 59 | bereda,so -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bereda,so&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 60 | berezna,ua -- query_url: http://api.openweathermap.org/data/2.5/weather?q=berezna,ua&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 61 | berlevag,no -- query_url: http://api.openweathermap.org/data/2.5/weather?q=berlevag,no&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 62 | beyneu,kz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=beyneu,kz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 63 | bilma,ne -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bilma,ne&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 64 | biograd na moru,hr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=biograd na moru,hr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 65 | birao,cf -- query_url: http://api.openweathermap.org/data/2.5/weather?q=birao,cf&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 66 | biu,ng -- query_url: http://api.openweathermap.org/data/2.5/weather?q=biu,ng&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 67 | blagoyevo,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=blagoyevo,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 68 | bloemfontein,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bloemfontein,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 69 | boali,cf -- query_url: http://api.openweathermap.org/data/2.5/weather?q=boali,cf&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 70 | boende,cd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=boende,cd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 71 | bokspits,bw -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bokspits,bw&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 72 | bolama,gw -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bolama,gw&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 73 | bolshegrivskoye,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bolshegrivskoye,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 74 | bolungarvik,is -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bolungarvik,is&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 75 | bonavista,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bonavista,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 76 | botro,ci -- query_url: http://api.openweathermap.org/data/2.5/weather?q=botro,ci&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 77 | bouar,cf -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bouar,cf&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 78 | boueni,yt -- query_url: http://api.openweathermap.org/data/2.5/weather?q=boueni,yt&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 79 | bourbonnais,us -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bourbonnais,us&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 80 | bousse,bf -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bousse,bf&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 81 | braniewo,pl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=braniewo,pl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 82 | bredasdorp,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 83 | bubaque,gw -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bubaque,gw&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 84 | bud,no -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bud,no&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 85 | bur gabo,so -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bur gabo,so&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 86 | burgersdorp,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=burgersdorp,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 87 | buritis,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=buritis,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 88 | busselton,au -- query_url: http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 89 | butterworth,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=butterworth,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 90 | cabedelo,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=cabedelo,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 91 | caico,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=caico,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 92 | camacupa,ao -- query_url: http://api.openweathermap.org/data/2.5/weather?q=camacupa,ao&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 93 | camopi,gf -- query_url: http://api.openweathermap.org/data/2.5/weather?q=camopi,gf&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 94 | campoverde,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=campoverde,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 95 | canete,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=canete,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 96 | cantanhede,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=cantanhede,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 97 | cape town,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 98 | carauari,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=carauari,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 99 | caravelas,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=caravelas,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 100 | carnarvon,au -- query_url: http://api.openweathermap.org/data/2.5/weather?q=carnarvon,au&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 101 | casablanca,ma -- query_url: http://api.openweathermap.org/data/2.5/weather?q=casablanca,ma&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 102 | castro,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=castro,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 103 | catamarca,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=catamarca,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 104 | cayenne,gf -- query_url: http://api.openweathermap.org/data/2.5/weather?q=cayenne,gf&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 105 | celendin,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=celendin,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 106 | cestas,fr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=cestas,fr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 107 | chakia,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=chakia,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 108 | chala,tz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=chala,tz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 109 | chapais,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=chapais,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 110 | chicama,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=chicama,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 111 | chililabombwe,zm -- query_url: http://api.openweathermap.org/data/2.5/weather?q=chililabombwe,zm&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 112 | chiredzi,zw -- query_url: http://api.openweathermap.org/data/2.5/weather?q=chiredzi,zw&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 113 | chlorakas,cy -- query_url: http://api.openweathermap.org/data/2.5/weather?q=chlorakas,cy&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 114 | chuy,uy -- query_url: http://api.openweathermap.org/data/2.5/weather?q=chuy,uy&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 115 | cidreira,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=cidreira,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 116 | ciudad bolivar,ve -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ciudad bolivar,ve&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 117 | clonakilty,ie -- query_url: http://api.openweathermap.org/data/2.5/weather?q=clonakilty,ie&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 118 | clyde river,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=clyde river,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 119 | coari,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=coari,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 120 | codrington,ag -- query_url: http://api.openweathermap.org/data/2.5/weather?q=codrington,ag&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 121 | coihaique,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=coihaique,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 122 | colares,pt -- query_url: http://api.openweathermap.org/data/2.5/weather?q=colares,pt&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 123 | conceicao do araguaia,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=conceicao do araguaia,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 124 | conde,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=conde,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 125 | constitucion,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=constitucion,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 126 | contamana,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=contamana,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 127 | coquimbo,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=coquimbo,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 128 | cururupu,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=cururupu,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 129 | de aar,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=de aar,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 130 | deer lake,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=deer lake,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 131 | destin,us -- query_url: http://api.openweathermap.org/data/2.5/weather?q=destin,us&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 132 | diego de almagro,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=diego de almagro,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 133 | dikson,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=dikson,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 134 | dingle,ie -- query_url: http://api.openweathermap.org/data/2.5/weather?q=dingle,ie&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 135 | dolbeau,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=dolbeau,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 136 | dori,bf -- query_url: http://api.openweathermap.org/data/2.5/weather?q=dori,bf&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 137 | dunda,tz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=dunda,tz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 138 | dwarka,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=dwarka,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 139 | dzaoudzi,yt -- query_url: http://api.openweathermap.org/data/2.5/weather?q=dzaoudzi,yt&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 140 | east london,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=east london,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 141 | edd,er -- query_url: http://api.openweathermap.org/data/2.5/weather?q=edd,er&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 142 | el badari,eg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=el badari,eg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 143 | eregli,tr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=eregli,tr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 144 | eskasem,af -- query_url: http://api.openweathermap.org/data/2.5/weather?q=eskasem,af&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 145 | esna,eg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=esna,eg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 146 | faya,td -- query_url: http://api.openweathermap.org/data/2.5/weather?q=faya,td&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 147 | filadelfia,py -- query_url: http://api.openweathermap.org/data/2.5/weather?q=filadelfia,py&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 148 | florianopolis,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=florianopolis,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 149 | frutal,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=frutal,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 150 | fuerte olimpo,py -- query_url: http://api.openweathermap.org/data/2.5/weather?q=fuerte olimpo,py&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 151 | gamarra,co -- query_url: http://api.openweathermap.org/data/2.5/weather?q=gamarra,co&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 152 | gamba,ga -- query_url: http://api.openweathermap.org/data/2.5/weather?q=gamba,ga&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 153 | garissa,ke -- query_url: http://api.openweathermap.org/data/2.5/weather?q=garissa,ke&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 154 | gashua,ng -- query_url: http://api.openweathermap.org/data/2.5/weather?q=gashua,ng&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 155 | gat,ly -- query_url: http://api.openweathermap.org/data/2.5/weather?q=gat,ly&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 156 | gazli,uz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=gazli,uz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 157 | general elizardo aquino,py -- query_url: http://api.openweathermap.org/data/2.5/weather?q=general elizardo aquino,py&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 158 | georgetown,sh -- query_url: http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 159 | georgetown,gy -- query_url: http://api.openweathermap.org/data/2.5/weather?q=georgetown,gy&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 160 | geraldton,au -- query_url: http://api.openweathermap.org/data/2.5/weather?q=geraldton,au&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 161 | ghanzi,bw -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ghanzi,bw&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 162 | gizycko,pl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=gizycko,pl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 163 | gobabis,na -- query_url: http://api.openweathermap.org/data/2.5/weather?q=gobabis,na&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 164 | goderich,sl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=goderich,sl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 165 | goma,cd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=goma,cd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 166 | gore,et -- query_url: http://api.openweathermap.org/data/2.5/weather?q=gore,et&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 167 | grahamstown,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=grahamstown,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 168 | grand gaube,mu -- query_url: http://api.openweathermap.org/data/2.5/weather?q=grand gaube,mu&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 169 | grand river south east,mu -- query_url: http://api.openweathermap.org/data/2.5/weather?q=grand river south east,mu&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 170 | grand-santi,gf -- query_url: http://api.openweathermap.org/data/2.5/weather?q=grand-santi,gf&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 171 | grindavik,is -- query_url: http://api.openweathermap.org/data/2.5/weather?q=grindavik,is&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 172 | groningen,sr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=groningen,sr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 173 | grootfontein,na -- query_url: http://api.openweathermap.org/data/2.5/weather?q=grootfontein,na&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 174 | guane,cu -- query_url: http://api.openweathermap.org/data/2.5/weather?q=guane,cu&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 175 | guarapari,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=guarapari,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 176 | gweta,bw -- query_url: http://api.openweathermap.org/data/2.5/weather?q=gweta,bw&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 177 | halifax,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=halifax,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 178 | hambantota,lk -- query_url: http://api.openweathermap.org/data/2.5/weather?q=hambantota,lk&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 179 | hamilton,bm -- query_url: http://api.openweathermap.org/data/2.5/weather?q=hamilton,bm&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 180 | haradok,by -- query_url: http://api.openweathermap.org/data/2.5/weather?q=haradok,by&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 181 | harlingen,nl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=harlingen,nl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 182 | harper,lr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=harper,lr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 183 | hauterive,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=hauterive,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 184 | havre-saint-pierre,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=havre-saint-pierre,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 185 | henties bay,na -- query_url: http://api.openweathermap.org/data/2.5/weather?q=henties bay,na&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 186 | herat,af -- query_url: http://api.openweathermap.org/data/2.5/weather?q=herat,af&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 187 | hermanus,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 188 | hithadhoo,mv -- query_url: http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 189 | hobyo,so -- query_url: http://api.openweathermap.org/data/2.5/weather?q=hobyo,so&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 190 | hofn,is -- query_url: http://api.openweathermap.org/data/2.5/weather?q=hofn,is&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 191 | huarmey,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=huarmey,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 192 | hunza,pk -- query_url: http://api.openweathermap.org/data/2.5/weather?q=hunza,pk&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 193 | husavik,is -- query_url: http://api.openweathermap.org/data/2.5/weather?q=husavik,is&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 194 | iberia,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=iberia,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 195 | illoqqortoormiut,gl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=illoqqortoormiut,gl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 196 | ilulissat,gl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ilulissat,gl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 197 | imbituba,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=imbituba,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 198 | inongo,cd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=inongo,cd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 199 | iqaluit,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=iqaluit,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 200 | itacoatiara,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=itacoatiara,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 201 | itaituba,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=itaituba,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 202 | itarema,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=itarema,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 203 | jacareacanga,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=jacareacanga,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 204 | jamestown,sh -- query_url: http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 205 | japura,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=japura,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 206 | jaru,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=jaru,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 207 | juazeiro,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=juazeiro,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 208 | kabinda,cd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kabinda,cd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 209 | kachikau,bw -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kachikau,bw&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 210 | kadi,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kadi,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 211 | kaduqli,sd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kaduqli,sd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 212 | kakonko,tz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kakonko,tz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 213 | kalemie,cd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kalemie,cd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 214 | kambove,cd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kambove,cd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 215 | kamenka,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kamenka,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 216 | kansanshi,zm -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kansanshi,zm&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 217 | kaoma,zm -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kaoma,zm&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 218 | karaul,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=karaul,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 219 | karkaralinsk,kz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=karkaralinsk,kz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 220 | karlskoga,se -- query_url: http://api.openweathermap.org/data/2.5/weather?q=karlskoga,se&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 221 | karonga,mw -- query_url: http://api.openweathermap.org/data/2.5/weather?q=karonga,mw&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 222 | kashi,cn -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kashi,cn&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 223 | kavaratti,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kavaratti,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 224 | kayanga,tz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kayanga,tz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 225 | kedrovyy,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kedrovyy,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 226 | kerchevskiy,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kerchevskiy,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 227 | khabary,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=khabary,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 228 | khash,ir -- query_url: http://api.openweathermap.org/data/2.5/weather?q=khash,ir&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 229 | khorixas,na -- query_url: http://api.openweathermap.org/data/2.5/weather?q=khorixas,na&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 230 | kibakwe,tz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kibakwe,tz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 231 | kilembe,ug -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kilembe,ug&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 232 | kindia,gn -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kindia,gn&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 233 | kismayo,so -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kismayo,so&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 234 | klaksvik,fo -- query_url: http://api.openweathermap.org/data/2.5/weather?q=klaksvik,fo&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 235 | knysna,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=knysna,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 236 | kokstad,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kokstad,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 237 | kondagaon,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kondagaon,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 238 | korablino,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=korablino,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 239 | korla,cn -- query_url: http://api.openweathermap.org/data/2.5/weather?q=korla,cn&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 240 | kraljevo,rs -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kraljevo,rs&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 241 | krasnokholmskiy,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=krasnokholmskiy,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 242 | krasnopavlivka,ua -- query_url: http://api.openweathermap.org/data/2.5/weather?q=krasnopavlivka,ua&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 243 | krasnoselkup,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=krasnoselkup,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 244 | kruisfontein,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kruisfontein,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 245 | kudahuvadhoo,mv -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kudahuvadhoo,mv&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 246 | kurtamysh,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kurtamysh,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 247 | kuytun,cn -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kuytun,cn&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 248 | lagoa,pt -- query_url: http://api.openweathermap.org/data/2.5/weather?q=lagoa,pt&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 249 | laguna,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=laguna,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 250 | lakkion,gr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=lakkion,gr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 251 | lasa,cn -- query_url: http://api.openweathermap.org/data/2.5/weather?q=lasa,cn&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 252 | lavumisa,sz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=lavumisa,sz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 253 | lebu,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=lebu,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 254 | ler,sd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ler,sd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 255 | lerwick,gb -- query_url: http://api.openweathermap.org/data/2.5/weather?q=lerwick,gb&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 256 | liepaja,lv -- query_url: http://api.openweathermap.org/data/2.5/weather?q=liepaja,lv&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 257 | lima,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=lima,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 258 | lincoln,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=lincoln,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 259 | lira,ug -- query_url: http://api.openweathermap.org/data/2.5/weather?q=lira,ug&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 260 | liverpool,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=liverpool,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 261 | loandjili,cg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=loandjili,cg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 262 | lodja,cd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=lodja,cd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 263 | longyearbyen,sj -- query_url: http://api.openweathermap.org/data/2.5/weather?q=longyearbyen,sj&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 264 | los andes,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=los andes,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 265 | los llanos de aridane,es -- query_url: http://api.openweathermap.org/data/2.5/weather?q=los llanos de aridane,es&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 266 | luanda,ao -- query_url: http://api.openweathermap.org/data/2.5/weather?q=luanda,ao&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 267 | lucapa,ao -- query_url: http://api.openweathermap.org/data/2.5/weather?q=lucapa,ao&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 268 | luderitz,na -- query_url: http://api.openweathermap.org/data/2.5/weather?q=luderitz,na&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 269 | luis correia,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=luis correia,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 270 | lutry,ch -- query_url: http://api.openweathermap.org/data/2.5/weather?q=lutry,ch&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 271 | maceio,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=maceio,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 272 | madimba,tz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=madimba,tz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 273 | mafra,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mafra,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 274 | mahajanga,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mahajanga,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 275 | mahebourg,mu -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mahebourg,mu&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 276 | malakal,sd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=malakal,sd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 277 | maldonado,uy -- query_url: http://api.openweathermap.org/data/2.5/weather?q=maldonado,uy&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 278 | mamlyutka,kz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mamlyutka,kz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 279 | mana,gf -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mana,gf&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 280 | manaure,co -- query_url: http://api.openweathermap.org/data/2.5/weather?q=manaure,co&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 281 | mancio lima,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mancio lima,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 282 | mandal,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mandal,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 283 | manicore,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=manicore,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 284 | maniitsoq,gl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=maniitsoq,gl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 285 | manjakandriana,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=manjakandriana,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 286 | manoel urbano,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=manoel urbano,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 287 | manono,cd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=manono,cd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 288 | manta,ec -- query_url: http://api.openweathermap.org/data/2.5/weather?q=manta,ec&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 289 | manyana,bw -- query_url: http://api.openweathermap.org/data/2.5/weather?q=manyana,bw&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 290 | mar del plata,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mar del plata,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 291 | marawi,sd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=marawi,sd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 292 | marcona,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=marcona,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 293 | margate,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=margate,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 294 | marienburg,sr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=marienburg,sr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 295 | mariental,na -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mariental,na&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 296 | marrakesh,ma -- query_url: http://api.openweathermap.org/data/2.5/weather?q=marrakesh,ma&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 297 | marzuq,ly -- query_url: http://api.openweathermap.org/data/2.5/weather?q=marzuq,ly&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 298 | masty,by -- query_url: http://api.openweathermap.org/data/2.5/weather?q=masty,by&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 299 | masuguru,tz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=masuguru,tz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 300 | matara,lk -- query_url: http://api.openweathermap.org/data/2.5/weather?q=matara,lk&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 301 | matay,eg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=matay,eg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 302 | medina,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=medina,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 303 | mehamn,no -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mehamn,no&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 304 | meulaboh,id -- query_url: http://api.openweathermap.org/data/2.5/weather?q=meulaboh,id&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 305 | mezen,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mezen,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 306 | mhlume,sz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mhlume,sz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 307 | micheweni,tz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=micheweni,tz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 308 | minab,ir -- query_url: http://api.openweathermap.org/data/2.5/weather?q=minab,ir&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 309 | minas novas,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=minas novas,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 310 | miranorte,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=miranorte,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 311 | mirina,gr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mirina,gr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 312 | mizdah,ly -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mizdah,ly&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 313 | mocambique,mz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mocambique,mz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 314 | mocuba,mz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mocuba,mz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 315 | molchanovo,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=molchanovo,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 316 | monte aprazivel,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=monte aprazivel,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 317 | montepuez,mz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=montepuez,mz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 318 | moose factory,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=moose factory,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 319 | mopipi,bw -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mopipi,bw&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 320 | morales,gt -- query_url: http://api.openweathermap.org/data/2.5/weather?q=morales,gt&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 321 | moroni,km -- query_url: http://api.openweathermap.org/data/2.5/weather?q=moroni,km&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 322 | morros,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=morros,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 323 | muli,mv -- query_url: http://api.openweathermap.org/data/2.5/weather?q=muli,mv&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 324 | mumford,gh -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mumford,gh&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 325 | murgab,tm -- query_url: http://api.openweathermap.org/data/2.5/weather?q=murgab,tm&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 326 | muros,es -- query_url: http://api.openweathermap.org/data/2.5/weather?q=muros,es&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 327 | mutoko,zw -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mutoko,zw&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 328 | mutsamudu,km -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mutsamudu,km&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 329 | mwinilunga,zm -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mwinilunga,zm&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 330 | namibe,ao -- query_url: http://api.openweathermap.org/data/2.5/weather?q=namibe,ao&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 331 | nanortalik,gl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=nanortalik,gl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 332 | nantucket,us -- query_url: http://api.openweathermap.org/data/2.5/weather?q=nantucket,us&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 333 | narsaq,gl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=narsaq,gl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 334 | naryan-mar,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=naryan-mar,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 335 | natal,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=natal,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 336 | necochea,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=necochea,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 337 | neuquen,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=neuquen,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 338 | newton abbot,gb -- query_url: http://api.openweathermap.org/data/2.5/weather?q=newton abbot,gb&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 339 | nicoya,cr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=nicoya,cr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 340 | nizwa,om -- query_url: http://api.openweathermap.org/data/2.5/weather?q=nizwa,om&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 341 | nokaneng,bw -- query_url: http://api.openweathermap.org/data/2.5/weather?q=nokaneng,bw&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 342 | nosy varika,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=nosy varika,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 343 | nouadhibou,mr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=nouadhibou,mr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 344 | nuuk,gl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=nuuk,gl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 345 | oistins,bb -- query_url: http://api.openweathermap.org/data/2.5/weather?q=oistins,bb&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 346 | olafsvik,is -- query_url: http://api.openweathermap.org/data/2.5/weather?q=olafsvik,is&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 347 | olinda,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=olinda,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 348 | ondjiva,ao -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ondjiva,ao&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 349 | ongwediva,na -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ongwediva,na&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 350 | opuwo,na -- query_url: http://api.openweathermap.org/data/2.5/weather?q=opuwo,na&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 351 | oranjemund,na -- query_url: http://api.openweathermap.org/data/2.5/weather?q=oranjemund,na&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 352 | oranjestad,aw -- query_url: http://api.openweathermap.org/data/2.5/weather?q=oranjestad,aw&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 353 | ostrovnoy,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ostrovnoy,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 354 | paamiut,gl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=paamiut,gl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 355 | padang,id -- query_url: http://api.openweathermap.org/data/2.5/weather?q=padang,id&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 356 | pangnirtung,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=pangnirtung,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 357 | pangody,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=pangody,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 358 | parabel,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=parabel,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 359 | paramonga,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=paramonga,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 360 | paratinga,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=paratinga,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 361 | pascagoula,us -- query_url: http://api.openweathermap.org/data/2.5/weather?q=pascagoula,us&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 362 | pisco,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=pisco,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 363 | plettenberg bay,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=plettenberg bay,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 364 | ponta do sol,cv -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ponta do sol,cv&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 365 | poopo,bo -- query_url: http://api.openweathermap.org/data/2.5/weather?q=poopo,bo&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 366 | port alfred,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=port alfred,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 367 | port elizabeth,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=port elizabeth,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 368 | port hawkesbury,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=port hawkesbury,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 369 | port shepstone,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=port shepstone,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 370 | port-gentil,ga -- query_url: http://api.openweathermap.org/data/2.5/weather?q=port-gentil,ga&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 371 | porto nacional,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=porto nacional,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 372 | porto torres,it -- query_url: http://api.openweathermap.org/data/2.5/weather?q=porto torres,it&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 373 | portree,gb -- query_url: http://api.openweathermap.org/data/2.5/weather?q=portree,gb&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 374 | potoci,ba -- query_url: http://api.openweathermap.org/data/2.5/weather?q=potoci,ba&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 375 | pozzallo,it -- query_url: http://api.openweathermap.org/data/2.5/weather?q=pozzallo,it&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 376 | presidencia roque saenz pena,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=presidencia roque saenz pena,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 377 | punta arenas,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 378 | qaanaaq,gl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 379 | qaqortoq,gl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=qaqortoq,gl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 380 | quatre cocos,mu -- query_url: http://api.openweathermap.org/data/2.5/weather?q=quatre cocos,mu&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 381 | quelimane,mz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=quelimane,mz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 382 | quthing,ls -- query_url: http://api.openweathermap.org/data/2.5/weather?q=quthing,ls&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 383 | raga,sd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=raga,sd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 384 | rawson,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=rawson,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 385 | rehoboth,na -- query_url: http://api.openweathermap.org/data/2.5/weather?q=rehoboth,na&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 386 | riachao das neves,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=riachao das neves,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 387 | ribeira grande,pt -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ribeira grande,pt&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 388 | richards bay,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=richards bay,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 389 | rio gallegos,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=rio gallegos,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 390 | rio grande,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=rio grande,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 391 | rio pardo,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=rio pardo,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 392 | rivadavia,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=rivadavia,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 393 | road town,vg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=road town,vg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 394 | roald,no -- query_url: http://api.openweathermap.org/data/2.5/weather?q=roald,no&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 395 | rocha,uy -- query_url: http://api.openweathermap.org/data/2.5/weather?q=rocha,uy&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 396 | roches noires,mu -- query_url: http://api.openweathermap.org/data/2.5/weather?q=roches noires,mu&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 397 | rognan,no -- query_url: http://api.openweathermap.org/data/2.5/weather?q=rognan,no&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 398 | rojhan,pk -- query_url: http://api.openweathermap.org/data/2.5/weather?q=rojhan,pk&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 399 | rolim de moura,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=rolim de moura,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 400 | ruthin,gb -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ruthin,gb&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 401 | saint anthony,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=saint anthony,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 402 | saint-augustin,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=saint-augustin,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 403 | saint-denis,re -- query_url: http://api.openweathermap.org/data/2.5/weather?q=saint-denis,re&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 404 | saint-jean-de-braye,fr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=saint-jean-de-braye,fr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 405 | saint-joseph,re -- query_url: http://api.openweathermap.org/data/2.5/weather?q=saint-joseph,re&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 406 | saint-leu,re -- query_url: http://api.openweathermap.org/data/2.5/weather?q=saint-leu,re&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 407 | saint-philippe,re -- query_url: http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 408 | saint-pierre,re -- query_url: http://api.openweathermap.org/data/2.5/weather?q=saint-pierre,re&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 409 | sakaraha,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sakaraha,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 410 | salalah,om -- query_url: http://api.openweathermap.org/data/2.5/weather?q=salalah,om&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 411 | saldanha,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=saldanha,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 412 | salinopolis,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=salinopolis,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 413 | sambava,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sambava,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 414 | san carlos de bariloche,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=san carlos de bariloche,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 415 | san cristobal,ec -- query_url: http://api.openweathermap.org/data/2.5/weather?q=san cristobal,ec&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 416 | san ignacio,bo -- query_url: http://api.openweathermap.org/data/2.5/weather?q=san ignacio,bo&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 417 | san luis,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=san luis,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 418 | san martin,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=san martin,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 419 | san matias,bo -- query_url: http://api.openweathermap.org/data/2.5/weather?q=san matias,bo&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 420 | san rafael,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=san rafael,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 421 | san vicente de canete,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=san vicente de canete,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 422 | santa cruz,cr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=santa cruz,cr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 423 | santa isabel do rio negro,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=santa isabel do rio negro,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 424 | santa rosa,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=santa rosa,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 425 | santa vitoria do palmar,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=santa vitoria do palmar,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 426 | santiago del estero,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=santiago del estero,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 427 | santona,es -- query_url: http://api.openweathermap.org/data/2.5/weather?q=santona,es&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 428 | sao felix do xingu,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sao felix do xingu,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 429 | sao filipe,cv -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sao filipe,cv&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 430 | sao gabriel da cachoeira,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sao gabriel da cachoeira,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 431 | sao geraldo do araguaia,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sao geraldo do araguaia,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 432 | sao joao da barra,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sao joao da barra,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 433 | sao joao da ponte,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sao joao da ponte,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 434 | sao luiz gonzaga,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sao luiz gonzaga,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 435 | sao miguel do araguaia,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sao miguel do araguaia,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 436 | sao paulo de olivenca,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sao paulo de olivenca,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 437 | sao raimundo nonato,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sao raimundo nonato,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 438 | scottsboro,us -- query_url: http://api.openweathermap.org/data/2.5/weather?q=scottsboro,us&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 439 | scottsburgh,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=scottsburgh,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 440 | secunda,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=secunda,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 441 | semme,sn -- query_url: http://api.openweathermap.org/data/2.5/weather?q=semme,sn&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 442 | sept-iles,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sept-iles,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 443 | shakawe,bw -- query_url: http://api.openweathermap.org/data/2.5/weather?q=shakawe,bw&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 444 | sinkat,sd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sinkat,sd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 445 | sistranda,no -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sistranda,no&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 446 | skelleftea,se -- query_url: http://api.openweathermap.org/data/2.5/weather?q=skelleftea,se&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 447 | sokolo,ml -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sokolo,ml&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 448 | sokoto,ng -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sokoto,ng&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 449 | songea,tz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=songea,tz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 450 | souillac,mu -- query_url: http://api.openweathermap.org/data/2.5/weather?q=souillac,mu&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 451 | soyo,ao -- query_url: http://api.openweathermap.org/data/2.5/weather?q=soyo,ao&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 452 | stantsiya gorchakovo,uz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=stantsiya gorchakovo,uz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 453 | stokmarknes,no -- query_url: http://api.openweathermap.org/data/2.5/weather?q=stokmarknes,no&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 454 | strezhevoy,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=strezhevoy,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 455 | stykkisholmur,is -- query_url: http://api.openweathermap.org/data/2.5/weather?q=stykkisholmur,is&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 456 | suez,eg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=suez,eg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 457 | sur,om -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sur,om&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 458 | swellendam,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=swellendam,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 459 | tabou,ci -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tabou,ci&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 460 | tabuk,sa -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tabuk,sa&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 461 | tacna,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tacna,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 462 | talnakh,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=talnakh,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 463 | taltal,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=taltal,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 464 | tamandare,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tamandare,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 465 | taolanaro,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=taolanaro,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 466 | tarancon,es -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tarancon,es&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 467 | tarata,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tarata,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 468 | tarko-sale,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tarko-sale,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 469 | tarudant,ma -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tarudant,ma&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 470 | tashtyp,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tashtyp,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 471 | tasiilaq,gl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 472 | tawkar,sd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tawkar,sd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 473 | taybad,ir -- query_url: http://api.openweathermap.org/data/2.5/weather?q=taybad,ir&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 474 | tazmalt,dz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tazmalt,dz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 475 | tazovskiy,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tazovskiy,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 476 | tefe,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tefe,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 477 | teguise,es -- query_url: http://api.openweathermap.org/data/2.5/weather?q=teguise,es&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 478 | tessalit,ml -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tessalit,ml&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 479 | thinadhoo,mv -- query_url: http://api.openweathermap.org/data/2.5/weather?q=thinadhoo,mv&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 480 | thompson,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=thompson,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 481 | tingo maria,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tingo maria,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 482 | tocopilla,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tocopilla,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 483 | torbay,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=torbay,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 484 | totma,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=totma,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 485 | touros,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=touros,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 486 | trinidad,bo -- query_url: http://api.openweathermap.org/data/2.5/weather?q=trinidad,bo&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 487 | tromso,no -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tromso,no&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 488 | tsihombe,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tsihombe,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 489 | tsiroanomandidy,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tsiroanomandidy,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 490 | tulum,mx -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tulum,mx&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 491 | tumannyy,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tumannyy,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 492 | umzimvubu,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=umzimvubu,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 493 | upernavik,gl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 494 | urucara,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=urucara,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 495 | urucui,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=urucui,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 496 | usak,tr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=usak,tr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 497 | ushuaia,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 498 | usinsk,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=usinsk,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 499 | uvarovka,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=uvarovka,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 500 | uyuni,bo -- query_url: http://api.openweathermap.org/data/2.5/weather?q=uyuni,bo&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 501 | vakhtan,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=vakhtan,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 502 | valdivia,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=valdivia,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 503 | vallenar,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=vallenar,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 504 | valparaiso,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=valparaiso,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 505 | vardo,no -- query_url: http://api.openweathermap.org/data/2.5/weather?q=vardo,no&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 506 | vargem grande,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=vargem grande,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 507 | veinticinco de mayo,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=veinticinco de mayo,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 508 | verkh-suetka,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=verkh-suetka,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 509 | vestmanna,fo -- query_url: http://api.openweathermap.org/data/2.5/weather?q=vestmanna,fo&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 510 | vestmannaeyjar,is -- query_url: http://api.openweathermap.org/data/2.5/weather?q=vestmannaeyjar,is&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 511 | vetlanda,se -- query_url: http://api.openweathermap.org/data/2.5/weather?q=vetlanda,se&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 512 | victoria,sc -- query_url: http://api.openweathermap.org/data/2.5/weather?q=victoria,sc&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 513 | viedma,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=viedma,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 514 | vila franca do campo,pt -- query_url: http://api.openweathermap.org/data/2.5/weather?q=vila franca do campo,pt&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 515 | vila velha,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=vila velha,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 516 | vilhena,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=vilhena,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 517 | villavicencio,co -- query_url: http://api.openweathermap.org/data/2.5/weather?q=villavicencio,co&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 518 | villazon,bo -- query_url: http://api.openweathermap.org/data/2.5/weather?q=villazon,bo&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 519 | viseu,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=viseu,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 520 | waddan,ly -- query_url: http://api.openweathermap.org/data/2.5/weather?q=waddan,ly&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 521 | wajir,ke -- query_url: http://api.openweathermap.org/data/2.5/weather?q=wajir,ke&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 522 | walvis bay,na -- query_url: http://api.openweathermap.org/data/2.5/weather?q=walvis bay,na&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 523 | warri,ng -- query_url: http://api.openweathermap.org/data/2.5/weather?q=warri,ng&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 524 | watsa,cd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=watsa,cd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 525 | weligama,lk -- query_url: http://api.openweathermap.org/data/2.5/weather?q=weligama,lk&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 526 | werda,bw -- query_url: http://api.openweathermap.org/data/2.5/weather?q=werda,bw&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 527 | willowmore,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=willowmore,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 528 | winchester,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=winchester,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 529 | witrivier,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=witrivier,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 530 | wukari,ng -- query_url: http://api.openweathermap.org/data/2.5/weather?q=wukari,ng&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 531 | xique-xique,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=xique-xique,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 532 | xuddur,so -- query_url: http://api.openweathermap.org/data/2.5/weather?q=xuddur,so&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 533 | yangambi,cd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=yangambi,cd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 534 | yar-sale,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=yar-sale,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 535 | yarada,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=yarada,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 536 | yauya,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=yauya,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 537 | young,uy -- query_url: http://api.openweathermap.org/data/2.5/weather?q=young,uy&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 538 | zaltan,ly -- query_url: http://api.openweathermap.org/data/2.5/weather?q=zaltan,ly&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 539 | zharkent,kz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=zharkent,kz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 540 | zhezkazgan,kz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=zhezkazgan,kz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Total errors:  1
    




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
      <td>abeche</td>
      <td>td</td>
      <td>2017-09-08 13:40:20</td>
      <td>20.83</td>
      <td>13.83</td>
      <td>72.99</td>
      <td>83.0</td>
      <td>24.0</td>
      <td>3.40</td>
    </tr>
    <tr>
      <th>1</th>
      <td>abu samrah</td>
      <td>qa</td>
      <td>2017-09-08 13:00:00</td>
      <td>55.58</td>
      <td>24.25</td>
      <td>91.40</td>
      <td>33.0</td>
      <td>0.0</td>
      <td>4.70</td>
    </tr>
    <tr>
      <th>2</th>
      <td>acari</td>
      <td>pe</td>
      <td>2017-09-08 13:40:21</td>
      <td>-74.62</td>
      <td>-15.43</td>
      <td>66.69</td>
      <td>54.0</td>
      <td>8.0</td>
      <td>2.95</td>
    </tr>
    <tr>
      <th>3</th>
      <td>adjumani</td>
      <td>ug</td>
      <td>2017-09-08 13:40:21</td>
      <td>31.79</td>
      <td>3.38</td>
      <td>68.04</td>
      <td>96.0</td>
      <td>68.0</td>
      <td>3.74</td>
    </tr>
    <tr>
      <th>4</th>
      <td>agadir</td>
      <td>ma</td>
      <td>2017-09-08 13:00:00</td>
      <td>-9.60</td>
      <td>30.42</td>
      <td>64.40</td>
      <td>100.0</td>
      <td>90.0</td>
      <td>3.36</td>
    </tr>
  </tbody>
</table>
</div>




```python
## Save Data to csv
## For data analysis: Export file without index, with header
city_wdf.to_csv("world_cities_weather_hw5.csv", index=False, header=True)
```


```python
## Scatter plot Latitude - Temperature:

# The biggest information that jumps out at me is the concentration
# of cities in the moderate temperature zone.  The cities are concentrated
# in the 60 - 80 degree range with fewer as you move upwards or downwards 
# in temperature.  It would be nice to be able to hover over the circles and
# see more information.  Hidden city information would be helpful but not 
# distracting from the chart.
```


```python
## https://seaborn.pydata.org/generated/seaborn.regplot.html
## import seaborn as sns; sns.set(color_codes=True)

import seaborn as sns

# Set my default color palette
mycolors = ["magenta", "blue", "red", "green", "cyan", "coral", "skyblue", "gold"]
sns.set_palette(mycolors)

# Add current date to the title
cdate = datetime.now().strftime("(%m/%d/%Y)")

x_axis = city_wdf["lat"]
y_axis = city_wdf["max_temperature"]


sns.regplot(x=x_axis, y=y_axis, color="magenta", marker="o", fit_reg=True, 
            scatter_kws={"s":80, "linewidths":1, "edgecolor":"k"})

sns.set_style("darkgrid")
sns.plt.title("City Latitude vs Temperature %s" % (cdate), weight='bold').set_fontsize('16')
sns.plt.xlabel("Latitude", weight='bold').set_fontsize('14')
sns.plt.ylabel("Max Temperature (F)", weight='bold',).set_fontsize('14')

plt.savefig("lat_temp_scatter.png",bbox_inches="tight")
plt.show()
```


![png](PyWeather_hw5-submit_files/PyWeather_hw5-submit_9_0.png)



```python
## Scatter plot Latitude - Humidity:

# The humidity chart reveals something I don't often remember, being
# from California most of my life, but having experienced east coast 
# humidity, there is a percentage of humidity in all the cities.  That
# tells me that humidity doesn't have to be connected to sticky yucky
# weather.  Also, Humidity doesn't seem to impact the bilding of cities 
# as they are spread out relatively well with some concentrations.
```


```python
## https://seaborn.pydata.org/generated/seaborn.regplot.html
## import seaborn as sns; sns.set(color_codes=True)

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


![png](PyWeather_hw5-submit_files/PyWeather_hw5-submit_11_0.png)



```python
## Scatter plot Latitude - Cloudiness:

# I think this is the least informative chart of the group.  I can tell it
# is cloudy in a lot of cities to some degree, and there are a number of 
# cities with no clouds.
```


```python
## https://seaborn.pydata.org/generated/seaborn.regplot.html
## import seaborn as sns; sns.set(color_codes=True)

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


![png](PyWeather_hw5-submit_files/PyWeather_hw5-submit_13_0.png)



```python
## Scatter plot Latitude - Wind:

# The latidtude wind chart doesn't hold any surprises for me.  In my
# area, wind up 16 mph is normal with higher gusts at higher elevations.
# Above 25 mph is getting more uncomfortable especially if the wind
# speed is sustained for hours or days.  Our weather window is narrow
# so we can't tell much besides the majority of cities in our population
# are having a normal range of wind speed for the forcast.
```


```python
## https://seaborn.pydata.org/generated/seaborn.regplot.html
## import seaborn as sns; sns.set(color_codes=True)

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


![png](PyWeather_hw5-submit_files/PyWeather_hw5-submit_15_0.png)



```python
## Create a markdown file of the Jupyter Notebook
```
