

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
    271
    Current tuple  (0, 90)
    b = 0 c = 90
    Pass b, c to while loop...
    546
    Current tuple  (90, 180)
    b = 90 c = 180
    Pass b, c to while loop...
    559
    


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

    559
    534
    




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
      <td>abu dhabi</td>
      <td>ae</td>
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
      <td>aconibe</td>
      <td>gq</td>
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
      <td>adeje</td>
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
      <th>5</th>
      <td>adrar</td>
      <td>dz</td>
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
      <td>afua</td>
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
      <th>7</th>
      <td>alanya</td>
      <td>tr</td>
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
      <th>9</th>
      <td>albertville</td>
      <td>us</td>
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

    Row index: 0 | abu dhabi,ae -- query_url: http://api.openweathermap.org/data/2.5/weather?q=abu dhabi,ae&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 1 | acarau,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=acarau,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 2 | acari,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=acari,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 3 | aconibe,gq -- query_url: http://api.openweathermap.org/data/2.5/weather?q=aconibe,gq&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 4 | adeje,es -- query_url: http://api.openweathermap.org/data/2.5/weather?q=adeje,es&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 5 | adrar,dz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=adrar,dz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 6 | afua,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=afua,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 7 | alanya,tr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=alanya,tr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 8 | albany,au -- query_url: http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 9 | albertville,us -- query_url: http://api.openweathermap.org/data/2.5/weather?q=albertville,us&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 10 | aleksandrovsk,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=aleksandrovsk,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 11 | alta floresta,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=alta floresta,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 12 | ambilobe,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ambilobe,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 13 | amderma,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=amderma,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 14 | ampanihy,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ampanihy,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 15 | anaco,ve -- query_url: http://api.openweathermap.org/data/2.5/weather?q=anaco,ve&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 16 | ancud,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ancud,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 17 | andevoranto,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=andevoranto,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 18 | angoche,mz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=angoche,mz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 19 | ankazoabo,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ankazoabo,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 20 | anloga,gh -- query_url: http://api.openweathermap.org/data/2.5/weather?q=anloga,gh&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 21 | antigonish,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=antigonish,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 22 | apele vii,ro -- query_url: http://api.openweathermap.org/data/2.5/weather?q=apele vii,ro&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 23 | aranos,na -- query_url: http://api.openweathermap.org/data/2.5/weather?q=aranos,na&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 24 | araouane,ml -- query_url: http://api.openweathermap.org/data/2.5/weather?q=araouane,ml&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 25 | arcachon,fr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=arcachon,fr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 26 | ardon,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ardon,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 27 | aripuana,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=aripuana,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 28 | arlit,ne -- query_url: http://api.openweathermap.org/data/2.5/weather?q=arlit,ne&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 29 | arraial do cabo,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=arraial do cabo,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 30 | ascension,bo -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ascension,bo&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 31 | asosa,et -- query_url: http://api.openweathermap.org/data/2.5/weather?q=asosa,et&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 32 | aswan,eg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=aswan,eg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 33 | atlantic city,us -- query_url: http://api.openweathermap.org/data/2.5/weather?q=atlantic city,us&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 34 | atocha,bo -- query_url: http://api.openweathermap.org/data/2.5/weather?q=atocha,bo&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 35 | attawapiskat,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=attawapiskat,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 36 | axim,gh -- query_url: http://api.openweathermap.org/data/2.5/weather?q=axim,gh&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 37 | bajina basta,rs -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bajina basta,rs&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 38 | balfour,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=balfour,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 39 | bam,ir -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bam,ir&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 40 | bambous virieux,mu -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bambous virieux,mu&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 41 | bangangte,cm -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bangangte,cm&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 42 | barentsburg,sj -- query_url: http://api.openweathermap.org/data/2.5/weather?q=barentsburg,sj&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    The key doesn't exist: barentsburg, sj.
    <class 'KeyError'>
    Row index: 43 | barranca,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=barranca,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 44 | bathsheba,bb -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bathsheba,bb&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 45 | beira,mz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=beira,mz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 46 | beirut,lb -- query_url: http://api.openweathermap.org/data/2.5/weather?q=beirut,lb&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 47 | belmonte,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=belmonte,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 48 | beloha,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=beloha,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 49 | belushya guba,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=belushya guba,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 50 | bengkulu,id -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bengkulu,id&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 51 | benguela,ao -- query_url: http://api.openweathermap.org/data/2.5/weather?q=benguela,ao&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 52 | berdychiv,ua -- query_url: http://api.openweathermap.org/data/2.5/weather?q=berdychiv,ua&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 53 | berlevag,no -- query_url: http://api.openweathermap.org/data/2.5/weather?q=berlevag,no&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 54 | bhag,pk -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bhag,pk&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 55 | bibiani,gh -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bibiani,gh&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 56 | bid,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bid,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 57 | bilma,ne -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bilma,ne&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 58 | boa vista,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=boa vista,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 59 | boca do acre,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=boca do acre,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 60 | bodden town,ky -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bodden town,ky&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 61 | bolgatanga,gh -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bolgatanga,gh&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 62 | bolungarvik,is -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bolungarvik,is&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 63 | bom jesus do galho,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bom jesus do galho,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 64 | bonavista,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bonavista,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 65 | bosobolo,cd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bosobolo,cd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 66 | bowling green,us -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bowling green,us&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 67 | brae,gb -- query_url: http://api.openweathermap.org/data/2.5/weather?q=brae,gb&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 68 | brasilia,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=brasilia,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 69 | bredasdorp,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 70 | bronnoysund,no -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bronnoysund,no&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 71 | bubaque,gw -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bubaque,gw&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 72 | buchanan,lr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=buchanan,lr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 73 | bud,no -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bud,no&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 74 | bur gabo,so -- query_url: http://api.openweathermap.org/data/2.5/weather?q=bur gabo,so&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 75 | burica,pa -- query_url: http://api.openweathermap.org/data/2.5/weather?q=burica,pa&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 76 | busselton,au -- query_url: http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 77 | butembo,cd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=butembo,cd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 78 | buzmeyin,tm -- query_url: http://api.openweathermap.org/data/2.5/weather?q=buzmeyin,tm&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 79 | cabimas,ve -- query_url: http://api.openweathermap.org/data/2.5/weather?q=cabimas,ve&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 80 | calamar,co -- query_url: http://api.openweathermap.org/data/2.5/weather?q=calamar,co&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 81 | calvinia,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=calvinia,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 82 | camabatela,ao -- query_url: http://api.openweathermap.org/data/2.5/weather?q=camabatela,ao&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 83 | camana,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=camana,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 84 | camocim,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=camocim,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 85 | cap malheureux,mu -- query_url: http://api.openweathermap.org/data/2.5/weather?q=cap malheureux,mu&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 86 | cape town,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 87 | caravelas,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=caravelas,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 88 | carnarvon,au -- query_url: http://api.openweathermap.org/data/2.5/weather?q=carnarvon,au&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 89 | carnot,cf -- query_url: http://api.openweathermap.org/data/2.5/weather?q=carnot,cf&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 90 | carutapera,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=carutapera,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 91 | castro,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=castro,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 92 | cayenne,gf -- query_url: http://api.openweathermap.org/data/2.5/weather?q=cayenne,gf&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 93 | centralia,us -- query_url: http://api.openweathermap.org/data/2.5/weather?q=centralia,us&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 94 | chake chake,tz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=chake chake,tz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 95 | chapais,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=chapais,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 96 | chicama,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=chicama,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 97 | chimore,bo -- query_url: http://api.openweathermap.org/data/2.5/weather?q=chimore,bo&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 98 | chinsali,zm -- query_url: http://api.openweathermap.org/data/2.5/weather?q=chinsali,zm&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 99 | chipinge,zw -- query_url: http://api.openweathermap.org/data/2.5/weather?q=chipinge,zw&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 100 | chokwe,mz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=chokwe,mz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 101 | chulym,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=chulym,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 102 | chuy,uy -- query_url: http://api.openweathermap.org/data/2.5/weather?q=chuy,uy&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 103 | cidreira,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=cidreira,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 104 | clarence town,bs -- query_url: http://api.openweathermap.org/data/2.5/weather?q=clarence town,bs&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 105 | clinton,us -- query_url: http://api.openweathermap.org/data/2.5/weather?q=clinton,us&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 106 | clonakilty,ie -- query_url: http://api.openweathermap.org/data/2.5/weather?q=clonakilty,ie&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 107 | clyde river,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=clyde river,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 108 | cockburn town,bs -- query_url: http://api.openweathermap.org/data/2.5/weather?q=cockburn town,bs&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 109 | codrington,ag -- query_url: http://api.openweathermap.org/data/2.5/weather?q=codrington,ag&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 110 | coihaique,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=coihaique,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 111 | colesberg,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=colesberg,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 112 | comodoro rivadavia,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=comodoro rivadavia,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 113 | conceicao do araguaia,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=conceicao do araguaia,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 114 | conde,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=conde,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 115 | constitucion,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=constitucion,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 116 | coquimbo,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=coquimbo,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 117 | de aar,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=de aar,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 118 | diamantino,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=diamantino,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 119 | dikson,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=dikson,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 120 | dingle,ie -- query_url: http://api.openweathermap.org/data/2.5/weather?q=dingle,ie&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 121 | dinsor,so -- query_url: http://api.openweathermap.org/data/2.5/weather?q=dinsor,so&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 122 | ditrau,ro -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ditrau,ro&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 123 | dnestrovsc,md -- query_url: http://api.openweathermap.org/data/2.5/weather?q=dnestrovsc,md&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 124 | dodoma,tz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=dodoma,tz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 125 | dourados,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=dourados,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 126 | durban,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=durban,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 127 | dzilam gonzalez,mx -- query_url: http://api.openweathermap.org/data/2.5/weather?q=dzilam gonzalez,mx&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 128 | east london,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=east london,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 129 | eenhana,na -- query_url: http://api.openweathermap.org/data/2.5/weather?q=eenhana,na&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 130 | el alto,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=el alto,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 131 | eyl,so -- query_url: http://api.openweathermap.org/data/2.5/weather?q=eyl,so&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 132 | faya,td -- query_url: http://api.openweathermap.org/data/2.5/weather?q=faya,td&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 133 | ferme-neuve,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ferme-neuve,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 134 | fomboni,km -- query_url: http://api.openweathermap.org/data/2.5/weather?q=fomboni,km&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 135 | formoso do araguaia,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=formoso do araguaia,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 136 | gainesville,us -- query_url: http://api.openweathermap.org/data/2.5/weather?q=gainesville,us&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 137 | galgani,sd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=galgani,sd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 138 | gallipoli,it -- query_url: http://api.openweathermap.org/data/2.5/weather?q=gallipoli,it&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 139 | gamba,ga -- query_url: http://api.openweathermap.org/data/2.5/weather?q=gamba,ga&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 140 | gemena,cd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=gemena,cd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 141 | general roca,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=general roca,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 142 | georgetown,sh -- query_url: http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 143 | georgiyevka,kz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=georgiyevka,kz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 144 | glasgow,us -- query_url: http://api.openweathermap.org/data/2.5/weather?q=glasgow,us&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 145 | gopalganj,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=gopalganj,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 146 | grand river south east,mu -- query_url: http://api.openweathermap.org/data/2.5/weather?q=grand river south east,mu&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 147 | grand-santi,gf -- query_url: http://api.openweathermap.org/data/2.5/weather?q=grand-santi,gf&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 148 | gravdal,no -- query_url: http://api.openweathermap.org/data/2.5/weather?q=gravdal,no&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 149 | halden,no -- query_url: http://api.openweathermap.org/data/2.5/weather?q=halden,no&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 150 | hambantota,lk -- query_url: http://api.openweathermap.org/data/2.5/weather?q=hambantota,lk&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 151 | hamilton,bm -- query_url: http://api.openweathermap.org/data/2.5/weather?q=hamilton,bm&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 152 | harper,lr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=harper,lr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 153 | havoysund,no -- query_url: http://api.openweathermap.org/data/2.5/weather?q=havoysund,no&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 154 | havre-saint-pierre,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=havre-saint-pierre,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 155 | henties bay,na -- query_url: http://api.openweathermap.org/data/2.5/weather?q=henties bay,na&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 156 | herat,af -- query_url: http://api.openweathermap.org/data/2.5/weather?q=herat,af&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 157 | hermanus,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 158 | hithadhoo,mv -- query_url: http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 159 | hobyo,so -- query_url: http://api.openweathermap.org/data/2.5/weather?q=hobyo,so&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 160 | hofn,is -- query_url: http://api.openweathermap.org/data/2.5/weather?q=hofn,is&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 161 | honningsvag,no -- query_url: http://api.openweathermap.org/data/2.5/weather?q=honningsvag,no&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 162 | hoopstad,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=hoopstad,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 163 | houlton,us -- query_url: http://api.openweathermap.org/data/2.5/weather?q=houlton,us&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 164 | hualmay,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=hualmay,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 165 | husavik,is -- query_url: http://api.openweathermap.org/data/2.5/weather?q=husavik,is&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 166 | iberia,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=iberia,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 167 | igarape-miri,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=igarape-miri,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 168 | igarka,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=igarka,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 169 | ilhabela,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ilhabela,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 170 | illoqqortoormiut,gl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=illoqqortoormiut,gl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 171 | ilo,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ilo,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 172 | ilulissat,gl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ilulissat,gl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 173 | imbituba,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=imbituba,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 174 | indiaroba,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=indiaroba,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 175 | ipojuca,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ipojuca,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 176 | iqaluit,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=iqaluit,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 177 | iquique,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=iquique,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 178 | iquitos,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=iquitos,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 179 | iracoubo,gf -- query_url: http://api.openweathermap.org/data/2.5/weather?q=iracoubo,gf&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 180 | irbil,iq -- query_url: http://api.openweathermap.org/data/2.5/weather?q=irbil,iq&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 181 | itacare,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=itacare,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 182 | itagiba,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=itagiba,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 183 | jacareacanga,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=jacareacanga,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 184 | jaguarao,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=jaguarao,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 185 | jalingo,ng -- query_url: http://api.openweathermap.org/data/2.5/weather?q=jalingo,ng&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 186 | jamestown,sh -- query_url: http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 187 | jarjis,tn -- query_url: http://api.openweathermap.org/data/2.5/weather?q=jarjis,tn&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 188 | jiddah,sa -- query_url: http://api.openweathermap.org/data/2.5/weather?q=jiddah,sa&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 189 | juripiranga,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=juripiranga,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 190 | jutai,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=jutai,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 191 | kalengwa,zm -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kalengwa,zm&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 192 | kalmunai,lk -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kalmunai,lk&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 193 | kapiri mposhi,zm -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kapiri mposhi,zm&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 194 | karasjok,no -- query_url: http://api.openweathermap.org/data/2.5/weather?q=karasjok,no&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 195 | karauzyak,uz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=karauzyak,uz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 196 | kargasok,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kargasok,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 197 | kargil,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kargil,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 198 | karpogory,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=karpogory,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 199 | kasamwa,tz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kasamwa,tz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 200 | kashi,cn -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kashi,cn&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 201 | kathu,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kathu,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 202 | kavaratti,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kavaratti,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 203 | kazalinsk,kz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kazalinsk,kz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 204 | kerchevskiy,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kerchevskiy,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 205 | khalkhal,ir -- query_url: http://api.openweathermap.org/data/2.5/weather?q=khalkhal,ir&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 206 | kharan,pk -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kharan,pk&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 207 | khormuj,ir -- query_url: http://api.openweathermap.org/data/2.5/weather?q=khormuj,ir&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 208 | khudumelapye,bw -- query_url: http://api.openweathermap.org/data/2.5/weather?q=khudumelapye,bw&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 209 | kidal,ml -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kidal,ml&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 210 | kilindoni,tz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kilindoni,tz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 211 | kisangani,cd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kisangani,cd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 212 | klaksvik,fo -- query_url: http://api.openweathermap.org/data/2.5/weather?q=klaksvik,fo&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 213 | kontagora,ng -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kontagora,ng&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 214 | korla,cn -- query_url: http://api.openweathermap.org/data/2.5/weather?q=korla,cn&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 215 | kosonsoy,uz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kosonsoy,uz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 216 | kralendijk,an -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kralendijk,an&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 217 | krasnoselkup,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=krasnoselkup,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 218 | krasnovishersk,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=krasnovishersk,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 219 | kruisfontein,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kruisfontein,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 220 | kutum,sd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=kutum,sd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 221 | la oroya,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=la oroya,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 222 | la palma,pa -- query_url: http://api.openweathermap.org/data/2.5/weather?q=la palma,pa&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 223 | la romana,do -- query_url: http://api.openweathermap.org/data/2.5/weather?q=la romana,do&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 224 | lagoa,pt -- query_url: http://api.openweathermap.org/data/2.5/weather?q=lagoa,pt&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 225 | laguna,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=laguna,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 226 | lagunas,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=lagunas,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 227 | lamu,ke -- query_url: http://api.openweathermap.org/data/2.5/weather?q=lamu,ke&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 228 | lar gerd,af -- query_url: http://api.openweathermap.org/data/2.5/weather?q=lar gerd,af&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 229 | lasa,cn -- query_url: http://api.openweathermap.org/data/2.5/weather?q=lasa,cn&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 230 | laukaa,fi -- query_url: http://api.openweathermap.org/data/2.5/weather?q=laukaa,fi&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 231 | lebu,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=lebu,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 232 | leh,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=leh,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 233 | lekoni,ga -- query_url: http://api.openweathermap.org/data/2.5/weather?q=lekoni,ga&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 234 | leningradskiy,tj -- query_url: http://api.openweathermap.org/data/2.5/weather?q=leningradskiy,tj&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 235 | leo,bf -- query_url: http://api.openweathermap.org/data/2.5/weather?q=leo,bf&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 236 | ler,sd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ler,sd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 237 | lerwick,gb -- query_url: http://api.openweathermap.org/data/2.5/weather?q=lerwick,gb&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 238 | litomerice,cz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=litomerice,cz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 239 | livingstonia,mw -- query_url: http://api.openweathermap.org/data/2.5/weather?q=livingstonia,mw&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 240 | llallagua,bo -- query_url: http://api.openweathermap.org/data/2.5/weather?q=llallagua,bo&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 241 | lodja,cd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=lodja,cd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 242 | longyearbyen,sj -- query_url: http://api.openweathermap.org/data/2.5/weather?q=longyearbyen,sj&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 243 | los llanos de aridane,es -- query_url: http://api.openweathermap.org/data/2.5/weather?q=los llanos de aridane,es&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 244 | louisbourg,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=louisbourg,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 245 | luanda,ao -- query_url: http://api.openweathermap.org/data/2.5/weather?q=luanda,ao&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 246 | lucapa,ao -- query_url: http://api.openweathermap.org/data/2.5/weather?q=lucapa,ao&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 247 | luderitz,na -- query_url: http://api.openweathermap.org/data/2.5/weather?q=luderitz,na&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 248 | luwingu,zm -- query_url: http://api.openweathermap.org/data/2.5/weather?q=luwingu,zm&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 249 | lyantonde,ug -- query_url: http://api.openweathermap.org/data/2.5/weather?q=lyantonde,ug&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 250 | maceio,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=maceio,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 251 | madaoua,ne -- query_url: http://api.openweathermap.org/data/2.5/weather?q=madaoua,ne&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 252 | mahebourg,mu -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mahebourg,mu&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 253 | makat,kz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=makat,kz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 254 | malanje,ao -- query_url: http://api.openweathermap.org/data/2.5/weather?q=malanje,ao&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 255 | malatya,tr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=malatya,tr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 256 | manavalakurichi,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=manavalakurichi,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 257 | mancio lima,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mancio lima,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 258 | mandera,ke -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mandera,ke&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 259 | manica,mz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=manica,mz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 260 | manicore,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=manicore,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 261 | maniitsoq,gl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=maniitsoq,gl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 262 | manono,cd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=manono,cd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 263 | mar del plata,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mar del plata,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 264 | maraa,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=maraa,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 265 | maragogi,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=maragogi,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 266 | marathon,us -- query_url: http://api.openweathermap.org/data/2.5/weather?q=marathon,us&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 267 | marcona,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=marcona,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 268 | margate,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=margate,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 269 | mariakani,ke -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mariakani,ke&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 270 | marion,us -- query_url: http://api.openweathermap.org/data/2.5/weather?q=marion,us&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 271 | marsa matruh,eg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=marsa matruh,eg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 272 | marystown,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=marystown,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 273 | matara,lk -- query_url: http://api.openweathermap.org/data/2.5/weather?q=matara,lk&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 274 | mathathane,bw -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mathathane,bw&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 275 | maues,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=maues,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 276 | mayahi,ne -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mayahi,ne&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 277 | mayumba,ga -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mayumba,ga&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 278 | mbala,zm -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mbala,zm&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 279 | mehamn,no -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mehamn,no&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 280 | meulaboh,id -- query_url: http://api.openweathermap.org/data/2.5/weather?q=meulaboh,id&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 281 | middletown,us -- query_url: http://api.openweathermap.org/data/2.5/weather?q=middletown,us&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 282 | milford,us -- query_url: http://api.openweathermap.org/data/2.5/weather?q=milford,us&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 283 | mitsamiouli,km -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mitsamiouli,km&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 284 | mmabatho,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mmabatho,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 285 | mocambique,mz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mocambique,mz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 286 | mogadishu,so -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mogadishu,so&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 287 | monrovia,lr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=monrovia,lr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 288 | moose factory,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=moose factory,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 289 | morondava,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=morondava,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 290 | mossoro,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mossoro,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 291 | moyale,ke -- query_url: http://api.openweathermap.org/data/2.5/weather?q=moyale,ke&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 292 | mpika,zm -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mpika,zm&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 293 | mponela,mw -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mponela,mw&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 294 | mtambile,tz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mtambile,tz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 295 | mufulira,zm -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mufulira,zm&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 296 | muros,es -- query_url: http://api.openweathermap.org/data/2.5/weather?q=muros,es&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 297 | mwinilunga,zm -- query_url: http://api.openweathermap.org/data/2.5/weather?q=mwinilunga,zm&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 298 | nador,ma -- query_url: http://api.openweathermap.org/data/2.5/weather?q=nador,ma&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 299 | nalut,ly -- query_url: http://api.openweathermap.org/data/2.5/weather?q=nalut,ly&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 300 | namibe,ao -- query_url: http://api.openweathermap.org/data/2.5/weather?q=namibe,ao&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 301 | namikupa,tz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=namikupa,tz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 302 | nanortalik,gl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=nanortalik,gl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 303 | nara,ml -- query_url: http://api.openweathermap.org/data/2.5/weather?q=nara,ml&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 304 | narsaq,gl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=narsaq,gl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 305 | naryan-mar,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=naryan-mar,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 306 | nassau,bs -- query_url: http://api.openweathermap.org/data/2.5/weather?q=nassau,bs&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 307 | natal,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=natal,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 308 | ndola,zm -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ndola,zm&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 309 | necochea,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=necochea,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 310 | neuquen,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=neuquen,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 311 | nkhata bay,mw -- query_url: http://api.openweathermap.org/data/2.5/weather?q=nkhata bay,mw&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 312 | nohar,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=nohar,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 313 | north bay,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=north bay,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 314 | nouadhibou,mr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=nouadhibou,mr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 315 | nove straseci,cz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=nove straseci,cz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 316 | nsanje,mw -- query_url: http://api.openweathermap.org/data/2.5/weather?q=nsanje,mw&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 317 | nurota,uz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=nurota,uz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 318 | nuuk,gl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=nuuk,gl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 319 | nyagan,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=nyagan,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 320 | nyakahanga,tz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=nyakahanga,tz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 321 | obidos,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=obidos,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 322 | of,tr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=of,tr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 323 | ofaqim,il -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ofaqim,il&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 324 | oktyabrskoye,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=oktyabrskoye,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 325 | olafsvik,is -- query_url: http://api.openweathermap.org/data/2.5/weather?q=olafsvik,is&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 326 | omidiyeh,ir -- query_url: http://api.openweathermap.org/data/2.5/weather?q=omidiyeh,ir&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 327 | ondjiva,ao -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ondjiva,ao&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 328 | opuwo,na -- query_url: http://api.openweathermap.org/data/2.5/weather?q=opuwo,na&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 329 | oranjestad,aw -- query_url: http://api.openweathermap.org/data/2.5/weather?q=oranjestad,aw&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 330 | ordynskoye,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ordynskoye,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 331 | oriximina,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=oriximina,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 332 | ostrovnoy,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ostrovnoy,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 333 | oum hadjer,td -- query_url: http://api.openweathermap.org/data/2.5/weather?q=oum hadjer,td&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 334 | paamiut,gl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=paamiut,gl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 335 | paidha,ug -- query_url: http://api.openweathermap.org/data/2.5/weather?q=paidha,ug&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 336 | paita,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=paita,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 337 | panaba,mx -- query_url: http://api.openweathermap.org/data/2.5/weather?q=panaba,mx&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 338 | panama city,us -- query_url: http://api.openweathermap.org/data/2.5/weather?q=panama city,us&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 339 | pangnirtung,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=pangnirtung,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 340 | pangoa,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=pangoa,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 341 | panguipulli,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=panguipulli,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 342 | paradwip,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=paradwip,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 343 | paragominas,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=paragominas,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 344 | paramonga,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=paramonga,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 345 | parana,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=parana,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 346 | parauna,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=parauna,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 347 | parrita,cr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=parrita,cr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 348 | parrsboro,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=parrsboro,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 349 | patos de minas,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=patos de minas,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 350 | paucartambo,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=paucartambo,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 351 | pedro ii,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=pedro ii,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 352 | peniche,pt -- query_url: http://api.openweathermap.org/data/2.5/weather?q=peniche,pt&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 353 | piacabucu,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=piacabucu,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 354 | pimentel,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=pimentel,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 355 | pirenopolis,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=pirenopolis,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 356 | pisco,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=pisco,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 357 | pitimbu,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=pitimbu,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 358 | plettenberg bay,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=plettenberg bay,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 359 | pokhara,np -- query_url: http://api.openweathermap.org/data/2.5/weather?q=pokhara,np&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 360 | ponta delgada,pt -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ponta delgada,pt&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 361 | ponta do sol,pt -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ponta do sol,pt&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 362 | ponta do sol,cv -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ponta do sol,cv&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 363 | porecatu,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=porecatu,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 364 | port alfred,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=port alfred,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 365 | port elizabeth,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=port elizabeth,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 366 | port elizabeth,vc -- query_url: http://api.openweathermap.org/data/2.5/weather?q=port elizabeth,vc&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 367 | port shepstone,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=port shepstone,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 368 | porto novo,cv -- query_url: http://api.openweathermap.org/data/2.5/weather?q=porto novo,cv&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 369 | porto velho,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=porto velho,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 370 | praia da vitoria,pt -- query_url: http://api.openweathermap.org/data/2.5/weather?q=praia da vitoria,pt&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 371 | presidencia roque saenz pena,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=presidencia roque saenz pena,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 372 | presidente epitacio,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=presidente epitacio,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 373 | presque isle,us -- query_url: http://api.openweathermap.org/data/2.5/weather?q=presque isle,us&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 374 | puerto del rosario,es -- query_url: http://api.openweathermap.org/data/2.5/weather?q=puerto del rosario,es&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 375 | puerto narino,co -- query_url: http://api.openweathermap.org/data/2.5/weather?q=puerto narino,co&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 376 | puerto pinasco,py -- query_url: http://api.openweathermap.org/data/2.5/weather?q=puerto pinasco,py&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 377 | punta arenas,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 378 | qaanaaq,gl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 379 | qarchi gak,af -- query_url: http://api.openweathermap.org/data/2.5/weather?q=qarchi gak,af&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 380 | qeshm,ir -- query_url: http://api.openweathermap.org/data/2.5/weather?q=qeshm,ir&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 381 | quatre cocos,mu -- query_url: http://api.openweathermap.org/data/2.5/weather?q=quatre cocos,mu&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 382 | quelimane,mz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=quelimane,mz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 383 | rabat,ma -- query_url: http://api.openweathermap.org/data/2.5/weather?q=rabat,ma&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 384 | raisio,fi -- query_url: http://api.openweathermap.org/data/2.5/weather?q=raisio,fi&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 385 | rakai,ug -- query_url: http://api.openweathermap.org/data/2.5/weather?q=rakai,ug&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 386 | ramon castilla,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ramon castilla,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 387 | raudeberg,no -- query_url: http://api.openweathermap.org/data/2.5/weather?q=raudeberg,no&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 388 | rawson,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=rawson,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 389 | rehoboth,na -- query_url: http://api.openweathermap.org/data/2.5/weather?q=rehoboth,na&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 390 | requena,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=requena,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 391 | ribeira grande,pt -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ribeira grande,pt&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 392 | riberalta,bo -- query_url: http://api.openweathermap.org/data/2.5/weather?q=riberalta,bo&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 393 | richards bay,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=richards bay,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 394 | rio gallegos,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=rio gallegos,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 395 | riyadh,sa -- query_url: http://api.openweathermap.org/data/2.5/weather?q=riyadh,sa&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 396 | rocha,uy -- query_url: http://api.openweathermap.org/data/2.5/weather?q=rocha,uy&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 397 | rodrigues alves,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=rodrigues alves,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 398 | rumonge,bi -- query_url: http://api.openweathermap.org/data/2.5/weather?q=rumonge,bi&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 399 | sabha,ly -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sabha,ly&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 400 | saint anthony,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=saint anthony,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 401 | saint george,bm -- query_url: http://api.openweathermap.org/data/2.5/weather?q=saint george,bm&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 402 | saint-augustin,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=saint-augustin,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 403 | saint-denis,re -- query_url: http://api.openweathermap.org/data/2.5/weather?q=saint-denis,re&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 404 | saint-francois,gp -- query_url: http://api.openweathermap.org/data/2.5/weather?q=saint-francois,gp&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 405 | saint-georges,gf -- query_url: http://api.openweathermap.org/data/2.5/weather?q=saint-georges,gf&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 406 | saint-joseph,re -- query_url: http://api.openweathermap.org/data/2.5/weather?q=saint-joseph,re&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 407 | saint-philippe,re -- query_url: http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 408 | sainte-rose,re -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sainte-rose,re&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 409 | sal rei,cv -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sal rei,cv&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 410 | salalah,om -- query_url: http://api.openweathermap.org/data/2.5/weather?q=salalah,om&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 411 | saldanha,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=saldanha,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 412 | salta,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=salta,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 413 | san andres,co -- query_url: http://api.openweathermap.org/data/2.5/weather?q=san andres,co&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 414 | san carlos de bariloche,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=san carlos de bariloche,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 415 | san cristobal,ec -- query_url: http://api.openweathermap.org/data/2.5/weather?q=san cristobal,ec&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 416 | san ignacio,bo -- query_url: http://api.openweathermap.org/data/2.5/weather?q=san ignacio,bo&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 417 | san jose de sisa,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=san jose de sisa,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 418 | san jose del guaviare,co -- query_url: http://api.openweathermap.org/data/2.5/weather?q=san jose del guaviare,co&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 419 | san juan,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=san juan,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 420 | san pedro,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=san pedro,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 421 | san rafael,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=san rafael,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 422 | san ramon,bo -- query_url: http://api.openweathermap.org/data/2.5/weather?q=san ramon,bo&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 423 | san-pedro,ci -- query_url: http://api.openweathermap.org/data/2.5/weather?q=san-pedro,ci&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 424 | santa marta de tormes,es -- query_url: http://api.openweathermap.org/data/2.5/weather?q=santa marta de tormes,es&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 425 | santa rosa,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=santa rosa,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 426 | santiago del estero,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=santiago del estero,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 427 | sao bento do sul,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sao bento do sul,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 428 | sao felix do xingu,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sao felix do xingu,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 429 | sao filipe,cv -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sao filipe,cv&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 430 | sao joao da barra,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sao joao da barra,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 431 | sao jose da coroa grande,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sao jose da coroa grande,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 432 | savannah bight,hn -- query_url: http://api.openweathermap.org/data/2.5/weather?q=savannah bight,hn&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 433 | scottsburgh,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=scottsburgh,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 434 | sechura,pe -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sechura,pe&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 435 | sena madureira,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sena madureira,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 436 | sept-iles,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sept-iles,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 437 | serro,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=serro,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 438 | shar,kz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=shar,kz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 439 | sikonge,tz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sikonge,tz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 440 | sinazongwe,zm -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sinazongwe,zm&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 441 | sindand,af -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sindand,af&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 442 | sirjan,ir -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sirjan,ir&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 443 | skjervoy,no -- query_url: http://api.openweathermap.org/data/2.5/weather?q=skjervoy,no&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 444 | soavinandriana,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=soavinandriana,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 445 | songea,tz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=songea,tz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 446 | souillac,mu -- query_url: http://api.openweathermap.org/data/2.5/weather?q=souillac,mu&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 447 | springbok,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=springbok,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 448 | springdale,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=springdale,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 449 | steinhausen,ch -- query_url: http://api.openweathermap.org/data/2.5/weather?q=steinhausen,ch&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 450 | stokmarknes,no -- query_url: http://api.openweathermap.org/data/2.5/weather?q=stokmarknes,no&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 451 | stornoway,gb -- query_url: http://api.openweathermap.org/data/2.5/weather?q=stornoway,gb&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 452 | suez,eg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=suez,eg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 453 | sumbe,ao -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sumbe,ao&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 454 | sur,om -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sur,om&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 455 | sussex,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=sussex,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 456 | tabas,ir -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tabas,ir&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 457 | tacuarembo,uy -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tacuarembo,uy&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 458 | takoradi,gh -- query_url: http://api.openweathermap.org/data/2.5/weather?q=takoradi,gh&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 459 | talcahuano,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=talcahuano,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 460 | tallahassee,us -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tallahassee,us&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 461 | talnakh,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=talnakh,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 462 | taltal,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=taltal,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 463 | tamandare,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tamandare,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 464 | taolanaro,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=taolanaro,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 465 | taoudenni,ml -- query_url: http://api.openweathermap.org/data/2.5/weather?q=taoudenni,ml&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 466 | tarija,bo -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tarija,bo&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 467 | tarudant,ma -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tarudant,ma&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 468 | tasiilaq,gl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 469 | teguldet,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=teguldet,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 470 | tekeli,kz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tekeli,kz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 471 | teodoro sampaio,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=teodoro sampaio,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 472 | tete,mz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tete,mz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 473 | thinadhoo,mv -- query_url: http://api.openweathermap.org/data/2.5/weather?q=thinadhoo,mv&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 474 | thompson,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=thompson,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 475 | tignere,cm -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tignere,cm&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 476 | tira sujanpur,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tira sujanpur,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 477 | toktogul,kg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=toktogul,kg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 478 | toliary,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=toliary,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 479 | torbay,ca -- query_url: http://api.openweathermap.org/data/2.5/weather?q=torbay,ca&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 480 | torres,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=torres,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 481 | touros,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=touros,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 482 | trairi,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=trairi,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 483 | trapani,it -- query_url: http://api.openweathermap.org/data/2.5/weather?q=trapani,it&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 484 | treinta y tres,uy -- query_url: http://api.openweathermap.org/data/2.5/weather?q=treinta y tres,uy&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 485 | trelew,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=trelew,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 486 | trincomalee,lk -- query_url: http://api.openweathermap.org/data/2.5/weather?q=trincomalee,lk&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 487 | tshela,cd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tshela,cd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 488 | tshikapa,cd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tshikapa,cd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 489 | tsienyane,bw -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tsienyane,bw&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 490 | tsihombe,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tsihombe,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 491 | tucano,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=tucano,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 492 | udaipura,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=udaipura,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 493 | uitenhage,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=uitenhage,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 494 | umea,se -- query_url: http://api.openweathermap.org/data/2.5/weather?q=umea,se&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 495 | umzimvubu,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=umzimvubu,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 496 | upernavik,gl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 497 | urucara,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=urucara,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 498 | ushirombo,tz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ushirombo,tz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 499 | ushuaia,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 500 | usinsk,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=usinsk,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 501 | ussel,fr -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ussel,fr&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 502 | ust-shonosha,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ust-shonosha,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 503 | ustyuzhna,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=ustyuzhna,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 504 | uvira,cd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=uvira,cd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 505 | vaasa,fi -- query_url: http://api.openweathermap.org/data/2.5/weather?q=vaasa,fi&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 506 | vagur,fo -- query_url: http://api.openweathermap.org/data/2.5/weather?q=vagur,fo&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 507 | valera,ve -- query_url: http://api.openweathermap.org/data/2.5/weather?q=valera,ve&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 508 | vallenar,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=vallenar,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 509 | valparaiso,cl -- query_url: http://api.openweathermap.org/data/2.5/weather?q=valparaiso,cl&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 510 | vangaindrano,mg -- query_url: http://api.openweathermap.org/data/2.5/weather?q=vangaindrano,mg&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 511 | vardo,no -- query_url: http://api.openweathermap.org/data/2.5/weather?q=vardo,no&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 512 | veinticinco de mayo,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=veinticinco de mayo,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 513 | vestmanna,fo -- query_url: http://api.openweathermap.org/data/2.5/weather?q=vestmanna,fo&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 514 | vestmannaeyjar,is -- query_url: http://api.openweathermap.org/data/2.5/weather?q=vestmannaeyjar,is&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 515 | victoria,sc -- query_url: http://api.openweathermap.org/data/2.5/weather?q=victoria,sc&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 516 | viedma,ar -- query_url: http://api.openweathermap.org/data/2.5/weather?q=viedma,ar&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 517 | vila franca do campo,pt -- query_url: http://api.openweathermap.org/data/2.5/weather?q=vila franca do campo,pt&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 518 | vila velha,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=vila velha,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 519 | vilhena,br -- query_url: http://api.openweathermap.org/data/2.5/weather?q=vilhena,br&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 520 | vredendal,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=vredendal,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 521 | vryburg,za -- query_url: http://api.openweathermap.org/data/2.5/weather?q=vryburg,za&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 522 | wahran,dz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=wahran,dz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 523 | warmbad,na -- query_url: http://api.openweathermap.org/data/2.5/weather?q=warmbad,na&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 524 | westport,ie -- query_url: http://api.openweathermap.org/data/2.5/weather?q=westport,ie&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 525 | wilmington,us -- query_url: http://api.openweathermap.org/data/2.5/weather?q=wilmington,us&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 526 | yabrud,sy -- query_url: http://api.openweathermap.org/data/2.5/weather?q=yabrud,sy&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 527 | yar-sale,ru -- query_url: http://api.openweathermap.org/data/2.5/weather?q=yar-sale,ru&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 528 | yavatmal,in -- query_url: http://api.openweathermap.org/data/2.5/weather?q=yavatmal,in&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 529 | yirol,sd -- query_url: http://api.openweathermap.org/data/2.5/weather?q=yirol,sd&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 530 | zamora,es -- query_url: http://api.openweathermap.org/data/2.5/weather?q=zamora,es&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 531 | zhanaozen,kz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=zhanaozen,kz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 532 | zharkent,kz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=zharkent,kz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
    Row index: 533 | zhezkazgan,kz -- query_url: http://api.openweathermap.org/data/2.5/weather?q=zhezkazgan,kz&units=imperial&APPID=b28cc4b4c0a1d1d9ff4c2d9e808f9a5a
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
      <td>abu dhabi</td>
      <td>ae</td>
      <td>2017-08-23 20:00:00</td>
      <td>54.37</td>
      <td>24.47</td>
      <td>89.60</td>
      <td>55.0</td>
      <td>20.0</td>
      <td>14.99</td>
    </tr>
    <tr>
      <th>1</th>
      <td>acarau</td>
      <td>br</td>
      <td>2017-08-23 21:19:52</td>
      <td>-40.12</td>
      <td>-2.89</td>
      <td>77.79</td>
      <td>81.0</td>
      <td>0.0</td>
      <td>18.14</td>
    </tr>
    <tr>
      <th>2</th>
      <td>acari</td>
      <td>pe</td>
      <td>2017-08-23 21:19:53</td>
      <td>-74.62</td>
      <td>-15.43</td>
      <td>46.20</td>
      <td>67.0</td>
      <td>0.0</td>
      <td>2.04</td>
    </tr>
    <tr>
      <th>3</th>
      <td>aconibe</td>
      <td>gq</td>
      <td>2017-08-23 21:19:53</td>
      <td>10.94</td>
      <td>1.30</td>
      <td>69.42</td>
      <td>98.0</td>
      <td>92.0</td>
      <td>2.15</td>
    </tr>
    <tr>
      <th>4</th>
      <td>adeje</td>
      <td>es</td>
      <td>2017-08-23 21:00:00</td>
      <td>-16.73</td>
      <td>28.12</td>
      <td>82.40</td>
      <td>88.0</td>
      <td>0.0</td>
      <td>8.05</td>
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


sns.regplot(x=x_axis, y=y_axis, color="magenta", marker="o", fit_reg=False, 
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
# weather.  Humidity doesn't seem to impact the bilding of cities as
# they are spread out relatively well with some concentrations.
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
