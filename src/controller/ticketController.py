from parkingLot.src.dtos.issueTokenRequest import IssueTokenRequest
from parkingLot.src.dtos.ticketResponse import TicketResponse
from parkingLot.src.service.ticketService import TicketService


class TicketController:
    def __init__(self, ticket_service: TicketService):
        self.ticket_service = ticket_service

    def issue_ticket(self, request: IssueTokenRequest) -> TicketResponse:
        ticket = self.ticket_service.issue_ticket(request.vehicle_number,
                                         request.vehicle_type,
                                         request.owner_name,
                                         request.gate_id)
        response = TicketResponse()
        response.ticket_id = ticket.id
        response.entry_time = ticket.entry_time
        response.slot = ticket.parking_slot
        # response.status = ticket.parking_slot.parking_slot_status.name
        response.status = "SUCCESS"
        response.floor = ticket.parking_slot.parking_floor.floor_number
        response.vehicle = ticket.vehicle.vehicle_number
        return response