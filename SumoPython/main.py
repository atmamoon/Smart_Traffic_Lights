import os
import sys
import traci
import traciMethods as tm
import time
import Light

# change here  -path to your sumo\tools directory
sys.path.append(os.path.join('F:\\SUMO\\sumo\\tools'))

# change here
path_SumoGui = "F:\\bin\\sumo-gui"

# change here
path_sumocfg_file = "C:\\Users\\narwayaayush\\Sumo\\trial\\osm.sumocfg"

sumoCmd = [path_SumoGui, "-c", path_sumocfg_file]

# change here
startEdge = '-24241790#2'
endEdge = '-4588217#1'
routeID = "ambulanceRoute"
ambulanceID = "ambulance"
viewID = "View #0"

traci.start(sumoCmd)

print("started")

step = 0
last = startEdge
tLights = []
edges = []
allTLIds = []
isAmbulancePresent = False

while step < 1500:

    if isAmbulancePresent:
        traci.vehicle.setSpeed(ambulanceID, traci.vehicle.getMaxSpeed(ambulanceID) * 0.05)
        if last != traci.vehicle.getRoadID(ambulanceID):
            last = traci.vehicle.getRoadID(ambulanceID)
            if last[len(last)-2] == "#":
                edges.append(last)
            elif last[1:len(last)-2] in allTLIds:
                tLights.append(Light.Light(edges[len(edges) - 1], last[1:len(last)-2]))
            elif last[1:len(last)-3] in allTLIds:
                tLights.append(Light.Light(edges[len(edges) - 1], last[1:len(last)-3]))

        if traci.vehicle.getRoadID(ambulanceID) == endEdge:
            isAmbulancePresent = False

    if step == 100:
        isAmbulancePresent = True
        tm.addAmbulance(ambulanceID, routeID, viewID, startEdge, endEdge)
        allTLIds = traci.trafficlight.getIDList()
        edges.append(startEdge)

    traci.simulationStep()
    step += 1

print(f"Ended at {step}")

traci.close()

traci.start(sumoCmd)

step = 0
delayTime = 0
light = "cluster_1828018077_1828018093_1828018094_1828018095_1840326399_1840326421_262469034_29123671_29123672_3832550626_3832550632_6795935360_6795935361_6795935362_967017837_967017877"
links = traci.trafficlight.getControlledLinks(light)
print("started")

while step < 455:

    if isAmbulancePresent:
        tm.control_TLights(ambulanceID, tLights, edges)

        if traci.vehicle.getRoadID(ambulanceID) == endEdge:
            isAmbulancePresent = False

    if step == 100:

        isAmbulancePresent = True
        tm.addAmbulance(ambulanceID, routeID, viewID, startEdge, endEdge)
        # tLights = tm.findLights(ambulanceID)
        delayTime = 0.15

    time.sleep(delayTime)
    traci.simulationStep()
    step += 1

print(f"Ended at {step}")

traci.close()