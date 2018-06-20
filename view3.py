import DBAccessor as dbac
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import datetime
from pytz import timezone

jp = timezone('Asia/Tokyo')

plotly.tools.set_credentials_file(username='kaihuu', api_key='znMv1Ngj0FwLt4HcoZbb')

speed = dbac.DBAccessor.SpeedDataQuery()

district = dbac.DBAccessor.TimeDistinctDataQuery()

nptime = np.array(district)
npspeed = np.array(speed)
    

datatypes = ['LEAFSPY_Speed1','LEAFSPY_Speed2', 'AT570', 'BEAT', 'Nexus7']

data = []
# make data
for datatype in datatypes:
    if datatype == 'LEAFSPY_Speed1':
        xdata = nptime[:, 0]
        ydata = nptime[:, 1]
    elif datatype == 'LEAFSPY_Speed2':
        xdata = nptime[:, 0]
        ydata = nptime[:, 2]
    elif datatype == 'AT570':
        npspeed570 = npspeed[npspeed[:,1] == 16]
        xdata = npspeed570[:,0]
        ydata = npspeed570[:,2]
    elif datatype == 'BEAT':
        npspeedBEAT = npspeed[npspeed[:,1] == 28]
        xdata = npspeedBEAT[:,0]
        ydata = npspeedBEAT[:,2]
    elif datatype == 'Nexus7':
        npspeedBEAT = npspeed[npspeed[:,1] == 18]
        xdata = npspeedBEAT[:,0]
        ydata = npspeedBEAT[:,2]


    trace = go.Scatter(
                x=xdata,
                y=ydata,
                name = datatype,
                opacity = 0.8)

    data.append(trace)

layout = dict(
    title = "Speed Data",
    font = dict(size=30)
)

fig = dict(data=data, layout=layout)
py.plot(fig)