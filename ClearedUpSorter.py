#!/usr/bin/env python
# coding: utf-8

# In[1]:


#ALL IMPORTS

import requests
import re
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import base64
import time


# In[23]:





# In[3]:


x = User("sakethgn", "29EE1EA4-E58E-423C-B89E-A5B9FCCECB02")
print(x.auth)


# In[27]:


class BasicScouter:
    def __init__(self, username, authToken):
        self.username = username
        self.authToken = authToken
        self.auth = "Basic: " + base64.b64encode((username + ":" + authToken).encode("ascii")).decode("ascii")
    def findAllBetween(a, b, c):
        if a in c and b in c:
            print(a)
            print(b)
            print(c)
            return re.findall(r'(?:{a})(.*?)(?:{b})'.format(a = a, b = b), c)
        else:
            return "Couldn't find value"
class Scouter(BasicScouter):
    def __init__(self, username, authToken, year, numLookup):
        self.auth = "Basic: " + base64.b64encode((username + ":" + authToken).encode("ascii")).decode("ascii")
        self.year = year
        self.numLookup = numLookup
        self.allData = []
        self.allTeams = []
    def setAllTeams(self, eventCode = None, teams = None):
        if teams != None:
            allTeams = teams
            return
        elif eventCode != None:
            req = requests.get("http://ftc-api.firstinspires.org/v2.0/{season}/teams".format(season = year), headers = headers, params={'eventCode':tournamentCode})
            
    def generateData(self):
        return self.auth


# In[28]:


x = Scouter("sakethgn", "29EE1EA4-E58E-423C-B89E-A5B9FCCECB02", 2022, 3)
print(x.getAuth())


# In[76]:


def getTime():
    return time.time()-startTime

def resetTime():
    global startTime
    startTime = time.time()


# In[82]:


getTime()


# In[83]:


resetTime()


# In[84]:


getTime()


# In[ ]:




