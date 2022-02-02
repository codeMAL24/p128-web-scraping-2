from bs4 import BeautifulSoup as bs
from flask import request
import requests
import pandas as pd
 

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(START_URL)
soup = bs(page.text,"html.parser")
starTable = soup.find_all("table")

templist = []
tablerows = starTable[7].find_all("tr")
for tr in tablerows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]   
    templist.append(row)

starname = []
distance = []
mass = []
radius = []

for i in range(1,len(templist)):
    starname.append(templist[i][0])
    distance.append(templist[i][5])
    mass.append(templist[i][7])
    radius.append(templist[i][8])
df2 = pd.DataFrame(list(zip(starname, distance , mass ,radius)), columns = ["name","distance","mass","radius",]) 
df2.to_csv("starFinal.csv")   



