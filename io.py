import requests as r
import pandas as pd
import panel as pn
from .params import *

pn.extenstion('ipywidgets')


class Getter(Reactor, Generic):
    sdf3 = df.spatial.from_xy(df=df, x_column="long", y_column="lat")
    df = Reactor.reactors
 


    @param.depends('conti', watch=True)
    def _update_coords(self):
        lat, lon = self.plant[self.df]
        self.param['lat', 'lon'].objects = lat, lon  

    def
        return location

def _get_wind()
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

    split_top = getint[:7]
    split_bot = getint[7:]
    datatable_atmo = [split_top, split_bot]

  