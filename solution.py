import pandas as pandas
import numpy as numpy

pandas.options.mode.chained_assignment = None  
readData = pandas.read_csv('shots_data.csv')
print("----------------------------------------------------------------------------------")
teamAStats = readData[readData["team"] == "Team A"]
teamBStats = readData[readData["team"] == "Team B"]


def getData(meas, team):
    meas["distance"] = numpy.sqrt(meas["x"] ** 2 + meas["y"] ** 2) #distance measurement with square root of 2
    meas["corner"] = meas["y"] <= 7.8

    
    twoPoints = meas[numpy.logical_and(numpy.logical_not(numpy.logical_and(meas["corner"], abs(meas["x"]) >= 22)), numpy.logical_not(numpy.logical_and(numpy.logical_not(meas["corner"]), meas["distance"] >= 23.75)))]
    nc3ZoneP = meas[numpy.logical_and(numpy.logical_not(meas["corner"]), meas["distance"] >= 23.75)]
    c3ZoneP = meas[numpy.logical_and(meas["corner"], abs(meas["x"]) >= 22)]
    

    shotsTotal = float(len(meas))
    
    twoPointDist = len(twoPoints) / shotsTotal
    threeNPointDist = len(nc3ZoneP) / shotsTotal
    c3zoneShotDist = len(c3ZoneP) / shotsTotal 
    print(f'{team} 2PT zone shot dstr = {twoPointDist}')  
    print(f'{team} NC3 zone shot dstr = {threeNPointDist}')
    print(f'{team} C3 zone shot dstr  = {c3zoneShotDist}')

    twoPointsFGM = numpy.sum(twoPoints["fgmade"])
    nc3ZonePointsFGM = numpy.sum(nc3ZoneP["fgmade"])
    c3ZonePointsFGM = numpy.sum(c3ZoneP["fgmade"])
 

    print(f'{team} 2PT zone fg percentage: {twoPointsFGM / len(twoPoints)}')
    print(f'{team} NC3 zone fg percentage: {nc3ZonePointsFGM * 1.5 / len(nc3ZoneP)}')
    print(f'{team} C3 zone fg percentage: { c3ZonePointsFGM * 1.5 / len(c3ZoneP)}')
    del c3ZoneP
    del twoPoints
    del nc3ZoneP
    

getData(teamAStats, "Team A")

print("----------------------------------------------------------------------------------")

getData(teamBStats, "Team B")
print("----------------------------------------------------------------------------------")