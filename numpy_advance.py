#!/usr/bin/env python
# coding: utf-8

# In[1]:


############################################ advanced numpy #############################################################


# In[2]:


############### Numpy array vs python list


# In[6]:


#speed
#memory
#convenience

a = [i for i in range(10000000)]                       # dynamic and referencial array
b = [i for i in range(10000000 , 20000000)]

c = []

import time

start = time.time()
for i in range(len(a)):
    c.append(a[i] + b[i])
    
print(time.time() - start)
    


# In[9]:


import numpy as np               #numpy C ka syntax use krta hai jo static hai size fixed hai

a = np.arange(10000000)
b = np.arange(10000000 , 20000000)

import time

start = time.time()            # current time

c = a + b

print(time.time() - start)


# In[10]:



a = [i for i in range(10000000)] 

import sys

sys.getsizeof(a)


# In[11]:


a = np.arange(10000000)

import sys

sys.getsizeof(a)


# In[12]:


###########################################################Fancy indexing ##################################################
#########################################################Boolean indexing ##################################################


a = np.arange(12).reshape(4 , 3)
print(a)


# In[13]:


a[::2 , :]


# In[14]:


###########but we get 1 , 3 , 4 row cannot get then we using fancy indexing:

a[[0 , 2 , 3]]


# In[15]:


############################this is possible by using fancy indexing#########################################


# In[16]:


a = np.arange(24).reshape(6 ,4)
print(a)


# In[17]:


a[[0 , 2 , 4 , 5]]


# In[18]:


a[: , [1 , 2  , 3]]


# In[24]:


#########################Boolean indexing:  When we seperate even odd numbers , numbers greater or less then we use boolean indexing

1d and temporary result daite hai original array mei change ni hota


# In[26]:


b = np.random.randint(1 , 100 , 24).reshape(6 , 4)               #########2 integers ky darmayan random numbers
print(b)


# In[27]:


b > 8            #(called boolean array)


# In[28]:


################################soo , we use boolean masking    given condition ke base py filtration krty hai


# In[29]:


b[b > 8]                  # only True gets the value


# In[30]:


b[b%2 == 0]                #will return even numbers


# In[36]:


(b > 8) & (b%2 == 0)


# In[37]:


b[(b > 8) & (b%2 == 0)]                          ( & ---> bitwise operator     and---> logical operator )


# In[39]:


b[b%7 != 0]


# In[43]:


b[~(b%7 == 0)]    #also use


# In[1]:


###############################################Broadcasting##########################################################


# In[2]:


#Broadcasting describes how numpy treat arrays with different shapes during arithemtic operations
#chotay walay array ko broadcast krty hoo baray walay ky sath so that they have compatible shape


# In[3]:


########################## Broadcasting rules ######################################


# In[4]:


#Make the two arrays have the same number of dimension
#How???
#(1 , 3)      (2)  having different dimension
#add 1 with smaller dimension in head
#(1 , 3)       (1 , 2)



#then next rule is :
    
    #if ( 4 , 3)    (1 , 3)    then make the sizes same
    #then stretch 1 upto the size of row which is  4 and column size is same
    
    #so , 
    
    #(4 , 3)       ( 4 , 3)
    
    
#agr 1 ni hoo ga no broadcasting is performed


# In[6]:


import numpy as np
a = np.arange(12).reshape(4 , 3)
b = np.arange(3).reshape(3)
print(a)
print(b)


# In[7]:


a + b


# In[9]:


a = np.arange(12).reshape(3 , 4)
b = np.arange(3).reshape(3)
a + b                            #not possible because size is different


# In[12]:


a = np.arange(3).reshape(3 , 1)
b = np.arange(3).reshape(1 , 3)
a + b                            #not possible because size is different


#how's it possible because 3 , 1 and 1 , 3 dimension is same but sizes are different now we will same this. jaha jaha one hoo ga us ko stretch karein gy kaha tk dosare ke row tk then dosaray ke column tk


# In[14]:


a = np.arange(3).reshape(3 , 1) 
b = np.arange(4).reshape(1 , 4)
a + b  


#3 , 1  ------- 1 , 4

#3 , [1]----stretch by seeing the next array of column    --------------3 , 4

#1 , 4------stretch by seeing the previous array of row   --------------3 , 4


# In[19]:


a = np.array([1])
b = np.arange(4).reshape(2 , 2)
a + b  


# In[20]:


a = np.arange(12).reshape(3 , 4) 
b = np.arange(12).reshape(4 , 3)
a + b  


# In[21]:


a = np.arange(16).reshape(4 , 4) 
b = np.arange(4).reshape(2 , 2)
a + b  


# In[22]:


#####################it is used in vectorization ######################################


# In[23]:


############################ working with mathematical formula######################################################


# In[24]:


a = np.arange(10)
print(a)


# In[25]:


np.sum(a)


# In[26]:


######Sigmoid:


# In[30]:


def sigmoid(array):
    
    return 1 / (1 + np.exp(-(array)))

array = np.arange(100)
sigmoid(array)


# In[31]:


###### loss function is like a torch kya karein gy error km hoo ga   called mean square error

#iq    marks             prediction

#45     50   ------------ 60      (error)
#78      60---------------50       (error)


# In[34]:


actual_data = np.random.randint( 1, 50 , 25)
predicted_data = np.random.randint( 1, 50 , 25)

mean_square_error = np.mean((actual_data - predicted_data) ** 2)
print(mean_square_error)


# In[35]:


######### binary cross entropy


# In[36]:


#########################################Working with missing values#############################################


# In[37]:


#jab data ata hai tu bht sara missing hota hai missing values hote hai


# In[40]:


a = np.array([1 , 2 , 3 , 4 , np.nan , 5 , np.nan])         #np.nan generates missing values    nan and non not same nan means missing values 
a


# In[41]:


np.isnan(a)


# In[42]:


a[np.isnan(a)]


# In[43]:


a[~(np.isnan(a))]


# In[44]:


import matplotlib.pyplot as plt
x = np.linspace(-10 , 10 , 100)       #used when we make equidistance points
y = x

plt.plot(x , y)


# In[45]:


import matplotlib.pyplot as plt
x = np.linspace(-10 , 10 , 100)       #used when we make equidistance points
y = x**2                               # parabola

plt.plot(x , y)


# In[47]:


import matplotlib.pyplot as plt
x = np.linspace(-10 , 10 , 100)       #used when we make equidistance points
y = np.sin(x)                              

plt.plot(x , y)


# In[48]:


import matplotlib.pyplot as plt
x = np.linspace(-10 , 10 , 100)       #used when we make equidistance points
y = x*np.log(x)                            

plt.plot(x , y)


# In[49]:


import matplotlib.pyplot as plt
x = np.linspace(-10 , 10 , 100)  
y = 1 / (1 + np.exp(-(x)))

plt.plot(x , y)


# In[ ]:




