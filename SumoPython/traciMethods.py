import traci
import Light

def addAmbulance(ambulanceID, routeID, viewID, startEdge, endEdge):

    traci.route.add(routeID, [startEdge, endEdge])

    traci.vehicle.add(ambulanceID, routeID, typeID="truck_emergency")
    traci.vehicle.setVehicleClass(ambulanceID, "emergency")
    traci.vehicle.setShapeClass(ambulanceID, "emergency")

    traci.gui.trackVehicle(viewID, ambulanceID)
    traci.gui.setZoom(viewID, 3500)

# def findLights(vehId):
#
#     allTLIds = traci.trafficlight.getIDList()
#     edges = traci.route.getEdges(traci.vehicle.getRouteID(vehId))
#     lights = []
#
#     for i in range(0, len(edges)-1):
#         for tLId in allTLIds:
#             lanes = traci.trafficlight.getControlledLanes(tLId)
#             cnt = 0
#             for lane in lanes:
#                 tLEdge = laneToEdge(lane)
#                 if tLEdge == edges[i] or tLEdge == edges[i+1]:
#                     cnt += 1
#             if cnt == 2:
#                 lights.append(Light.Light(edges[i], edges[i+1], tLId))
#
#     return lights


def control_TLights(vehID, tl_list, edges):

    road_id_amb = traci.vehicle.getRoadID(vehID)
    if road_id_amb in edges:
        amb_index = edges.index(road_id_amb)
        v_amb = traci.vehicle.getSpeed(vehID) + 0.01
        x_lane = traci.vehicle.getLanePosition(vehID)

        for light in tl_list:

            if not light.isStateChanged:
                tl_index = edges.index(light.fromEdge)
                dist_to_light = 0
                for i in range(amb_index, tl_index+1):
                    dist_to_light += (traci.edge.getTraveltime(edges[i])*traci.edge.getLastStepMeanSpeed(edges[i]))

                est_time = dist_to_light/v_amb
                if est_time <= light.phaseDuration - 5:
                    light.goGreen()
