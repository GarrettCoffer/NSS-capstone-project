# For 2nd gathering laptop (on a different network and in a different house)

import requests
import json
import pandas as pd
import time

endpoint = 'https://services2.arcgis.com/HdTo6HJqh92wn4D8/arcgis/rest/services/Metro_Nashville_Police_Department_Active_Dispatch_Table_view/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson'

i = 0

while True:
    i += 1
    print(f"\rIteration: {i}", end="")
    try :
        response = requests.get(endpoint)
        if(response.status_code == 200) :
            res = response.json()
            active_dispatch = pd.DataFrame(columns = ['incident_type_code','incident_type_name','call_received_time','location',
                                             'location_description','city_name','last_updated'])
            for incident in res['features'] :
                new_row = {'incident_type_code': incident['properties']['IncidentTypeCode'],
                           'incident_type_name': incident['properties']['IncidentTypeName'],
                           'call_received_time': incident['properties']['CallReceivedTime'],
                           'location': incident['properties']['Location'],
                           'location_description': incident['properties']['LocationDescription'],
                           'city_name': incident['properties']['CityName'],
                           'last_updated': incident['properties']['LastUpdated']}
                active_dispatch.loc[len(active_dispatch)] = new_row
            if len(active_dispatch) > 0 :
                last_updated = active_dispatch.loc[0,'last_updated']
                active_dispatch.to_csv('/active_dispatch/' + str(last_updated) + '.csv', index=False)
        else :
            print('')
            print('Error!  Response : ' + str(response))
    except requests.exceptions.RequestException as e:
        print('')
        print('Error!  Requests error : ' + str(e))
    except:
	print('')
        print('Something else went wrong')
    time.sleep(360) #360 checks every 6 minutes