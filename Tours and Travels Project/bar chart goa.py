#goa
import numpy as np
import matplotlib.pyplot as pl
x=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
y=[12,30,14,4,5,5,6,7,18,16,25,13]
pl.xlabel("months")
pl.ylabel("average visitors")
pl.bar(x,y,width=0.3,color='g')
pl.show()
