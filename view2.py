import DBAccessor as dbac
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from IPython.display import display, HTML
import pandas as pd
import numpy as np
import datetime

init_notebook_mode(connected=True)

speed = dbac.DBAccessor.SpeedDataQuery()

district = dbac.DBAccessor.TimeDistinctDataQuery()

nptime = np.array(district)
npspeed = np.array(speed)

datatypes = ['LEAFSPY_Speed1','LEAFSPY_Speed2', 'AT570', 'BEAT']

# make figure
figure = {
    'data': [],
    'layout': {},
    'frames': []
}

min = district[0][0]

print(min)

# fill in most of layout
figure['layout']['xaxis'] = {'range': [min, min + datetime.timedelta(minutes = 1)], 'title': 'Time'}
figure['layout']['yaxis'] = {'title': 'Speed'}
figure['layout']['hovermode'] = 'closest'
figure['layout']['sliders'] = {
    'args': [
        'transition', {
            'duration': 400,
            'easing': 'cubic-in-out'
        }
    ],
    'initialValue': district[0],
    'plotlycommand': 'animate',
    'values': district[0],
    'visible': True
}

figure['layout']['updatemenus'] = [
    {
        'buttons': [
            {
                'args': [None, {'frame': {'duration': 50, 'redraw': False},
                         'fromcurrent': True, 'transition': {'duration': 30, 'easing': 'quadratic-in-out'}}],
                'label': 'Play',
                'method': 'animate'
            },
            {
                'args': [[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'immediate',
                'transition': {'duration': 0}}],
                'label': 'Pause',
                'method': 'animate'
            }
        ],
        'direction': 'left',
        'pad': {'r': 10, 't': 87},
        'showactive': False,
        'type': 'buttons',
        'x': 0.1,
        'xanchor': 'right',
        'y': 0,
        'yanchor': 'top'
    }
]
sliders_dict = {
    'active': 0,
    'yanchor': 'top',
    'xanchor': 'left',
    'currentvalue': {
        'font': {'size': 20},
        'prefix': 'Time:',
        'visible': True,
        'xanchor': 'right'
    },
    'transition': {'duration': 300, 'easing': 'cubic-in-out'},
    'pad': {'b': 10, 't': 50},
    'len': 0.9,
    'x': 0.1,
    'y': 0,
    'steps': []
}

# make data
for datatype in datatypes:
    if datatype == 'LEAFSPY_Speed1':
        nptimeSpeed1 = nptime[nptime[:,0] >= min]
        nptimeSpeed1 = nptimeSpeed1[nptimeSpeed1[:,0] <= min + datetime.timedelta(minutes = 1)]
        xdata = nptimeSpeed1[:, 0]
        ydata = nptimeSpeed1[:, 1]
    elif datatype == 'LEAFSPY_Speed2':
        nptimeSpeed2 = nptime[nptime[:,0] >= min]
        nptimeSpeed2 = nptimeSpeed2[nptimeSpeed2[:,0] <= min + datetime.timedelta(minutes = 1)]
        xdata = nptimeSpeed2[:, 0]
        ydata = nptimeSpeed2[:, 2]
    elif datatype == 'AT570':
        npspeed570 = npspeed[npspeed[:,1] == 16]
        npspeed570 = npspeed570[npspeed570[:,0] >= min]
        npspeed570 = npspeed570[npspeed570[:,0] <= min + datetime.timedelta(minutes = 1)]
        xdata = npspeed570[:,0]
        ydata = npspeed570[:,2]
    elif datatype == 'BEAT':
        npspeedBEAT = npspeed[npspeed[:,1] == 28]
        npspeedBEAT = npspeedBEAT[npspeedBEAT[:,0] >= min]
        npspeedBEAT = npspeedBEAT[npspeedBEAT[:,0] <= min + datetime.timedelta(minutes = 1)]
        xdata = npspeedBEAT[:,0]
        ydata = npspeedBEAT[:,2]
    data_dict = {
        'x': xdata,
        'y': ydata,
        'mode': 'lines+markers',
        'name': datatype
    }
    figure['data'].append(data_dict)

# make frames
for i, time in enumerate(district):
    frame = {'data': [],'layout': {'xaxis': {'range': [time[0], time[0] + datetime.timedelta(minutes=1)],
     'title': 'Time'}}, 'name': str(time[0])}
    for datatype in datatypes:
        if datatype == 'LEAFSPY_Speed1':
            nptimeSpeed1 = nptime[nptime[:,0] >= time[0]]
            nptimeSpeed1 = nptimeSpeed1[nptimeSpeed1[:,0] <= time[0] + datetime.timedelta(minutes = 1)]
            xdata = nptimeSpeed1[:, 0]
            ydata = nptimeSpeed1[:, 1]
        elif datatype == 'LEAFSPY_Speed2':
            nptimeSpeed2 = nptime[nptime[:,0] >= time[0]]
            nptimeSpeed2 = nptimeSpeed2[nptimeSpeed2[:,0] <= time[0] + datetime.timedelta(minutes = 1)]
            xdata = nptimeSpeed2[:, 0]
            ydata = nptimeSpeed2[:, 2]
        elif datatype == 'AT570':
            npspeed570 = npspeed[npspeed[:,1] == 16]
            npspeed570 = npspeed570[npspeed570[:,0] >= time[0]]
            npspeed570 = npspeed570[npspeed570[:,0] <= time[0] + datetime.timedelta(minutes = 1)]
            xdata = npspeed570[:,0]
            ydata = npspeed570[:,2]
        elif datatype == 'BEAT':
            npspeedBEAT = npspeed[npspeed[:,1] == 28]
            npspeedBEAT = npspeedBEAT[npspeedBEAT[:,0] >= time[0]]
            npspeedBEAT = npspeedBEAT[npspeedBEAT[:,0] <= time[0] + datetime.timedelta(minutes = 1)]
            xdata = npspeedBEAT[:,0]
            ydata = npspeedBEAT[:,2]
        data_dict = {
            'x': xdata,
            'y': ydata,
            'mode': 'lines+markers',
            'name': datatype
        }
        frame['data'].append(data_dict)

    figure['frames'].append(frame)

    slider_step = {'args': [
        [time[0]],
        {'frame': {'duration': 30, 'redraw': False},
         'mode': 'immediate',
       'transition': {'duration': 30}}
     ],
     'label': time[0],
     'method': 'animate'}
    sliders_dict['steps'].append(slider_step)


figure['layout']['sliders'] = [sliders_dict]

plot(figure)