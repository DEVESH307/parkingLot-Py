class IssueTokenRequest:
    def __init__(self, vehicle_number: str, vehicle_type: str, owner_name: str, gate_id: int):
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type
        self.owner_name = owner_name
        self.gate_id = gate_id
