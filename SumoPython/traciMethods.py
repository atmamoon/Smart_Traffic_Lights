import traci
import main

def addAmbulance(ambulanceID, routeID, viewID, startEdge, endEdge):

    traci.route.add(routeID, [startEdge, endEdge])

    traci.vehicle.add(ambulanceID, routeID, typeID="truck_emergency")
    traci.vehicle.setVehicleClass(ambulanceID, "emergency")
    traci.vehicle.setShapeClass(ambulanceID, "emergency")

    traci.gui.trackVehicle(viewID, ambulanceID)
    traci.gui.setZoom(viewID, 3500)



def control_TLights(tl_list):
    critical_time=5

    lane_id_amb=traci._vehicle.getLaneID(vehID)
    road_id_amb=traci._vehicle.getRoadID(vehID)
    v_amb=traci._vehicle.getSpeed(self, vehID)
    x_lane=traci._vehicle.getLanePosition(vehID)

    for light in tl_list:
        dist_to_light=454
        est_time=dist_to_light/v_amb
        if est_time<=critical_time:
            state=""
            traci._trafficlight.setLinkState(light.tlsID, tlsLinkIndex, state)
