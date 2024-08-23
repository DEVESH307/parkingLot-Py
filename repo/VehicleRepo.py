from models.models import Vehicle


class VehicleRepo:
    def __init__(self):
        self.vehicleMap = {}

    def find_vehicle_by_number(self, number):
        if number in self.vehicleMap:
            return self.vehicleMap[number]
        return None

    def save_vehicle(self, vehicle):
        self.vehicleMap[vehicle.number] = vehicle
        return vehicle