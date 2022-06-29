#!/usr/bin/env python
# coding: utf-8

# # Visualization with Plotly

# ## Objectives 

# Perform exploratory Data Analysis and feature Engineering using Pandas,Matplotlib and plotly

#  - Exploratory data Analysis

# __colors available for 'color_continuous_scale__ :brbg, bluyl, rdylbu, earth, prgn, speed, sunsetdark, armyrose

# __Basic Colors__ : 'gray', 'blue', 'white', 'lightgreen', 'pink', 'black', 'green', 'red', 'lightgray', 'lightred', 'darkblue', 'darkred', 'purple', 'orange', 'darkpurple', 'lightblue', 'cadetblue', 'beige', 'darkgreen

# ### Import Libraries and Define Auxiliary Functions

# We will import the following libraries the lab 

# In[22]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import plotly.express as px
import plotly.graph_objects as go


# ## Exploratory Data Analysis

# First, let's read the SpaceX dataset into pandas dataframe and print its summary

# In[23]:


df=pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv")
df.head(5)


# First, let's try to see how the FlightNumber (indicating the continuous launch attempts.) and Payload variables would affect the launch outcome.
# 
# We can plot out the FlightNumber vs. PayloadMassand overlay the outcome of the launch. We see that as the flight number increases, the first stage is more likely to land successfully. The payload mass is also important; it seems the more massive the payload, the less likely the first stage will return.
# 
# We see that different launch sites have different success rates. CCAFS LC-40, has a success rate of 60 %, while KSC LC-39A and VAFB SLC 4E has a success rate of 77%.

# In[24]:


fig = px.scatter(df, x="FlightNumber", y="PayloadMass", color="Class", size='PayloadMass', hover_data=['PayloadMass'], color_continuous_scale='rdylgn')
fig.update_layout(title='Flight Number vs. Payload Mass', xaxis_title='Flight Number', yaxis_title='Payload Mass (Kg)')
fig.show()


# Next, let's drill down to each site visualize its detailed launch record

# ## TASK 1: Visualize the relationship between Flight Number and Launch Site

# Use the function catplot to plot FlightNumber vs LaunchSite, set the parameter x parameter to FlightNumber,set the y to Launch Site and set the parameter hue to 'class'

# Now try to explain the patterns you found in the Flight Number vs. Launch Site scatter point plots.

# In[25]:


fig = px.scatter(df, x="FlightNumber", y="LaunchSite", color="Class", hover_data=['PayloadMass'], color_continuous_scale='rdylgn')
fig.update_layout(title='Flight Number vs. Launch Site', xaxis_title='Flight Number', yaxis_title='Launch Site')
fig.show()


# In[26]:


fig = px.scatter(df, x="FlightNumber", y="LaunchSite", color="Class", size='PayloadMass', hover_data=['PayloadMass'], color_continuous_scale='rdylgn', opacity=.6)
fig.update_layout(title='Flight Number vs. Launch Site', xaxis_title='Flight Number', yaxis_title='Launch Site')
fig.show()


# In[27]:


fig = px.scatter(df, x="FlightNumber", y="LaunchSite", color="Class", size='PayloadMass', hover_data=['PayloadMass'], color_continuous_scale='rdylgn', opacity=.6, facet_row="Class",height=400)
fig.update_layout(title='Flight Number vs. Launch Site', xaxis_title='Flight Number', yaxis_title='Launch Site')
fig.show()


# ### Explain the patterns - found in the Flight Number vs. Launch Site

#  - __With more flight numbers (after 40) higher the success rate for the Rocket is increasing__.
#  - *But theres no clear pattern to make a decision if the Flight Number is dependant on Launch Site for a success launch.*
#  
#  ***

# ## TASK 2: Visualize the relationship between Payload and Launch Site

# We also want to observe if there is any relationship between launch sites and their payload mass.

# Now try to explain any patterns you found in the Payload Vs. Launch Site scatter point chart.

# In[33]:


fig = px.scatter(df, x="PayloadMass", y="LaunchSite", color="Class", size='PayloadMass', hover_data=['PayloadMass'],  color_continuous_scale='rdylgn', opacity=.6)
fig.update_layout(title='Payload Vs. Launch Site', xaxis_title='Payload Mass (kg)', yaxis_title='Launch Site')
fig.show()


# In[34]:


fig = px.scatter(df, x="PayloadMass", y="LaunchSite", color="Class", size='PayloadMass', facet_row="Class", hover_data=['PayloadMass'],  color_continuous_scale='rdylgn', opacity=.6, height=400)
fig.update_layout(title='Payload Vs. Launch Site', xaxis_title='Payload Mass (kg)', yaxis_title='Launch Site')
fig.show()


# ### Explain the patterns - found in the Payload Vs. Launch Site

# The **greater the payload mass (greater than 8000) higher the success rate for the Rocket**. But theres no clear pattern to make a decision if the Launch Site is dependant on Pay Load Mass for a success launch.
# 
# ***

# ## TASK 3: Visualize the relationship between success rate of each orbit type

# Next, we want to visually check if there are any relationship between success rate and orbit type.

# Let's create a bar chart for the sucess rate of each orbit

# Analyze the ploted bar chart try to find which orbits have high sucess rate.

# In[35]:


xh =  df.groupby(['Orbit'], as_index=False)['Class'].mean()
xh.sort_values(['Class'], inplace=True)
xh


# In[36]:


fig = px.bar(xh, x='Orbit', y='Class', hover_data=['Orbit', 'Class'], color='Class', height=400, color_continuous_scale='teal')
fig.update_layout(title='Success Rate vs. Orbit Type', xaxis_title='Orbit', yaxis_title='Success Rate' )
fig.show()


# ### Explain the patterns - which orbits have high sucess rate.

# **ES-L1, GEO, HEO, SSO has highest Sucess rates.** SO has poorest.
# 
# ***

# ## TASK 4: Visualize the relationship between FlightNumber and Orbit type

# For each orbit, we want to see if there is any relationship between FlightNumber and Orbit type.

# In[37]:


fig = px.scatter(df, x="Orbit", y="FlightNumber", color="Class", size='PayloadMass', hover_data=['PayloadMass'], height=600, color_continuous_scale='rdylgn', opacity=.6)
fig.update_layout(title='FlightNumber Vs. Orbit type', xaxis_title='Orbit', yaxis_title='Flight Number')
fig.show()


# In[38]:


fig = px.scatter(df, y="Orbit", x="FlightNumber", color="Class", size='PayloadMass', hover_data=['PayloadMass'], height=500, color_continuous_scale='rdylgn', opacity=.6)
fig.update_layout(title='FlightNumber Vs. Orbit Type', yaxis_title='Orbit', xaxis_title='Flight Number')
fig.show()


# You should see that in the LEO orbit the Success appears related to the number of flights; on the other hand, there seems to be no relationship between flight number when in GTO orbit.
# 
# ***

# ## TASK 5: Visualize the relationship between Payload and Orbit type

# Similarly, we can plot the Payload vs. Orbit scatter point charts to reveal the relationship between Payload and Orbit type

# In[39]:


fig = px.scatter(df, x="Orbit", y="PayloadMass", color="Class", size='PayloadMass', hover_data=['PayloadMass'], color_continuous_scale='rdylgn', height=600, opacity=.6)
fig.update_layout(title='Payload Vs. Orbit Type', xaxis_title='Orbit', yaxis_title='Payload Mass')
fig.show()


# In[40]:


fig = px.scatter(df, y="Orbit", x="PayloadMass", color="Class", size='PayloadMass', hover_data=['PayloadMass'], color_continuous_scale='rdylgn', height=450, opacity=.6)
fig.update_layout(title='Payload Vs. Orbit Type', yaxis_title='Orbit', xaxis_title='Payload Mass')
fig.show()


# In[41]:


fig = px.scatter(df, x="Orbit", y="PayloadMass", color="Class", facet_row="Class", size='PayloadMass', hover_data=['PayloadMass'], color_continuous_scale='rdylgn', height=800)
fig.update_layout(title='Payload Vs. Orbit type', xaxis_title='Orbit', yaxis_title='Payload Mass')
fig.show()


# In[42]:


fig = px.scatter(df, x="Orbit", y="PayloadMass", color="Class", facet_col="Class", size='PayloadMass', hover_data=['PayloadMass'], color_continuous_scale='rdylgn', height=500, width=1000)
fig.update_layout(title='Payload Vs. Orbit type', xaxis_title='Orbit', yaxis_title='Payload Mass (Kg)')
fig.show()


# You should observe that Heavy payloads have a negative influence on GTO orbits and positive on GTO and Polar LEO (ISS) orbits.

# ## TASK 6: Visualize the launch success yearly trend

# You can plot a line chart with x axis to be Year and y axis to be average success rate, to get the average launch success trend

# The function will help you get the year from the date:

# In[43]:


# A function to Extract years from the date 
year=[]
def Extract_year(date):
    for i in df["Date"]:
        year.append(i.split("-")[0])
    return year


# In[44]:


# Plot a line chart with x axis to be the extracted year and y axis to be the success rate
df['year']=Extract_year(df["Date"])
df_groupby_year=df.groupby("year",as_index=False)["Class"].mean()


# In[45]:


fig = px.line(df_groupby_year, x="year", y="Class", text="year", height=400)
fig.update_layout(title='Space X Rocket Success Rates', xaxis_title='Year', yaxis_title='Success Rate')
fig.update_traces(textposition="bottom right")
fig.show()


# In[46]:


fig = px.line(df_groupby_year, x="year", y="Class", text="year")
fig.update_layout(title='Space X Rocket Success Rates', xaxis_title='Year', yaxis_title='Success Rate', hovermode='x unified')
fig.update_traces(textposition="bottom right")
fig.show()


# you can observe that the sucess rate since 2013 kept increasing till 2020

# ## Authors

# [Swati Narang](https://www.linkedin.com/in/swatinarang12/)

# [Github Files](https://github.com/swatinarang1225/IBM-Data-science-Professional-Certificate/tree/master/10.%20Applied%20Data%20Science%20Capstone)
# 
