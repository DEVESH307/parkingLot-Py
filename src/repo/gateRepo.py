class GateRepo:
    def __init__(self):
        self.gate_dict = {}

    def find_gate_by_id(self, gate_id: int):
        if gate_id in self.gate_dict:
            return self.gate_dict[gate_id]
        return None