#wayanad
import numpy as np
import matplotlib.pyplot as pl
x=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
y=[12,13,12,24,17,10,6,7,18,26,25,13]
pl.xlabel("months")
pl.ylabel("average visitors")
pl.bar(x,y,width=0.3,color='y')
pl.show()
