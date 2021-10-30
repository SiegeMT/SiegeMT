# library imports
import prams
import numpy as np
import pandas as pd
import holoviews as hv
hv.extension('bokeh', logo=False)
import panel as pn


file = 'ted-rascal.csv'
ins = 'in.csv'

def main():
    df = pd.read_csv(ins)
    reactor = pn.widgets.AutocompleteInput(name='Reactor selection', options=df['plantName'], placeholder='Palo Verde')
    latitude = pn.widgets.Select(name='latitude', options=df['latitude'])
    longitude = pn.widgets.Select(name='longitude', options=df['longitude'])



reactor.value