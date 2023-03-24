#ooty
import numpy as np
import matplotlib.pyplot as pl
x=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
y=[12,13,14,24,25,25,11,12,18,17,15,12]
pl.xlabel("months")
pl.ylabel("average visitors")
pl.bar(x,y,width=0.3,color='b')
pl.show()
