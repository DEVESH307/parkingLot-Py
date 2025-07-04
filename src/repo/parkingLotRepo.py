from parkingLot.src.models.models import ParkingLot


class ParkingLotRepo:
    def __init__(self):
        self.parking_lots = {}

    def update_parking_lot_count(self, parking_lot: ParkingLot):
        # in multithreaded environment, we should use mutex or lock to avoid race conditions
        parking_lot.capacity -= 1
        self.parking_lots[parking_lot.id] = parking_lot
        return parking_lot
