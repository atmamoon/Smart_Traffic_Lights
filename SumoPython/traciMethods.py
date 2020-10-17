import traci
import Light
import sumolib


def addAmbulance(ambulanceID, routeID, viewID, startEdge, endEdge):

    traci.route.add(routeID, [startEdge, endEdge])

    traci.vehicle.add(ambulanceID, routeID, typeID="truck_emergency")
    traci.vehicle.setVehicleClass(ambulanceID, "emergency")
    traci.vehicle.setShapeClass(ambulanceID, "emergency")

    traci.gui.trackVehicle(viewID, ambulanceID)
    traci.gui.setZoom(viewID, 3500)


def control_TLights(vehID, tl_list, edges, network):

    road_id_amb = traci.vehicle.getRoadID(vehID)
    if road_id_amb in edges:
        amb_index = edges.index(road_id_amb)
        v_amb = traci.vehicle.getMaxSpeed(vehID)
        x_lane = traci.vehicle.getLanePosition(vehID)

        for light in tl_list:
            if light.isStateChanged:
                tl_index = edges.index(light.fromEdge)
                if tl_index < amb_index:
                    light.reset()
            else:
                tl_index = edges.index(light.fromEdge)
                dist_to_light = -1 * x_lane
                for i in range(amb_index, tl_index+1):
                    dist_to_light += network.getEdge(edges[i]).getLength()

                est_time = dist_to_light/v_amb
                if est_time <= light.phaseDuration + 5:
                    light.goGreen()
