# -*- coding: utf-8 -*-
"""

Created on Nov 01 13:52:52 2017

@author: ed12k3b

Programming for Geographical Information Analysts: Core Skills
Module taught for MA Social Research Methods (Interdisciplinary)
Module taught by Dr. Andy Evans, University of Leeds.

This file contains the code for the model to run.

To setup:
1. Ensure the 'agentframework_drunks.py' file is open in the same Spyder instance
2. Ensure the 'town.plan.txt' file is location in the same folder as the current file and the 'agentframework_drunks.py' file.

The model will run once, finishing when all drunk agents have reached their respective homes.
Two figures are created; 
1. An image of all agents in their homes after the mdodel has finshed running,
2. An image of the density map created using the data from the model run's output.

Please note: the second figure is not always created due to a NULL BYTE issue, this does not always occur but if it does, please rerun.
             A solution has not been found by the code author.

"""

# Import modules required for model creation

import matplotlib
import matplotlib.pyplot
import agentframework_drunks
import csv


# List creation

environment = []
agents = []
stepped_environment= []


# Defining model parameters such as number of agents: 

num_of_agents = 25


# Defining the ABM's window size, and variable axes

fig = matplotlib.pyplot.figure(figsize=(7,7))
ax = fig.add_axes([0,0,1,1])
#ax.set_autoscale_on(False)


# Reading in environment data

f=open ("town.plan.txt")
reader=csv. reader (f, quoting = csv.QUOTE_NONNUMERIC)


# Reading environment file csv into tows

for row in reader:
    rowlist = []
    for item in row:
        rowlist.append(item)
    environment.append(rowlist)
    

# Creating code for the density map output that adds up steps on each coordinate. It uses a 300x300px size, just like the environment used here


for i in range(300):
    rowlist = []
    for j in range(300):
        rowlist.append(0)
    stepped_environment.append(rowlist)
    

# Read into environment data to locate the pub, which is assigned a value of 1

for y, row in enumerate(environment):
    for x, value in enumerate (row):
        if value==1:
            xstartpoint=x
            ystartpoint=y
            

# Assign each agent a house number based on their creation number * 10. Also, append each drunk to the starting position of the pub's coordinates in the environment

for j in range(num_of_agents):
    housenum = (j+1)*10
    agents.append(agentframework_drunks.Agent(environment, agents, housenum, xstartpoint, ystartpoint))
    

# For agents that aren't home, continue moving and store 1 into the stepped_environment file

for i in range (num_of_agents):
    while agents[i].arrived_home==False:
        agents[i].nav()
        stepped_environment[agents[i]._y][agents[i]._x]+=1
        # For agents that made it home, set their arrival status to True to stop the code from rerunning those agents, and tell them to drunkely announce their arrival
        if agents[i].environment[agents[i]._y][agents[i]._x]==agents[i].housenum: # If the agent's location is the same as their house number
            agents[i].arrived_home=True
            print ("What a journey!! WHERE'S MY BED!")
                     

# Create a graph to demonstrate the agents that arrived at their house (all of them by this point due to above code)
	
fig.canvas.set_window_title('Figure of Drunk Agents at their Homes')
matplotlib.pyplot.xlim=len(environment)
matplotlib.pyplot.ylim=len(environment)
matplotlib.pyplot.imshow(environment)
for i in range (num_of_agents):
        matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)
matplotlib.pyplot.show()


# Write the stored values from the stepped_environment list to be able to create a density map

f2= open ('stepped_enviroment_output.csv', 'w', newline= '')
writer = csv.writer (f2, delimiter = ',')
for row in stepped_environment:
    writer.writerow(row)
f2.close


"""

 The following code produces a second figure; the density map of where drunks stepped during the model run

"""

# List creation

stepped_environment_output = []


# Reading in the stepped_environment_output file

f=open ("stepped_enviroment_output.csv")
reader=csv. reader (f, quoting = csv.QUOTE_NONNUMERIC)


# Convering CSV into rows

for row in reader:
    rowlist = []
    for item in row:
        rowlist.append(item)
    stepped_environment_output.append(rowlist)


# Creating the size of the figure

fig = matplotlib.pyplot.figure(figsize=(7,7))
ax = fig.add_axes([0,0,1,1])


# Creating the density map showing the density of where agents stepped when returning home

fig.canvas.set_window_title('Figure of Density Map')
matplotlib.pyplot.xlim=len(environment)
matplotlib.pyplot.ylim=len(environment)
matplotlib.pyplot.imshow(stepped_environment_output)
matplotlib.pyplot.show()