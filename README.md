# EV-Charging-Station-Based-on-parkingArea-of-SUMO

## Description

The charging station class is included in SUMO, but with restricted fuction.  
We can't control the number of charging points and set the power dynamically.  
Using the parkingArea structure and traci, I create a demo of self-made charging station. The number of parking spaces is actually the number of charging points. When an EV stopping, it will be charged with the power of the parameter 'power'.

## input file
h.net.xml (network)  
vehicle.rou.xml (2 EVs)  
char.add.xml (a self-made charging station-parkingarea and a charging station-not being used here)

## configuration
con.sumocfg

## control
tra.py (using traci)

[recording-2022-12-09-17-45-59.webm](https://user-images.githubusercontent.com/28706554/206679914-21b3888d-3232-49b8-92fb-94cc2e34a977.webm)
