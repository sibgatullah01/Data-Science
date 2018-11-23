
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sp
import pandas.plotting


# In[9]:


from IPython import display
from ipywidgets import interact, widget
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


Five_years_data=pd.read_csv('F:\Data science\\00Data\\gapminder-FiveYearData.csv')


# In[6]:


Five_years_data.head()


# In[99]:


def year(year):
    data=Five_years_data[Five_years_data.year==year]
    edgecolor=data.continent.map({'Asia':'darkblue','Europe':'gold',
                                         'Africa':'red','Americas':'Coral', 
                                         'Oceania':'palegreen',})
    size=data['pop']
    plt.scatter(data.gdpPercap,data.lifeExp, s=size*5e-6, linewidth=1, c='grey', edgecolor=edgecolor)
    
    plt.xlabel('gdp Per Capita')
    plt.ylabel('life expectancy')
    plt.axis([-10000,50000,10,90])
    plt.show
year(2007)


# In[100]:


interact(year, year=range(1952,2008,5))


# In[101]:


def gdp(country):
    data=Five_years_data[Five_years_data.country==country]
    
    plt.plot(data.year,data.gdpPercap, '^m',linewidth=1,)
    plt.plot(data.year,data.gdpPercap, 'b',linewidth=1,)
    plt.xlabel('year')
    plt.ylabel('gdp per capita')

    plt.show

    


# In[102]:


interact(gdp,country=Five_years_data['country'].unique())


# In[59]:


k=Five_years_data[Five_years_data.gdpPercap==Five_years_data.gdpPercap.max()]


# In[60]:


k


# In[66]:


k.loc[:,['country', 'gdpPercap']]


# In[86]:


k['gdpPercap']/365

