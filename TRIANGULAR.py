
# coding: utf-8

# In[19]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,150)
a=1
b=50
c=95

plt.xlabel('EJE X')
plt.title('FUNCION DEL TRIANGULO')

plt.grid()

def f(x,a,b,c):
    if ((x<a) | (x>=c)):
        ans=0
    if ((a<=x) & (x<b)):
         ans=(x-a)
    if ((b<=x) & (x<=c)):
        ans=c-x
    return ans

fun_vect = np.vectorize(f)
func=fun_vect(x,a,b,c)
plt.plot(x,fun_vect(x,a,b,c))


# In[ ]:



