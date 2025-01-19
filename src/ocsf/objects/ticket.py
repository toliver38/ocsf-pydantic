from pydantic import BaseModel
from typing import Optional
from enum import Enum

class TicketTypeId(Enum):
    Unknown: int = 0
    Internal: int = 1
    External: int = 2
    Other: int = 99

class Ticket(BaseModel):
    """
    The Ticket object represents a ticket in the customer's systems like Salesforce, Jira, etc.
    """

    src_url: Optional[str] = None # The URL of a ticket in the ticket system.
    type_id: Optional[TicketTypeId] = None # The normalized identifier for the ticket type.
    type: Optional[str] = None # The linked ticket type determines whether the ticket is internal or in an external ticketing system.
    title: Optional[str] = None # The title of the ticket.
    uid: Optional[str] = None # Unique ticket identifier like ticket id.
