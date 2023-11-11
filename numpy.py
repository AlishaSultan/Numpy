#!/usr/bin/env python
# coding: utf-8

# In[1]:


###########Numpy is a python library which is used for scientific computation.Numpy ka datatype numpy arrays hai means nd arrays multidimensional arrays object.data type of all items are same.


# In[2]:


#why we use numpy instead of python list>>>????
#In numpy , the array size is fixed at the time of creation but list not....when we change nd array it deletes the original and makes the new array


# In[3]:


# required same data type and same size in memory


# In[4]:


# numpy arrays facilitates to solve mathematical operations instantly as compared to list


# In[5]:


# pandas , matplotlib , scikit learn derived from the numpy


# In[6]:


#python ke data types slow thy but easy to use tha tu C mei completely ak data type bannaya numpy array aur python ky andat integrate kr diya tu speed enhance hoo gai... numpy is powerful datatype in python 


# In[7]:


import numpy as np
array = np.array([2 , 4 , 5 ,6 ,7 ,8 ])     #_______________np.array() is a function
print(array)             # also called vector


# In[8]:


# 2d array
import numpy as np
array = np.array([[2 , 4 , 5 ,6 ,7 ,8 ] , [4 , 6, 7,3 , 6 ,9]])     #_______________np.array() is a function
print(array)             # also called matrix


# In[11]:


#3d array
import numpy as np
array = np.array([[[3 , 4] , [8 , 9]] , [[4 , 6] , [5 , 9]]])     #_______________np.array() is a function
print(array)             # also called tensor


# In[12]:


# data type change krne hai tu????
array = np.array([1 , 2 , 5, 7, 8] , dtype = float)
print(array)


# In[13]:


array = np.array([1 , 2 , 5, 7, 8] , dtype = int)
print(array)


# In[14]:


array = np.array([1 , 2 , 5, 7, 8] , dtype = str)
print(array)


# In[15]:


array = np.array([1 , 2 , 5, 7, 8] , dtype = bool)
print(array)


# In[17]:


array = np.array([1 , 2 , 5, 7, 8] , dtype = complex)
print(array)


# In[20]:


array = np.arange(1 , 10 )
print(array)


# In[21]:


array = np.arange(1 , 10 , 2 )
print(array)


# In[24]:


array = np.arange(1 , 10).reshape(3 , 3)


# In[25]:


print(array)


# In[26]:


#np.ones() used for intialization ......

array = np.ones((3 , 4))
print(array)


# In[28]:


array = np.zeros((3 , 4))
print(array)


# In[36]:


array = np.random.random((3 , 4))             #random ak class hai us ky andar method hai random
print(array)


# In[39]:


array = np.linspace(-10 , 10 , 10)     #first -10 is lower range ,,,,,10 is upper range ,,,,,10 is number of elements     2 points ky beech ka difference same hoo ga 
print(array)
#called linearlyspace   linearly seperably points generate krta hai


# In[40]:


array = np.identity(3)
print(array)

(3)     3 ones in diagonal
# In[41]:


array = np.identity(4)
print(array)


# In[45]:


a1 = np.arange(10)
print(a1)


a2 = np.arange(16).reshape(2 , 8)
print(a2)


a3 = np.arange(20).reshape(2 , 5 , 2)            #first 2 batata hai kitne 2d arrays hai nect 5 , 2 is number of rows and columns
print(a3)


# In[46]:


##################################################numpy attributes##############################################


# In[47]:


print(a1.ndim)


# In[48]:


print(a2.ndim)


# In[49]:


print(a3.ndim)


# In[50]:


array = np.array([[[3 , 4 ,5 , 6] , [6 , 7 , 8, 4] , [3 , 6 , 8 , 4]]])
print(array.ndim)


# In[54]:


array = np.array([[[4 , 5 , 6] , [5 , 6 , 8]] , [[4 , 6 , 7] , [6 , 8 , 4]]])
print(array.ndim)


# In[55]:


print(a1.shape)


# In[56]:


print(a2.shape)


# In[57]:


print(a3.shape)


# In[58]:


print(a1.size)                     ####tell number of items


# In[59]:


print(a2.size)


# In[60]:


print(a3.size)


# In[61]:


print(a1.itemsize)                  #### har item memory mei kitna size occupy kr rahein hai


# In[62]:


print(a2.itemsize)


# In[63]:


print(a3.itemsize)


# In[71]:


a1 = np.arange(10,dtype = np.float64)       #####for increasing or decreasing the size
print(a1)


# In[66]:


print(a1.itemsize)


# In[67]:


#########################int32  = 4bytes  ,,,,,,,,,, int64 = 8bytes


# In[72]:


print(a1.dtype)


# In[69]:


print(a2.dtype)


# In[70]:


print(a3.dtype)


# In[73]:


########################### changing datatype  #######################################


# In[99]:


array=a3.astype(np.float32)                  ####astype changing the datatype when they occupy more space


# In[100]:


print(array.dtype)


# In[105]:


########################################Array operations##########################################

#two types of opeartions:
    #one is scalar                        scalar or numpy arrays opeartions
    #other is vector                      numpy array or another numpy operation 


# In[106]:


array1 = np.arange(12).reshape(3 , 4)
print(array1)

array2 = np.arange(12 , 24).reshape(3 ,4)
print(array2)


# In[107]:


print(array1 * 2 )              # 2 is a scalar


# In[108]:


print(array1 ** 2 )   
print(array1 + 2 )
print(array1 - 2 )
print(array1 / 2 )   


# In[109]:


###################################also use relational operator###########################################


# In[110]:


print(array1 > 5)


# In[111]:


print(array1 < 5)


# In[112]:


print(array1 == 5)


# In[113]:


print(array1 != 5)


# In[114]:


#######################################vector operation#############################################
# 2 arrays py operation perform kr sakhty hai 


# In[115]:


print(array1 + array2)


# In[117]:


print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(array1 ** array2)


# In[119]:


a3 = np.arange(20).reshape(2 , 5 , 2)            #first 2 batata hai kitne 2d arrays hai nect 5 , 2 is number of rows and columns
print(a3.ndim)


# In[122]:


a3 = np.arange(40).reshape(2 , 5 , 2 ,2 )            #first 2 batata hai kitne 2d arrays hai nect 5 , 2 is number of rows and columns
print(a3.ndim)


# In[123]:


######################################################Array functions#################################################


# In[138]:


a1 = np.random.random((3 , 3))
a1 = np.round(a1 * 100)
print(a1)


# In[139]:


np.max(a1)


# In[140]:


np.min(a1)


# In[141]:


np.sum(a1)


# In[142]:


np.product(a1)        #also use prod


# In[143]:


np.max(a1 , axis = 0)                     # axis = 0 column show          har column mei max bta do


# In[144]:


np.max(a1 , axis = 1)                    #axis = 1 row show                har row mei max bta do


# In[145]:


np.mean(a1)


# In[146]:


np.median(a1)


# In[147]:


np.std(a1)


# In[150]:


np.var(a1)


# In[151]:


np.sin(a1)


# In[152]:


np.cos(a1)


# In[153]:


np.tan(a1)


# In[154]:


jello = np.arange(12).reshape(3 , 4)
jello_1 = np.arange(12 , 24).reshape(4 , 3)
print(jello)
print(jello_1)


# In[155]:


np.dot(jello , jello_1)                             ####  (3 , 4)   and   (4 , 3)    2nd 4 and 4 is same and resultant is equal to 3 and 3


# In[157]:


np.log(jello_1)


# In[158]:


np.exp(jello_1)


# In[161]:


b2=np.random.random((3 , 4))


# In[162]:


np.round(b2 , 2)


# In[163]:


np.floor(b2)


# In[164]:


np.ceil(b2)


# In[165]:


##########################################indexing##############################################


# In[195]:


a1 = np.arange(12)
a2 = np.arange(12).reshape(3 , 4)
a3 = np.arange(27).reshape(3 , 3 , 3)
print(a1)
print(a2)
print(a3)


# In[168]:


a1[-1]


# In[169]:


a2[2 , 2]


# In[173]:


a3[1 , 2 , 0]                    # 1 is which 2d array 1 or 2??? 2 is row and 0 is column


# In[174]:


##############################################slicing##########################################################


# In[175]:


a1


# In[177]:


a1[2:7:2]


# In[178]:


a2


# In[179]:


a2[1 , :]


# In[180]:


a2[: , 2]


# In[181]:


a2[1: , 2:]


# In[183]:


a2[::2 , ::3]


# In[186]:


a2[1: , 1:3]


# In[187]:


a2[::2 , 1 : 3]


# In[190]:


a2[1 : 3 , ::2]


# In[191]:


a2[0:2 ,::2 ]


# In[192]:


a2[1:2 , ::3 ]


# In[193]:


a2[0:2 , 1: ]


# In[196]:


a3


# In[197]:


a3[1 , 0: , 0:]


# In[198]:


a3[::2]


# In[200]:


a3[0 , 1 , 0:]


# In[206]:


a3[1 , : , 1:2]


# In[202]:


a3[2 , 1: , 1: ]


# In[208]:


a3[::2 , 0:1 ,::2 ]


# In[209]:


#########################################################Iterating#######################################################


# In[210]:


a1


# In[211]:


for i in a1:
    print(i)


# In[212]:


a2


# In[213]:


for i in a2:
    print(i)


# In[214]:


for i in a3:
    print(i)


# In[216]:


for i in np.nditer(a1):                     ###############Print number of items#####################
    print(i)


# In[217]:


for i in np.nditer(a2):
    print(i)


# In[218]:


for i in np.nditer(a3):
    print(i)


# In[219]:


################################################# reshaping 3 functions:  transpose . reshape , ravel

np.transpose(a1)


# In[220]:


np.transpose(a2)


# In[221]:


np.transpose(a3)


# In[222]:


##############################also use########################################


# In[223]:


a1.T


# In[224]:


a2.T


# In[225]:


a3.T


# In[226]:


##########################################  ravel (n-dimension ko 1 dimension mei convert kr daita hai)


# In[227]:


a3.ravel()


# In[228]:


a2.ravel()


# In[229]:


#################################################Stacking####################################################

############mutliple data ko jorny ky liya use hota hai


# In[230]:


#horizontal stacking


# In[231]:


a4 = np.arange(12).reshape(3 , 4)
print(a4)


# In[233]:


a5 = np.arange(12 , 24).reshape(3 , 4)
print(a5)


# In[234]:


np.hstack((a4 , a5))                # rows same hote hai column add hotay hai


# In[235]:


np.vstack((a4 , a5))               # rows add hote hai column same hotay hai


# In[238]:


np.hsplit(a4 , 2)


# In[241]:


np.vsplit(a4 , 3)


# In[ ]:




