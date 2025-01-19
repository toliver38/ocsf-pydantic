from pydantic import BaseModel
from typing import Optional
from enum import Enum
from ocsf.objects.location import GeoLocation

class DomainContactTypeId(Enum):
    Unknown: int = 0
    Registrant: int = 1
    Administrative: int = 2
    Technical: int = 3
    Billing: int = 4
    Abuse: int = 5
    Other: int = 99

class DomainContact(BaseModel):
    """
    The contact information related to a domain registration, e.g., registrant, administrator, abuse, billing, or technical contact.
    """

    email_addr: Optional[str] = None # The user's primary email address.
    location: Optional[GeoLocation] = None # Location details for the contact such as the city, state/province, country, etc.
    type_id: DomainContactTypeId # The normalized domain contact type ID.
    type: Optional[str] = None # The Domain Contact type, normalized to the caption of the type_id value.
    name: Optional[str] = None # The individual or organization name for the contact.
    phone_number: Optional[str] = None # The number associated with the phone.
    uid: Optional[str] = None # The unique identifier of the contact information, typically provided in WHOIS information.
