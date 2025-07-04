from abc import ABC, abstractmethod

from parkingLot.src.models.models import VehicleType, ParkingSlot, Gate


class SlotStrategy(ABC):
    @abstractmethod
    def get_slot(self, vehicle_type: VehicleType, gate: Gate) -> ParkingSlot:
        pass
