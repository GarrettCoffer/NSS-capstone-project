# Nashville Police Dispatch and Weather Project

This is the collection of notebooks for Garrett Coffer's 2025 capstone project for Nashville Software School.

## Dashboard
[Power BI Dashboard](https://app.powerbi.com/view?r=eyJrIjoiMDMxZDU5NDUtMWFhMi00MTk4LTk5ODEtODJmNmFhNTMyZDEwIiwidCI6IjEwMWRhNTg3LTE4NDMtNGY1Mi04YjhhLTE3YjA2OWM2NmQzMyIsImMiOjJ9)

## Motivation
My inspiration for this project is that I was intrigued by the active dispatch reports from data.nashville.gov, and thought working with that data could present an interesting challenge and fuel some good questions.  The data shows a real-time snapshot (about every 8-15 minutes) of active emergencies where police are currently responding.  My goal was to work with that data in a meaningful way, by collecting it over a period of several weeks and combining it with archived police call data and weather data to look for patterns.

## Data Questions  
- How does Nashville police call data compare over the last several years?  
- How do weather events such as precipitation, wind, storms, or temperature fluctuations influence the frequency and nature of police calls?
- What effect did the recent big storm system on April 5, 2025 have on the emergency calls?

## Data Sources
>[data.nashville.gov](https://www.nashville.gov/departments/police/online-resources/active-dispatches) (API) for real-time active dispatch data  
3/27/2025 - 4/13/2025  
Real-time data about the current active major incident calls for service received by the Emergency Communications Center dispatched to Metro Nashville Police Department.

>[data.nashville.gov](https://datanashvillegov-nashville.hub.arcgis.com/datasets/Nashville::metro-nashville-police-department-calls-for-service/about) (CSV download) for police call data  
1/1/2018-4/13/2025  
Details about emergency and non-emergency calls for Metro Nashville Police Department service received by the Emergency Communications Center.

>www.weather.gov (Selenium web scraping) for weather data  
1/1/2018-4/13/2025  

## Challenges
- Weather.gov uses dynamic tables, so I learned about Selenium to web scrape the non-static weather data
- The Active Dispatch data refreshes about every 8-15 minutes, so I needed to set up a python script to run every 6 minutes to gather the data.
- The police call data had over 5 million rows in total, broken into multiple years.  That had to be worked with in batches.
- The police call data and active dispatch data had many separate CSV files that had to be combined and processed to perform analysis.

## Conclusion  
- Some events like theft and disorderly conduct follow seasonal cycles and weekly cycles  
- Weather does have an impact on the nature of police calls
  - Precipitation decreases theft, but increases vehicle accidents, hazards, and disorderly conduct
  - Days with 4 or more storm hours see a more extreme shift of increased vehicle accidents, hazards, and disorderly conduct
  - Temperature extremes decrease the frequency of police calls
- The recent storm on April 5 generated a lot of emergency calls, mostly from downed power lines and trees.  There were more emergency calls during the single highest-impact hour than there are on average for an entire day