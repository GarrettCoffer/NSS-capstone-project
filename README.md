# NSS-capstone-project

This is the collection of notebooks for Garrett Coffer's 2025 capstone project for Nashville Software School.


## active_dispatch.ipynb
type: Jupyter Source File
Being run every 6 minutes since 3/27/2025 to collect the Active Dispatch police data from data.nashville.gov
url: https://services2.arcgis.com/HdTo6HJqh92wn4D8/arcgis/rest/services/Metro_Nashville_Police_Department_Active_Dispatch_Table_view/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson
output: ../data/active_dispatch/[time code].csv

## active_dispatch_downloader.py
type: Python file
Same as above, but a py file that is run in the command line.  This is being run on a different laptop on a different network (thanks Mom!) to help the integrity of the collection process, even if my wifi goes down for maintenance for 30 minutes.
slightly different output: /active_dispatch/[time code].csv

## API - NOAA.ipynb
type: Jupyter Source File
This is to collect NOAA weather data from 1/1/2018-3/31/2025 through their API.
url: https://www.ncei.noaa.gov/access/services/data/v1?dataset=daily-summaries&stations=USW00013897&startDate=2020-01-01&endDate=2025-03-31&dataTypes=TMAX,TMIN,PRCP&units=standard&format=json (TBD)
output: TBD

## webscraping_nws_past_3_days.ipynb
type: Jupyter Source File
This is set up to automatically run every day, 86400 seconds, from 3/29/2025 forward.  It only needs to be run every 2 or 3 days.  This is to collect real-time historic weather for Nashville - hour-by-hour precipitation and temperatures for the past 3 days, so the data collected is from 3/27/2025 onward.
url: https://forecast.weather.gov/data/obhistory/KBNA.html
output: ../data/nws_past_3/[code for report day and time].csv

## webscraping_titans.ipynb
type: Jupyter Source File
Used to scrape 2018 - 2024 data about the Titans home games.
url: https://www.tennesseetitans.com/schedule/[year]/
output: ../data/titans_games/titans_[year].csv


## other data sources and files:


## Metro Nashville Police Department Calls for Service
source: data.nashville.gov
url: https://datanashvillegov-nashville.hub.arcgis.com/search?categories=%252Fcategories%252Fpublic%2520safety&collection=Dataset&sort=Title%7Ctitle%7Casc