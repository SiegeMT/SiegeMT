'''
inputs.py defines a few updating functions for radplume
this file updates the wind dataframe for the ui and program
'''
# %%
import requests as r
import pandas as pd
import panel as pn
from prams import Uset


pn.extenstion()
# %%
class Getter(Uset):
    df = Uset.dataframe
    plant = Uset.name
    lat = Uset.lat 
    long = Uset.long


    def __init__(self,**params):
        super(Getter, self).__init__(**params)
        reactor = pn.widgets.AutocompleteInput(name='Reactor selection', options=df['plantName'], placeholder='Palo Verde')
        latitude = pn.widgets.Select(name='latitude', options=df['latitude'])
        longitude = pn.widgets.Select(name='longitude', options=df['longitude'])
        location = pn.Row(reactor, latitude, longitude)

    return location
    
# %%
def _get_wind():
json = {'w3':'sfcwind',
        'w4':'sky',
        'w6':'rh',
        'w14':'ft20w',        
        'AheadHour':'0',
        'Submit':'Submit',
        'FcstType':'digital',
        'textField1':latitude,
        'textField2':longitude,
        'site':'psr'}

URL = 'http://forecast.weather.gov/MapClick.php?'
rep = r.get(URL)

response = r.get(URL, json)
data = pd.read_html(response.text)
df = pd.DataFrame(data[7])
getint = df.dropna(axis=0, how='any', thresh=None)



    ''' Used for API pulling wind ''''
    response = r.get(base_url, json)
    data = pd.read_html(response.text)
    df = pd.DataFrame(data[7])
    getint = df.dropna(axis=0, how='any', thresh=None)

    split_top = getint[:7]
    split_bot = getint[7:]
    datatable_atmo = [split_top, split_bot]

#df.set_index(keys, drop=True, append=False, inplace=False, verify_integrity=False)
