from django.db import models


class Atmosphere(models.Model):
    a = 'A' 
    b = 'B'
    c = 'C'
    d = 'D'
    e = 'E'
    d = 'D'
    e = 'E'
    f = 'F'


    
    stability = 
    wind_vector =
    height_release =
    height_mixinglid =


class ReactorAttrs(models.Model):
    reactor = models.CharField(max_length=50)
    latitude = models.DecimalField(decimal_places=5)
    longitude = models.DecimalField(decimal_places=5)


df = pd.read_csv('in.csv')
plant = pn.widgets.Select(name="plant", options=df['plantname'].tolist())
reactor=df.loc[df['plantname'].str.contains(plant.value, case=True)]