import traci


def addAmbulance():

    routeID = "ambulanceRoute"

    # change here  -give edges accordingly
    traci.route.add(routeID, ['-24241790#2', '-4588217#5'])

    ambulanceID = "ambulance"

    traci.vehicle.add(ambulanceID, "ambulanceRoute", typeID="truck_emergency")
    traci.vehicle.setVehicleClass(ambulanceID, "emergency")
    traci.vehicle.setShapeClass(ambulanceID, "emergency")

    viewID = "View #0"

    traci.gui.trackVehicle(viewID, ambulanceID)
    traci.gui.setZoom(viewID, 3500)
