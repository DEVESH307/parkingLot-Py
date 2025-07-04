from datetime import datetime
from enum import Enum
from typing import List

class BaseModel:
    def __init__(self, id: int):
        self.id = id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


class BillStatus(Enum):
    PENDING = "pending"
    PAID = "paid"
    PARTIALLY_PAID = "partially paid"
    CANCELLED = "cancelled"

class FloorStatus(Enum):
    OPEN = "open"
    CLOSED = "closed"
    FULL = "full"
    UNDER_MAINTENANCE = "under maintenance"

class GateStatus(Enum):
    OPEN = "open"
    CLOSED = "closed"
    LOCKED = "locked"
    UNDER_MAINTENANCE = "under maintenance"

class GateType(Enum):
    ENTRY = "entry"
    EXIT = "exit"

class ParkingLotStatus(Enum):
    OPEN = "open"
    CLOSED = "closed"
    FULL = "full"
    UNDER_MAINTENANCE = "under maintenance"

class PaymentModes(Enum):
    CASH = "cash"
    CARD = "card"
    ONLINE = "online"
    WALLET = "wallet"
    UPI = "upi"

class PaymentStatus(Enum):
    SUCCESS = "success"
    PENDING = "pending"
    FAILED = "failed"
    REFUNDED = "refunded"

class SlotStatus(Enum):
    AVAILABLE = "available"
    OCCUPIED = "occupied"
    RESERVED = "reserved"
    BLOCKED = "blocked"
    UNDER_MAINTENANCE = "under maintenance"

class SlotAssignmentStrategyEum(Enum):
    FIRST_COME_FIRST_SERVE = "first come first serve"
    RANDOM = "random"

class VehicleType(Enum):
    CAR = "car"
    BIKE = "bike"
    TRUCK = "truck"
    BUS = "bus"
    VAN = "van"


# inherit from BaseModel for common attributes
class Bill(BaseModel):
    def __init__(self,
                 id: int,
                 exit_time: datetime,
                 token,
                 exited_at,
                 payments: List,
                 total_amount: float,
                 bill_status: BillStatus):
        super().__init__(id)
        self.exit_time = exit_time
        self.token = token
        self.exited_at = exited_at
        self.payments = payments
        self.total_amount = total_amount
        self.bill_status = bill_status

class Floor(BaseModel):
    def __init__(self,
                 id: int,
                 parking_slots_list: List,
                 floor_number: int,
                 floor_status: FloorStatus,
                 allowed_vehicle_types: List[VehicleType]):
        super().__init__(id)
        self.parking_slots_list = parking_slots_list
        self.floor_number = floor_number
        self.floor_status = floor_status
        self.allowed_vehicle_types = allowed_vehicle_types

class Gate(BaseModel):
    def __init__(self,
                 id: int,
                 gate_number: int,
                 gate_type: GateType,
                 parking_lot,
                 gate_status: GateStatus):
        super().__init__(id)
        self.gate_number = gate_number
        self.gate_type = gate_type
        self.parking_lot = parking_lot
        self.gate_status = gate_status

class ParkingLot(BaseModel):
    def __init__(self,
                 id: int,
                 name: str,
                 address: str,
                 parking_floors: List[Floor],
                 gates: List[Gate],
                 allowed_vehicle_types: List[VehicleType],
                 capacity: int,
                 status: ParkingLotStatus,
                 slot_assignment_strategy: SlotAssignmentStrategyEum):
        super().__init__(id)
        self.name = name
        self.address = address
        self.parking_floors = parking_floors
        self.gates = gates
        self.allowed_vehicle_types = allowed_vehicle_types
        self.capacity = capacity
        self.status = status
        self.slot_assignment_strategy = slot_assignment_strategy

class Payment(BaseModel):
    def __init__(self,
                 id: int,
                 amount: float,
                 payment_mode: PaymentModes,
                 reference_id: str,
                 bill,
                 payment_status: PaymentStatus,
                 paid_at: datetime):
        super().__init__(id)
        self.amount = amount
        self.payment_mode = payment_mode
        self.reference_id = reference_id
        self.bill = bill
        self.payment_status = payment_status
        self.paid_at = paid_at

class ParkingSlot(BaseModel):
    def __init__(self,
                 id: int,
                 slot_number: int,
                 vehicle_type: VehicleType,
                 parking_slot_status: SlotStatus,
                 parking_floor: Floor):
        super().__init__(id)
        self.slot_number = slot_number
        self.vehicle_type = vehicle_type
        self.parking_slot_status = parking_slot_status
        self.parking_floor = parking_floor

class Ticket(BaseModel):
    def __init__(self,
                 id: int,
                 number: str,
                 entry_time: datetime,
                 vehicle,
                 parking_slot: ParkingSlot,
                 generated_gate: Gate):
        super().__init__(id)
        self.number = number
        self.entry_time = entry_time
        self.vehicle = vehicle
        self.parking_slot = parking_slot
        self.generated_gate = generated_gate

class Vehicle(BaseModel):
    def __init__(self,
                 id: int,
                 vehicle_number: str,
                 vehicle_type: VehicleType,
                 owner_name: str,
                 owner_contact: str):
        super().__init__(id)
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type
        self.owner_name = owner_name
        self.owner_contact = owner_contact
