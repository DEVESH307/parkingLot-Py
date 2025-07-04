import datetime

from parkingLot.src.factory.getSlotFactory import SlotFactory
from parkingLot.src.models.models import Ticket, Vehicle, SlotStatus


class TicketService:
    # dependency injection can be used here for repositories or other services
    def __init__(self, gate_repo, vehicle_repo, parking_slot_repo, parking_lot_repo, ticket_repo):
        self.gate_repo = gate_repo
        self.vehicle_repo = vehicle_repo
        self.parking_slot_repo = parking_slot_repo
        self.parking_lot_repo = parking_lot_repo
        self.ticket_repo = ticket_repo

    def issue_ticket(self, vehicle_number, vehicle_type, owner_name, gate_id) -> Ticket:
        # create ticket
        # set information like ticket number, entry time, vehicle, parking slot, generated gate
        ticket = Ticket(id=-1, number="", entry_time=datetime.datetime.now(), vehicle=None, parking_slot=None, generated_gate=None)
        gate = self.gate_repo.find_gate_by_id(gate_id)
        if not gate:
            raise Exception("Gate not found")
        ticket.generated_gate = gate

        # vehicle info
        vehicle = self.vehicle_repo.find_vehicle_by_number(vehicle_number)
        if not vehicle:
            vehicle = Vehicle(id=vehicle_number, vehicle_number=vehicle_number, vehicle_type=vehicle_type, owner_name=owner_name, owner_contact="")
            vehicle = self.vehicle_repo.save_vehicle(vehicle)
        ticket.vehicle = vehicle

        # finds a slot for the vehicle
        slot_strategy = SlotFactory.get_slot_strategy_object(gate.parking_lot.slot_assignment_strategy)
        if not slot_strategy:
            raise Exception("No slot assignment strategy found")

        slot = slot_strategy.get_slot(vehicle.vehicle_type, gate)
        if not slot:
            raise Exception("No available slot found for the vehicle type")

        ticket.parking_slot = slot

        # update the slot...
        self.parking_slot_repo.update_slot_status(slot, SlotStatus.OCCUPIED)

        # update parking counters
        self.parking_lot_repo.update_parking_lot_count(gate.parking_lot)

        # return the ticket
        return self.ticket_repo.save_ticket(ticket)



