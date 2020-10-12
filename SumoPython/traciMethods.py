import traci


def addAmbulance(ambulanceID, routeID, viewID, startEdge, endEdge):

    traci.route.add(routeID, [startEdge, endEdge])

    traci.vehicle.add(ambulanceID, routeID, typeID="truck_emergency")
    traci.vehicle.setVehicleClass(ambulanceID, "emergency")
    traci.vehicle.setShapeClass(ambulanceID, "emergency")

    traci.gui.trackVehicle(viewID, ambulanceID)
    traci.gui.setZoom(viewID, 3500)
