from parkingLot.src.strategy.slotStrategy import SlotStrategy
from parkingLot.src.models.models import VehicleType, ParkingSlot, Gate, SlotStatus


class RandomSlotFindingStrategy(SlotStrategy):
    def get_slot(self, vehicle_type: VehicleType, gate: Gate) -> ParkingSlot:
        for floor in gate.parking_lot.parking_floors:
            if vehicle_type in floor.allowed_vehicle_types:
                for slot in floor.parking_slots_list:
                    if slot.vehicle_type == vehicle_type and slot.parking_slot_status == SlotStatus.AVAILABLE:
                        return slot
        return None