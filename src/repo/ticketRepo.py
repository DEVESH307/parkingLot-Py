class TicketRepo:
    def __init__(self):
        self.count = -1
        self.tickets = {}

    def save_ticket(self, ticket):
        new_id = self.count + 1
        ticket.id = new_id
        ticket.number = new_id
        self.tickets[new_id] = ticket
        self.count += 1
        return ticket