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

step = 0
delayTime = 0

while traci.simulation.getMinExpectedNumber() > 0:

    if step == 100:
        tm.addAmbulance()
        delayTime = 0.15

    time.sleep(delayTime)
    traci.simulationStep()
    step += 1

print(f"Ended at {step}")

traci.close()
