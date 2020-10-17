import traci


def laneToEdge(laneId):
    return laneId[:len(laneId)-2]


class Light:

    fromEdge = ""
    trafficLightId = ""
    programId = ""
    phaseDuration = 0
    greenPhase = ""
    isStateChanged = False

    def __init__(self, fromEdge, trafficLightId):
        self.fromEdge = fromEdge
        self.trafficLightId = trafficLightId
        self.programId = traci.trafficlight.getProgram(self.trafficLightId)
        self.phaseDuration = traci.trafficlight.getPhaseDuration(self.trafficLightId)
        self.setGreenPhase()

    def setGreenPhase(self):
        links = traci.trafficlight.getControlledLinks(self.trafficLightId)
        state = traci.trafficlight.getRedYellowGreenState(self.trafficLightId)
        N = len(state)
        for i in range(0, N):
            if laneToEdge(links[i][0][0]) == self.fromEdge:
                self.greenPhase += "G"
            else:
                self.greenPhase += "r"

    def goGreen(self):
        traci.trafficlight.setRedYellowGreenState(self.trafficLightId, self.greenPhase)
        self.isStateChanged = True

    def reset(self):
        traci.trafficlight.setProgram(self.trafficLightId, self.programId)
        self.isStateChanged = False

    pass
