import numpy as np
import matplotlib.pyplot as plt
greyhound=500
lbd=500
grey_height=28+4*np.random.randn(greyhound)
lbd_height=24+4*np.random.randn(lbd)
plt.hist([grey_height,lbd_height],stacked='True',color=['r','b'])
plt.show()
