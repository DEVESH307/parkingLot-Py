class VehicleRepo:
    def __init__(self):
        self.vehicle_dict = {}

    def find_vehicle_by_number(self, vehicle_number: str):
        if vehicle_number in self.vehicle_dict:
            return self.vehicle_dict[vehicle_number]
        return None

    def save_vehicle(self, vehicle):
        if vehicle.vehicle_number in self.vehicle_dict:
            raise Exception("Vehicle already exists")
        self.vehicle_dict[vehicle.id] = vehicle
        return vehicle