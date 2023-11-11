#!/usr/bin/env python
# coding: utf-8

# In[1]:


############################################## numpy tricks #############################################################


# In[2]:


import numpy as np

a = np.random.randint(1 , 100 , 15)
b = np.random.randint(1 , 100 , 24).reshape(6 , 4)

a
b


# In[12]:


np.sort(a)


# In[13]:


np.sort(b)


# In[14]:


np.sort(b , axis = 0)     #0 column wise sorting


# In[15]:


np.sort(a)[::-1]


# In[11]:


np.sort(b , axis = 0)[::-1]


# In[16]:


np.sort(b , axis = 1)[::-1]


# In[17]:


np.sort(b , axis = 1)


# In[22]:


np.append(b , np.ones((b.shape[0] , 1)),axis = 1)      #(b.shape[0] , 1)   rows hai wo b ky equal hoo jai or column new 1 add hoo jai


# In[25]:


a = np.arange(12).reshape(6 , 2)
b = np.arange(12 , 24).reshape(6 , 2)


# In[26]:


np.concatenate((a , b) , axis = 0)


# In[27]:


np.concatenate((a , b) , axis = 1)

           - - - - - - - - column     ---------> axis = 1
      -
      -
row   -    axis = 0
      -
      -
      -
      -

# In[28]:


e = np.array([1 , 2 , 2 , 3 , 3 , 3 , 4 , 6 , 7 , 8])
np.unique(e)


# In[29]:


e = np.array([[1 , 2 , 2 , 3 , 3 , 3 , 4 , 6 , 7 , 8] , [1 , 2 , 2 , 3 , 3 , 3 , 4 , 6 , 7 , 8]])
np.unique(e)


# In[37]:


e = np.array([1 , 2, 3, 4 , 5 , 6 , 7 , 8 ,9 , 3 , 4 , 5])
f = np.expand_dims(e , axis = 0)


# In[38]:


e.shape


# In[39]:


f.shape


# In[40]:


f


# In[43]:


e = np.array([1 , 2, 3, 4 , 5 , 6 , 7 , 8 ,9 , 3 , 4 , 5])
f = np.expand_dims(e , axis = 1)


# In[44]:


f


# In[45]:


f.shape

where return the indexes
# In[47]:


y = np.array([3 , 4 ,78 , 23 , 45 , 67 , 89 , 23 , 45 , 67 , 45 , 89 ])


# In[48]:


np.where(y > 4)       


# In[51]:


#np.where(condition , true , false)

np.where(y < 4 , 0 , y)                  #condtion true then replace otherwise array again displays


# In[52]:


np.where(y%2 == 0 , 0 , y)    

argmax()-----------give the maximum index (maximum element)  of array in particular axis
# In[3]:


import numpy as np

y = np.array([3 , 4 ,78 , 23 , 45 , 67 , 89 , 23 , 45 , 67 , 45 , 89 ])
np.argmax(y)


# In[9]:


b = np.arange(0 , 24).reshape(4 , 6)
b


# In[10]:


np.argmax(b , axis = 0)


# In[11]:


np.argmax(b , axis = 1)


# In[12]:


np.argmin(b , axis = 0)


# In[13]:


np.argmin(b , axis = 1)

cumsum() ---------------------------> cummulative sum
# In[14]:


y


# In[15]:


np.cumsum(y)


# In[18]:


b


# In[21]:


np.cumsum(b)


# In[22]:


np.cumsum(b , axis = 0)


# In[23]:


np.cumsum(b , axis = 1)


# In[24]:


np.cumprod(b , axis = 0)


# In[25]:


np.cumprod(b , axis = 1)


# In[3]:


import numpy as np

y = np.array([3 , 4 ,78 , 23 , 45 , 67 , 89 , 23 , 45 , 67 , 45 , 89 ])

np.percentile(y , 100)


# In[4]:


np.percentile(y , 50)


# In[5]:


np.percentile(y , 0)

we write 75 it means that 75 ky neachy kitny log hai (n) / (N) -----Total people  * 100
percentile = n/N * 100

1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9

we select 5:

5/9 * 100 = 56---------56 numbers aisay hai joo 5 sy chotay hai  that is perecentile

then we select 50%

50/100 * (n+1)  = 3.3 tu 3.3(index) ----------> then we calculate average:  4 + 5 /2 = 7------(given data hai us mei 50% of data 7 sy km hai

Qunatile:

-q0-------------------q1-----------------q2---------------------q3-----------------------------------------
                25% of percentile    50% of percentile          75% of percentile
 
 first quantile is 25% of percentile vice a versaHistogram:

How do you define a histogram?

A histogram is a display of statistical information that uses rectangles to show the frequency of data items in successive numerical intervals of equal size

we define the number of bins  like 10 , 20 tu 10 or 20 ky beech mei kn kn se values aa rahe hai






# In[8]:


y


# In[7]:



np.histogram(y , bins = [0 , 10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90])


# In[12]:


import matplotlib.pyplot as plt

plt.hist(y)
plt.show()

np.corrcoef       #correlation means ak ky barny sy dosaray py kitna effect aa raha hai

Co-relation ---- (-1 to 1)

x                      y

x --------- 0   ------- y     -----------------------------> no co-relation

x --------- 1   --------y      -----------------------------. positive co-relation   x ky increase honay sy y be increase hoo raha hai....

x --------- -1   --------y      -----------------------------. negaive co-relation   x ky increase honay sy y be decrease hoo raha hai....






# In[13]:


salary = np.array([40000 , 50000 , 60000 , 23777 , 489766, 9376464])
experience = np.array([1 , 3 , 4 , 8 , 6 , 5])

np.corrcoef(salary , experience)

             salary          experience

salary        1.               0.114...

experience    0.114--             1.--np.isin() -------------searching the multiple values in array ky array mei calue present hai yeh ni hai
# In[14]:


y


# In[21]:


items = [78 , 89 , 3 , 4 , 23 , 67]

np.isin(y , items)


# In[22]:


items = [78 , 89 , 3 , 4 , 23 , 67]

y[np.isin(y , items)]

flip:
# In[23]:


y


# In[24]:


np.flip(y)


# In[26]:


z = np.arange(0 , 24).reshape(4 , 6)
z


# In[27]:


np.flip(z , axis = 0)


# In[28]:


np.flip(z , axis = 1)


# In[29]:


np.flip(z)

np.put()------------->changes data in an array--------------> permanent changes
# In[30]:


y


# In[31]:


np.put(y , [0 , 1] , [113 , 129])


# In[32]:


y

agr np.(something) karein tu print hoo jai temporary changes hoo ge wo agr nah hoo tu permanentdelete:
# In[33]:


y


# In[34]:


np.delete(y , 0)


# In[35]:


np.delete(y , [3 , 6 , 8])          #multiple deletion

Set functions:

np.union1d
np.intersect1d
np.setdiff1d
np.setxor1d
np.in1d


# In[36]:


a = np.array([4 , 5, 6 , 2 ,3 , 7, 9, 3])
b = np.array([5 , 6 , 2 , 3 , 8 ,9 , 3 , 4])

np.union1d(a , b)


# In[38]:


a = np.array([4 , 5, 6 , 2 ,3 , 7, 9, 3])
b = np.array([5 , 6 , 2 , 3 , 8 ,9 , 3 , 4])

np.intersect1d(a , b)


# In[39]:


np.setdiff1d(a , b)


# In[40]:


np.setxor1d(a , b)                        #common ko hata dein ga different rakh dy ga


# In[42]:


np.in1d(a , 3)


# In[43]:


a[np.in1d(a , 3)]

Clip : us range mei values given kr daita hai
# In[45]:


d = np.arange(0 , 30).reshape(5 , 6)
d


# In[49]:


np.clip(d , a_min = 11 , a_max = 14)            a_min-----> 0 to 11 ,  a_max -------->14 sy onward agy


# In[ ]:




