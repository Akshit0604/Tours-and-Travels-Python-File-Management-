#pune
import numpy as np
import matplotlib.pyplot as pl
x=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
y=[16,18,11,10,11,12,6,7,18,26,25,16]
pl.xlabel("months")
pl.ylabel("average visitors")
pl.bar(x,y,width=0.3,color='g')
pl.show()
