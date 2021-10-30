#%%
from typing_extensions import ParamSpec
import holoviews as hv
import holoviews.operation.datashader as hd
import bokeh as bk
import rioxarray as rxr
import geoviews as gv
import geoviews.feature as gf
import pandas as pd
import numpy as np
from geoviews import opts
from cartopy import crs
import param
import datetime as dt
import panel as pn

pn.extension('ipywidgets')
gv.extension('bokeh','matplotlib')


#%%
dataarray = rxr.open_rasterio('./dose.tif')
df = dataarray[0].to_pandas()
df.iloc[0:20, 0:20]

# %%
names = []
df = pd.read_csv('in.csv')

plant = pn.widgets.Select(name="plant", options=df['plantname'].tolist())
plant

# %%
reactor=df.loc[df['plantname'].str.contains(plant.value, case=True)]
reactor
# %%
.assign(plant=lambda x: pn.widgets.Select(options=x['a'].tolist()))

# %%

column_names = {'name': 'a', 'latitude': 'la', 'longitude': 'lo'}
reactor = (
            df 
            .rename(columns=column_names)
            .set_index('a', append=True)     
)


# %%
df = pd.read_csv('in.csv', index_col=0)
plant = pn.widgets.Select(name="plant", options=(df.index).tolist())
plant
# %%
r = df.loc[df.index == plant.value]
print(r.latitude)
# %%
df.iloc[df.index == plant.value]
# %%
df.loc[df['name'].str.contains('plant.value')==True] 
# %
# %%
base = df.index.get_indexer_for((df[plant.value].index))
# %%
print(base)
# %%
plant.value
# %%
e =[str(r.latitude), str(r.longitude)]
# %%
print(e)
# %%
from params import Reactor


df = Reactor.reactors
#lat, lon = Reactor.coord.df

#%%
df
# %%
df.index.get_object


# %%
