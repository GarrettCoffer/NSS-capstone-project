# NSS-capstone-project

This is the collection of notebooks for Garrett Coffer's 2025 capstone project for Nashville Software School.

---

## active_dispatch_json_extract.ipynb  
>type: Jupyter Source File  
Being run every 6 minutes since 3/27/2025 to collect the Active Dispatch police data from data.nashville.gov  
url: https://services2.arcgis.com/HdTo6HJqh92wn4D8/arcgis/rest/services/Metro_Nashville_Police_Department_Active_Dispatch_Table_view/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson  
output: ../data/active_dispatch/[time code].csv

## active_dispatch_combine_and_process.ipynb  
>type: Jupyter Source File  
Run to stitch the active dispatch tables together.  
input: ../data/active_dispatch/[time code].csv  
output: ../data/active_dispatch.csv  

## active_dispatch_downloader.py  
>type: Python file  
Similar to active_dispatch.ipynb, but a py file that is run in the command line.  This is being run on a different laptop on a different network (thanks Mom!) to help the integrity of the collection process, even if my wifi goes down for maintenance for 30 minutes.  
output (slightly different from the .ipynb version): /active_dispatch/[time code].csv

## mnpd_service_calls_combine_and_process.ipynb  
>type: Jupyter Source File  
Run to stitch the MNPD data together (in years from 2018-2024, and 2025_ytd).  
input: ../data/mnpd_calls_for_service/[year].csv  
output: ../data/mnpd_calls_for_service.csv  

## noaa_api_extract.ipynb  
>type: Jupyter Source File  
This is to collect NOAA weather data from 1/1/2018 - 3/31/2025 through their API.  This calls for their temperature max, temperature min, and precipitation reported from station USW00013897 (the BNA / Nashville International Airport station)  
url: https://www.ncei.noaa.gov/access/services/data/v1?dataset=daily-summaries&stations=USW00013897&startDate=2020-01-01&endDate=2025-03-31&dataTypes=TMAX,TMIN,PRCP&units=standard&format=json  
output: ../data/noaa_weather_data.csv

## nws_3_day_webscrape.ipynb  
>type: Jupyter Source File  
This is set up to automatically run every day, 86400 seconds, from 3/29/2025 forward.  It only needs to be run every 2 or 3 days.  This is to collect real-time historic weather for Nashville - hour-by-hour precipitation and temperatures for the past 3 days, so the data collected is from 3/27/2025 onward.  
url: https://forecast.weather.gov/data/obhistory/KBNA.html  
output: ../data/nws_past_3/[code for report day and time].csv

## nws_combine_and_process.ipynb  
>type: Jupyter Source File  
Run to stitch the webscraped NWS data together (collected 3 days at a time).  
input: ../data/nws_past_3/[code for report day and time].csv  
output: ../data/nws_weather_data.csv  

## tencodes_webscrape.ipynb  
>type: Jupyter Source File  
Used to scrape police "Ten Codes" descriptions  
url: https://wiki.radioreference.com/index.php/Davidson_County_(TN)  
output: ../data/tencodes.csv

## titans_webscrape.ipynb  
>type: Jupyter Source File  
Used to scrape 2018 - 2024 data about the Titans home games.  
url: https://www.tennesseetitans.com/schedule/[year]/  
output: ../data/titans_games/titans_[year].csv

## weather_gov_webscrape.ipynb  
>type: Jupyter Source File  
Used Selenium plugin to scrape weather.gov for hour-by-hour values from since 1/1/2018.  Scraping in 2 batches per month.  
url: https://www.weather.gov/wrh/timeseries?site=KBNA&hours=500&units=english&chart=off&headers=on&obs=tabular&hourly=true&pview=standard&font=12&history=yes&start=20180101&end=20180115&plot=  
output: ../data/weather_gov/weather_gov[yyyymmdd]-[yyyymmdd].csv

## weather_gov_combine_and_process.ipynb  
>type: Jupyter Source File  
Run to stitch the webscraped Weather.gov data together (collected in 2 batches per month).  
input: ../data/weather_gov/weather_gov[yyyymmdd]-[yyyymmdd].csv  
output: ../data/weather_gov.csv  

## other data sources and files:


## Metro Nashville Police Department Calls for Service  
>source: data.nashville.gov  
url: https://datanashvillegov-nashville.hub.arcgis.com/search?categories=%252Fcategories%252Fpublic%2520safety&collection=Dataset&sort=Title%7Ctitle%7Casc