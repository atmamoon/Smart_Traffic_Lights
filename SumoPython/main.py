import os
import sys
import traci
import traciMethods as tm
import time

# change here  -path to your sumo\tools directory
sys.path.append(os.path.join('F:\\SUMO\\sumo\\tools'))

# change here
path_SumoGui = "F:\\bin\\sumo-gui"

# change here
path_sumocfg_file = "C:\\Users\\narwayaayush\\Sumo\\trial\\osm.sumocfg"

sumoCmd = [path_SumoGui, "-c", path_sumocfg_file]

traci.start(sumoCmd)

print("started")

# change here
startEdge = '-24241790#2'
endEdge = '-4588217#1'
routeID = "ambulanceRoute"
ambulanceID = "ambulance"
viewID = "View #0"

step = 0
delayTime = 0
isAmbulancePresent = False

while traci.simulation.getMinExpectedNumber() > 0:

    if step == 100:
        tm.addAmbulance(ambulanceID, routeID, viewID, startEdge, endEdge)
        delayTime = 0.15
        isAmbulancePresent = True

    time.sleep(delayTime)
    traci.simulationStep()
    step += 1

print(f"Ended at {step}")

traci.close()
