class Vehicle:
    vehicle_id: str = ""
    type_vehicle: int = 0
    x_coordinate: int = 0
    y_coordinate: int = 0
    status: str = ""
    battery: float = 0.0

    def __int__(self, vehicle_id, type_vehicle, x_coordinate, y_coordinate, status, battery):
        self.vehicle_id = vehicle_id
        self.type_vehicle = type_vehicle
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.status = status
        self.battery = battery

    def getVehicleInfo(self):
        print("Vehicle ID: ", self.vehicle_id, "\nType of Vehicle: ", self.type_vehicle, "\nX coordinate: ",
              self.x_coordinate, "\nY coordinate: ", self.y_coordinate, "\nStatus: ", self.status, "\nBattery: ",
              self.battery)
