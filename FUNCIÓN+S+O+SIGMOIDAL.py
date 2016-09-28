
# coding: utf-8

# In[3]:

get_ipython().magic(u'matplotlib inline')
import math
import numpy as np
import matplotlib.pyplot as plt


plt.xlabel('EJE X')
plt.title('FUNCION SIGMOIDAL')

plt.grid()

def sigmoid(x):
    a = []
    for item in x:
        a.append(1/(1+math.exp(-item)))
    return a

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-15., 15,0.5)
sig = sigmoid(x)
plt.plot(x,sig)


# In[ ]:



