import DBAccessor as dbac
import pandas as pd
import numpy as np
import datetime
from pytz import timezone

jp = timezone('Asia/Tokyo')


speed = dbac.DBAccessor.SpeedDataQuery2()

#district = dbac.DBAccessor.TimeDistinctDataQuery()

#nptime = np.array(district)
npspeed = np.array(speed)
    

datatypes = ['AT570', 'BEAT', 'Nexus7', 'X_Performance']

data = []
# make data
for datatype in datatypes:
    if datatype == 'AT570':
        npspeed570 = npspeed[npspeed[:,1] == 16]
        #xdata570 = npspeed570[:,0]
        #ydata570 = npspeed570[:,2]
        error_leaf1_570 = np.sqrt(np.mean((npspeed570[:,2] - npspeed570[:,3])**2))
        error_leaf2_570 = np.sqrt(np.mean((npspeed570[:,2] - npspeed570[:,4])**2))
    elif datatype == 'BEAT':
        npspeedBEAT = npspeed[npspeed[:,1] == 28]
        #xdataBEAT = npspeedBEAT[:,0]
        #ydataBEAT = npspeedBEAT[:,2]
        error_leaf1_BEAT = np.sqrt(np.mean((npspeedBEAT[:,2] - npspeedBEAT[:,3])**2))
        error_leaf2_BEAT = np.sqrt(np.mean((npspeedBEAT[:,2] - npspeedBEAT[:,4])**2))
    elif datatype == 'Nexus7':
        npspeedNexus7 = npspeed[npspeed[:,1] == 18]
        #xdataNexus7 = npspeedNexus7[:,0]
        #ydataNexus7 = npspeedNexus7[:,2]
        error_leaf1_Nexus7 = np.sqrt(np.mean((npspeedNexus7[:,2] - npspeedNexus7[:,3])**2))
        error_leaf2_Nexus7 = np.sqrt(np.mean((npspeedNexus7[:,2] - npspeedNexus7[:,4])**2))
    elif datatype== 'X_Performance':
        npspeedXPerformance = npspeed[npspeed[:, 1] == 29]
        error_leaf1_XPerformance = np.sqrt(np.mean((npspeedXPerformance[:,2] - npspeedXPerformance[:,3])**2))
        error_leaf2_XPerformance = np.sqrt(np.mean((npspeedXPerformance[:,2] - npspeedXPerformance[:,4])**2))


print(error_leaf1_570)
print(error_leaf2_570)
print(error_leaf1_BEAT)
print(error_leaf2_BEAT)
print(error_leaf1_Nexus7)
print(error_leaf2_Nexus7)
print(error_leaf1_XPerformance)
print(error_leaf2_XPerformance)
