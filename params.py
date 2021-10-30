"""parameters for radplume, initialized in KMS with simple conversion support"""
import pandas as pd
import param


class Reactor(param.Parameterized):
    """Physical attributes of Nuclear Reactor"""
    
    reactors   = param.DataFrame(pd.read_csv('in.csv',index_col='name'), doc="name, lat, long")
    name       = param.Selector(objects=[], instantiate=True, doc ="reactor")
    coord      = param.XYCoordinates(doc="used for lat/long")
    height_sm  = param.Range(10, bounds=(0,25), doc="stack height or number hours")

class Release(param.Parameterized):
    """Source release factors""" 
    
    holdup     = param.Number(2, bounds=(5, 120), step=5, doc="hold-up time 5 minute steps") 
    sources    = param.Selector(options=['Noble Gas','Iodine','Particulate'])
    duration   = param.Number(bounds=(0,24), doc="time of release in hours") 

class Atmosphere(param.Parameterized):
    """Physical attributes of the atmosphere"""

    windspeed  = param.Number(bounds=(0.00, 25.00), doc="speed of wind at 10m")
    bearing    = param.Range(bounds=(0,2*np.pi), doc="API pull will set this")
    lid        = param.Integer(300, bounds=(300,5000), step=100, doc="mixing lid height step of 100m")
    stability  = param.Selector(options=['A','B','C','D','E','F','G'], doc="atmospheric stability class")

class Generic(param.Parameterized):
    _countries = param.ClassSelector{'North America': ['United States', 'Canada', 'Mexico']}

    timestamps = []    
    txtbool    = param.String(default="true", doc="for API true values")
    darklight  = param.Boolean(default=True, doc="theme selector dark=default=True")



