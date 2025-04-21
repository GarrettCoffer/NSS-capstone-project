# Nashville Police Dispatch and Weather Project

This is the collection of notebooks for Garrett Coffer's 2025 capstone project for Nashville Software School.

## Dashboard
[Power BI Dashboard](https://app.powerbi.com/view?r=eyJrIjoiMDMxZDU5NDUtMWFhMi00MTk4LTk5ODEtODJmNmFhNTMyZDEwIiwidCI6IjEwMWRhNTg3LTE4NDMtNGY1Mi04YjhhLTE3YjA2OWM2NmQzMyIsImMiOjJ9)

## Motivation
I was intrigued by the real-time active dispatch reports from data.nashville.gov, and thought that working with it could present an interesting challenge and fuel some interesting questions.  A real-time data pipeline is what sparked my interest.  My goal is to work with that data in a meaningful way, by combining it with archived police call data and weather data.

## Data Questions  
How does Nashville police call data compare over the last several years?  Additionally, how do weather events such as precipitation, wind, storms, or temperature fluctuations influence the frequency and nature of police calls?

## Data Sources
[data.nashville.gov](data.nashville.gov) (CSV download) for police call data from 1/1/2018-4/10/2025  
www.weather.gov (Selenium web scraping) for weather data from 1/1/2018-4/10/2025  
[data.nashville.gov](data.nashville.gov) for real-time active dispatch data (API)  

---

## active_dispatch_json_extract.ipynb  
>type: Jupyter Source File  
Being run every 6 minutes since 3/27/2025 to collect the Active Dispatch police data from data.nashville.gov  
[link to url](https://services2.arcgis.com/HdTo6HJqh92wn4D8/arcgis/rest/services/Metro_Nashville_Police_Department_Active_Dispatch_Table_view/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson)  
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

## processomg.ipynb  
>type: Jupyter Source File  
Run to do more processing on all the other files (as a last step before importing into Power BI).  Calculates sums, averages, etc.  Flags storm days and hours.  Merges with dispatch codes.  Combines 4.5 million records from the MNPD calls into 1 daily summaries file.  
input: ../data/mnpd_calls_for_service/[year].csv  
output: ../data/mnpd_calls_for_service.csv  

## mnpd_service_calls_combine_and_process.ipynb  
>type: Jupyter Source File  
Run to stitch the MNPD data together (in years from 2018-2024, and 2025_ytd).  
input: ../data/mnpd_calls_for_service/[year].csv  
output: ../data/mnpd_calls_for_service.csv  

## tencodes_webscrape.ipynb  
>type: Jupyter Source File  
Used to scrape police "Ten Codes" descriptions.  I did further combining in Excel, with tencode descriptions extracted from the active dispatch and mnpd tables.  
url: https://wiki.radioreference.com/index.php/Davidson_County_(TN)  
output: ../data/tencodes.csv  

## weather_gov_webscrape.ipynb  
>type: Jupyter Source File  
Used Selenium plugin to scrape weather.gov for hour-by-hour values from since 1/1/2018.  Scraping in 2 batches per month.  
[link to url](https://www.weather.gov/wrh/timeseries?site=KBNA&hours=500&units=english&chart=off&headers=on&obs=tabular&hourly=true&pview=standard&font=12&history=yes&start=20180101&end=20180115&plot=)  
output: ../data/weather_gov/weather_gov[yyyymmdd]-[yyyymmdd].csv

## weather_gov_combine_and_process.ipynb  
>type: Jupyter Source File  
Run to stitch the webscraped Weather.gov data together (collected in 2 batches per month).  
input: ../data/weather_gov/weather_gov[yyyymmdd]-[yyyymmdd].csv  
output: ../data/weather_gov.csv  

## other data sources and files:

## Metro Nashville Police Department Calls for Service  
>source: data.nashville.gov  
[link to url](https://datanashvillegov-nashville.hub.arcgis.com/search?categories=%252Fcategories%252Fpublic%2520safety&collection=Dataset&sort=Title%7Ctitle%7Casc)