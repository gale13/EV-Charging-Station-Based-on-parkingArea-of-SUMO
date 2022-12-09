#coding=utf-8
import traci
import time
import traci.constants as tc
import pytz
from random import randrange
import pandas as pd


sumoCmd = ["sumo-gui","-c","con.sumocfg"]
traci.start(sumoCmd)

maxcap=2000

power=50

wait = []
charge = []
cache={}
step = 0
while traci.simulation.getMinExpectedNumber()>0:
	traci.simulationStep()
	vehicles=traci.vehicle.getIDList()
	step+=1
	for i in range(len(vehicles)):
		vehid = vehicles[i]
		rembat=float(traci.vehicle.getParameter(vehid, "device.battery.actualBatteryCapacity"))
		#print(rembat)
		if (rembat<600 and (vehid not in wait) and (vehid not in charge)):
			#edge = traci.vehicle.getRoadID(vehid)
			target = traci.vehicle.getRoute(vehid)
			#print(target)
			target = target[len(target)-1]
			cache[vehid]=target
			traci.vehicle.changeTarget(vehid,"E3")
			traci.vehicle.setParkingAreaStop(vehid, "ParkAreaB", duration=2, flags=1)
			wait.append(vehid)
		if (vehid in wait):
			if (traci.vehicle.isStoppedParking(vehid)):
				print(11)
				wait.remove(vehid)
				charge.append(vehid)
		if (vehid in charge):
			if (float(traci.vehicle.getParameter(vehid, "device.battery.actualBatteryCapacity"))>maxcap-0.1):
				charge.remove(vehid)
				traci.vehicle.changeTarget(vehid,cache[vehid])
			else:
				currentcap=float(traci.vehicle.getParameter(vehid, "device.battery.actualBatteryCapacity"))
				print(currentcap)
				traci.vehicle.setParameter(vehid, "device.battery.actualBatteryCapacity",currentcap+power)
				traci.vehicle.setParkingAreaStop(vehid, "ParkAreaB", duration=2,flags=1)


traci.close()