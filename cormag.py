import csv

import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 18}

plt.rc('font', **font)


#정보관 inout
x11 = [0.22,0.12]
y11 = [28.62,17.84]
yy11 = [-48.11,-49.26]

#plt.plot(x11, y11, color="#2E2E2E", linewidth=3, linestyle="-", label="In_Out S6_white")
#plt.plot(x11, yy11, color="#B7950B", linewidth=3, linestyle="-", label="In_Out S6_gold")



#정보관 outin
x12 = [-0.22,0.52]
y12 = [-51.22,-79.86]
yy12 = [-79.86,-71.10]

#plt.plot(x12, y12, color="#585858", linewidth=3, linestyle=":", label="Out_In S6_white")
#plt.plot(x12, yy12, color="#B7950B", linewidth=3, linestyle="-", label="Out_In S6_gold")

#미융 inout
x21 = [0.22,-0.05]
y21 = [-30.79,-37.98]
yy21 = [-8.77,-10.67]

#plt.plot(x21, y21, color="#2E2E2E", linewidth=3, linestyle="-", label="In_Out S6_white")
#plt.plot(x21, yy21, color="#B7950B", linewidth=3, linestyle="-", label="In_Out S6_gold")

#미융 outin
x22 = [-0.28,0.63]
y22 = [-24.77,-22.01]
yy22 = [-35.81,-47.35]

plt.plot(x22, y22, color="#2E2E2E", linewidth=3, linestyle="-", label="Out_In S6_white")
plt.plot(x22, yy22, color="#585858", linewidth=3, linestyle=":", label="Out_In S6_gold")




plt.legend(bbox_to_anchor=(0.75, 0.81), loc=2, borderaxespad=0.)

#plt.legend(loc='upper right', frameon=False)

#label 표시
plt.xlabel(u'correlation',fontsize=20,weight='bold')
plt.ylabel(u'magnetometer (uT)',fontsize=20,weight='bold') #단위는 마이크로 테슬라

plt.show()