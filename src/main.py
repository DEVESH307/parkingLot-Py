from parkingLot.src.controller.ticketController import TicketController
from parkingLot.src.dtos.issueTokenRequest import IssueTokenRequest
from parkingLot.src.models.models import ParkingLot, ParkingLotStatus, SlotAssignmentStrategyEum, Floor, VehicleType, \
    FloorStatus, ParkingSlot, SlotStatus, Gate, GateType, GateStatus
from parkingLot.src.repo.gateRepo import GateRepo
from parkingLot.src.repo.parkingLotRepo import ParkingLotRepo
from parkingLot.src.repo.parkingSlotRepo import ParkingSlotRepo
from parkingLot.src.repo.ticketRepo import TicketRepo
from parkingLot.src.repo.vehicleRepo import VehicleRepo
from parkingLot.src.service.ticketService import TicketService

def setup_initial_data(gate_repo: GateRepo, parking_lot_repo: ParkingLotRepo, parking_slot_repo: ParkingSlotRepo):
    # Create ParkingLot
    parking_lot = ParkingLot(
        id=1,
        name="Main Parking Lot",
        address="123 Main St",
        parking_floors=[],
        gates=[],
        allowed_vehicle_types=[VehicleType.CAR, VehicleType.BIKE],
        capacity=100,
        status=ParkingLotStatus.OPEN,
        slot_assignment_strategy=SlotAssignmentStrategyEum.RANDOM
    )

    # Create Floor
    floor = Floor(
        id=1,
        parking_slots_list=[],
        floor_number=1,
        floor_status=FloorStatus.OPEN,
        allowed_vehicle_types=[VehicleType.CAR, VehicleType.BIKE]
    )

    # Create Slots
    slot1 = ParkingSlot(
        id=1,
        slot_number=1,
        vehicle_type=VehicleType.CAR,
        parking_slot_status=SlotStatus.AVAILABLE,
        parking_floor=floor
    )

    slot2 = ParkingSlot(
        id=2,
        slot_number=2,
        vehicle_type=VehicleType.BIKE,
        parking_slot_status=SlotStatus.AVAILABLE,
        parking_floor=floor
    )

    # Assign Slots to Floor
    floor.parking_slots_list = [slot1, slot2]

    # Assign Floor to ParkingLot
    parking_lot.parking_floors = [floor]

    # Create Gates
    gate = Gate(
        id=1,
        gate_number=1,
        gate_type=GateType.ENTRY,
        parking_lot=parking_lot,
        gate_status=GateStatus.OPEN
    )

    # Assign Gates to ParkingLot
    parking_lot.gates = [gate]

    # Save to Repositories
    gate_repo.gate_dict[gate.id] = gate
    parking_lot_repo.parking_lots[parking_lot.id] = parking_lot
    parking_slot_repo.slots[slot1.id] = slot1
    parking_slot_repo.slots[slot2.id] = slot2


if __name__ == '__main__':
    gate_repo = GateRepo()
    vehicle_repo = VehicleRepo()
    parking_slot_repo = ParkingSlotRepo()
    parking_lot_repo = ParkingLotRepo()
    ticket_repo = TicketRepo()
    setup_initial_data(gate_repo, parking_lot_repo, parking_slot_repo)

    ticket_service = TicketService(gate_repo, vehicle_repo, parking_slot_repo, parking_lot_repo, ticket_repo)

    ticket_controller = TicketController(ticket_service)

    # First request for a car
    car_request = IssueTokenRequest(
        vehicle_number="KA01MR1234",
        vehicle_type=VehicleType.CAR,
        owner_name="Devesh Jaiswal",
        gate_id=1
    )
    car_response = ticket_controller.issue_ticket(car_request)
    print(f"Car Ticket Response: {car_response}")
    print(f"ticket_id: {car_response.ticket_id}")
    print(f"entry_time: {car_response.entry_time}")
    print(f"slot: {car_response.slot.slot_number}")
    print(f"status: {car_response.status}")
    print(f"floor: {car_response.floor}")
    print(f"vehicle: {car_response.vehicle}")

    # Second request for a bike
    bike_request = IssueTokenRequest(
        vehicle_number="KA02AB5678",
        vehicle_type=VehicleType.BIKE,
        owner_name="Rahul Sharma",
        gate_id=1
    )
    bike_response = ticket_controller.issue_ticket(bike_request)
    print(f"Bike Ticket Response: {bike_response}")
    print(f"ticket_id: {bike_response.ticket_id}")
    print(f"entry_time: {bike_response.entry_time}")
    print(f"slot: {bike_response.slot.slot_number}")
    print(f"status: {bike_response.status}")
    print(f"floor: {bike_response.floor}")
    print(f"vehicle: {bike_response.vehicle}")

# BILL CONTROLLER, BILL SERVICE, BILL REPO
