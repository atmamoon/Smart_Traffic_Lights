import os
import sys
import traci
import traciMethods as tm
import time
import Light
import sumolib

# change here  -path to your sumo\tools directory
sys.path.append(os.path.join('F:\\SUMO\\sumo\\tools'))

# change here
path_SumoGui = "F:\\bin\\sumo-gui"

# change here
# path_sumocfg_file = "F:\\SUMO\\sumo\\tools\\2020-10-17-20-16-48\\osm.sumocfg" #0.8
path_sumocfg_file = "C:\\Users\\narwayaayush\\Sumo\\trial\\osm.sumocfg" #0.72

#change here
# path_network_file = "F:\\SUMO\\sumo\\tools\\2020-10-17-20-16-48\\osm.net.xml"
path_network_file = "C:\\Users\\narwayaayush\\Sumo\\trial\\osm.net.xml"
network = sumolib.net.readNet(path_network_file)

sumoCmd = [path_SumoGui, "-c", path_sumocfg_file]

# change here
# startEdge = '-4613293'  # 0.76
startEdge = '-24241790#2' # 0.73

# endEdge = '326116285#2'
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
delayTime = 0

while step < 455:

    if isAmbulancePresent:
        if last != traci.vehicle.getRoadID(ambulanceID):
            last = traci.vehicle.getRoadID(ambulanceID)
            if last[0] != ":":
                edges.append(last)
            elif last[1:len(last)-2] in allTLIds:
                tLights.append(Light.Light(edges[len(edges) - 1], last[1:len(last)-2]))
            elif last[1:len(last)-3] in allTLIds:
                tLights.append(Light.Light(edges[len(edges) - 1], last[1:len(last)-3]))

        if traci.vehicle.getRoadID(ambulanceID) == endEdge:
            initialTime = step
            print(f'Initial Completion Time = {step}')
            delayTime = 0
            isAmbulancePresent = False

    if step == 100:
        isAmbulancePresent = True
        tm.addAmbulance(ambulanceID, routeID, viewID, startEdge, endEdge)
        allTLIds = traci.trafficlight.getIDList()
        edges.append(startEdge)
        delayTime = 0.1

    time.sleep(delayTime)
    traci.simulationStep()
    step += 1

print(f"Ended at {step}")

traci.close()

traci.start(sumoCmd)

step = 0
delayTime = 0
print("started")

while step < 340:

    if isAmbulancePresent:
        traci.vehicle.setSpeed(ambulanceID,traci.vehicle.getMaxSpeed(ambulanceID))
        tm.control_TLights(ambulanceID, tLights, edges, network)

        if traci.vehicle.getRoadID(ambulanceID) == endEdge:
            finalTime = step
            print(f'Final Completion Time = {step}')
            print(f"Improvement = {finalTime*100/initialTime}%")
            delayTime = 0
            isAmbulancePresent = False

    if step == 100:

        isAmbulancePresent = True
        tm.addAmbulance(ambulanceID, routeID, viewID, startEdge, endEdge)
        delayTime = 0.1

    time.sleep(delayTime)
    traci.simulationStep()
    step += 1

print(f"Ended at {step}")

traci.close()
