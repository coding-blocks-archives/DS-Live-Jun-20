#!/usr/bin/env python
# coding: utf-8

# In[12]:


f = open("file1.txt")


# In[13]:


f.closed


# In[14]:


f.tell()


# In[15]:


f.read(4)


# In[16]:


f.tell()


# In[17]:


f.read()


# In[19]:


f.tell()


# In[18]:


f.read()


# In[20]:


# pointer ko particular index 
f.seek(0)


# In[21]:


f.tell()


# In[22]:


my_data = f.read()


# In[23]:


my_data


# In[24]:


f.close()


# In[25]:


f.closed


# ### with open 

# In[38]:


# Context Managers
with open("file1.txt" , 'rt') as fi:
    text = fi.readlines()
    print(text)


# In[28]:


fi.closed


# In[ ]:





# 
