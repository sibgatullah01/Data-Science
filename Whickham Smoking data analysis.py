
# coding: utf-8

# # Whickham analysis
# The table records the data of women whether they smoke or not. The survey was done in Whickham, England in 1973 and survey was followed after 20 to record if the women was still alive.

# In[5]:


import math
import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt
import pandas.plotting


# In[4]:


from IPython import display
from ipywidgets import interact, widget
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


smoking=pd.read_csv('F:\Data science\\00Data\\whickham.csv')


# In[15]:


smoking.head()


# In[14]:


smoking.columns


# In[17]:


smoking.outcome.value_counts(
)


# In[157]:


smoker=smoking.smoker.value_counts()


# In[27]:


outcome_group=smoking.groupby(['smoker']).outcome.value_counts(normalize=True)


# In[148]:


outcome_group.unstack()


# In[33]:


##the analysis above shows that in outcome more smokers are alive than that non-smokers and more non-smokers are dead compared to its counter part.This is because age factor is not considered here. We use stratification for this.


# In[132]:


smoking['agegroup']=pd.cut(smoking['age'],[15,25,35,45,55,65,75,85],labels=['15-25','25-35','35-45','45-55','55-65','65-75','75-85'])


# In[133]:


smoking.head()


# In[144]:


bysmoker=smoking.groupby(['agegroup','smoker']).outcome.value_counts(normalize=True)


# In[145]:


bysmoker


# In[146]:


bysmoker.unstack().drop('Dead', axis=1)


# In[ ]:


## after taking age variable in account and dropping 'dead' from data we can see that the proportion of non-smoker to smoker alive has increased. This is an example of simpson's paradox where one trand appears or disappears when two variables are pu together.


# In[164]:


outcome_group.unstack().plot(kind='bar')


# In[151]:


bysmoker.unstack().plot(kind='bar')
###we can see why the proportion of live and dead of smoker to non-smoker were different. Because age was not considered and as seen in the plot


# In[195]:


bysmoker2=bysmoker.unstack().drop('Dead',axis=1) ## unstacking the outcome into alive and then dropping the column dead


# In[196]:


bysmoker3=bysmoker2.unstack()       ##unsatcking again to get separate columns for smoker=yes and smoker=no
bysmoker3.columns=['No', 'Yes']
bysmoker3.columns.name='Smoker'


# In[197]:


bysmoker3


# In[198]:


bysmoker3.plot(kind='bar')


# Here is the final analysis. As we can see that in young age, smokers and non-smokers have similar proportions but as age increases non-smoker have a little edge over smokers. So don't smoke.
