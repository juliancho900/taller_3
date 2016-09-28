
# coding: utf-8

# In[4]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt

x=[0,15,15,50,150,180,180,200]
a=10
b=50
c=150
d=180

plt.xlabel('EJE X')
plt.title('FUNCION PI O TRAPECIO')

plt.grid()

def f(x,a,b,c,d):
    if ((x<a) | (x>=c)):
        ans=0
    if (x>=a)&(x<b):
         ans=(x-a)/(b-a)
    if (x>=b)&(x<d):
        ans=1
    if (x>=d)&(x<c):
        ans=1-(x-d)/(c-d)
    return ans


fun_vect = np.vectorize(f)
func=fun_vect(x,a,b,c,d)
print func
plt.axis([x[0], x[-1], 0, 2])
plt.plot(x,fun_vect(x,a,b,c,d))


# In[ ]:



