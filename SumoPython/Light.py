import traci


class Light:

    fromEdge = ""
    toEdge = ""
    trafficLightId = ""
    programId = ""
    phaseDuration = 0
    greenPhase = ""
    isStateChanged = False

    def __init__(self, fromEdge, toEdge, trafficLightId):
        self.toEdge = toEdge
        self.fromEdge = fromEdge
        self.trafficLightId = trafficLightId
        self.programId = traci.trafficlight.getProgram(self.trafficLightId)
        self.phaseDuration = traci.trafficlight.getPhaseDuration(self.trafficLightId)
        self.setGreenPhase()

    def setGreenPhase(self):

        # Kshitij, your code here

        pass

    def goGreen(self):
        traci.trafficlight.setRedYellowGreenState(self.trafficLightId, self.greenPhase)
        self.isStateChanged = True

    def reset(self):
        traci.trafficlight.setProgram(self.trafficLightId, self.programId)
        self.isStateChanged = False

    pass
