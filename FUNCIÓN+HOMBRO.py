
# coding: utf-8

# In[5]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt

x=[30,30,70,70,100]
a=20
b=70


plt.xlabel('EJE X')
plt.title('FUNCION HOMBRO')

plt.grid()

def f(x,a,b):

    if (x<a):
        ans=0
    if (x>=a)&(x<b):
         ans=(x-a)/(b-a)
    if (x>=b):
        ans=1
    return ans


fun_vect = np.vectorize(f)
func=fun_vect(x,a,b)
print func
plt.axis([x[0], x[-1], 0, 2])
plt.plot(x,fun_vect(x,a,b))


# In[ ]:



