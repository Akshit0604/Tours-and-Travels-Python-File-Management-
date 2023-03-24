#hyderabad
import numpy as np
import matplotlib.pyplot as pl
x=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
y=[11,12,14,24,22,5,6,9,18,26,25,10]
pl.xlabel("months")
pl.ylabel("average visitors")
pl.bar(x,y,width=0.3,color='r')
pl.show()
