# -*- coding: utf-8 -*-
"""

Created on Nov 01 13:44:33 2017

@author: ed12k3b

Programming for Geographical Information Analysts: Core Skills
Module taught for MA Social Research Methods (Interdisciplinary)
Module taught by Dr. Andy Evans, University of Leeds.

This file contains the parameters for the Agent class.

To setup:
1. Ensure the 'planning_for_drunks_model.py' file is open in the same Spyder instance
2. Ensure the 'town.plan.txt' file is location in the same folder as the current file and the 'planning_for_drunks_model.py' file.


"""

# Import modules

import random


# Creationg of agents with the followng characteristics: 

class Agent ():
    
    def __init__(self, environment, agents, housenum, xstartpoint, ystartpoint):
        
        """
        Constructing the Agent class; assigning class variables
        1. Place agents in the environment
        2. Make agents self-aware and of others
        3. Assign each agent a house number
        4. Set agent starting x coordinate to start the at the pub location
        5. Set agent starting y coordinate to start the at the pub location
        6. Add variable to set agent not at home at the start of the model        
        """
        
        self.environment = environment
        self.agents = agents
        self.housenum = housenum
        self._x = xstartpoint
        self._y = ystartpoint
        self.arrived_home = False
        #self.numofsteps = 0
        
        
    def nav (self):
        
        """
        Defining the nav function; allowing drunk agents to navigate the environment
        1. They are limited to walk between the environment edges; thus no torus is implemented
        2. Each agent takes a step in a random direction
        """
        
        if random.random() <0.5:
            xnav=self._x+1
            if xnav<len(self.environment) and xnav>0:
                self._x = xnav
                #self.numofsteps +=1
        else:
            xnav=self._x-1
            if xnav<len(self.environment) and xnav>0:
                self._x = xnav
                #self.numofsteps +=1            
                
        if random.random() <0.5:
            ynav=self._y+1
            if ynav<len(self.environment) and ynav>0:
                self._y = ynav
                #self.numofsteps +=1
        else:
            ynav=self._y-1
            if ynav<len(self.environment) and ynav>0:
                self._y = ynav
                #self.numofsteps +=1