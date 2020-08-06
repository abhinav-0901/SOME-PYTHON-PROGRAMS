#!/usr/bin/env python
# coding: utf-8

# In[2]:


#line class
import math


# In[4]:


class Line():
    def __init__(self,coor1,coor2):
        self.coor1=coor1
        self.coor2=coor2
    
    def distance(self):
        x1,y1=self.coor1
        x2,y2=self.coor2
        return ((x2-x1)**2+(y2-y1)**2)**0.5

    def slope(self):
        
        x1,y1=self.coor1
        x2,y2=self.coor2
        return (y2-y1)/(x2-x1)
        
        


# In[5]:


l=Line((1,2),(2,3))


# In[6]:


l.distance()


# In[7]:


l.slope()


# In[ ]:




