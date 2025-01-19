from pydantic import BaseModel
from typing import Optional, List
from enum import Enum
from ocsf.objects.autonomous_system import AutonomousSystem
from ocsf.objects.domain_contact import DomainContact
from datetime import datetime

class DnssecStatusId(Enum):
    Unknown: int = 0
    Signed: int = 1
    Unsigned: int = 2
    Other: int = 99

class Whois(BaseModel):
    """
    The resources of a WHOIS record for a given domain. This can include domain names, IP address blocks, autonomous system information, and/or contact and registration information for a domain.
    """

    autonomous_system: Optional[AutonomousSystem] = None # The autonomous system information associated with a domain.
    dnssec_status_id: Optional[DnssecStatusId] = None # Describes the normalized status of DNS Security Extensions (DNSSEC) for a domain.
    dnssec_status: Optional[str] = None # The normalized value of dnssec_status_id.
    domain: str # The name of the domain.
    domain_contacts: List[DomainContact] # An array of Domain Contact objects.
    registrar: str # The domain registrar.
    status: str # The status of a domain and its ability to be transferred, e.g., clientTransferProhibited.
    last_seen_time: datetime # When the WHOIS record was last updated or seen at.
    name_servers: List[str] # A collection of name servers related to a domain registration or other record.
    created_time: datetime # When the domain was registered or WHOIS entry was created.
    email_addr: Optional[str] = None # The email address for the registrar's abuse contact.
    phone_number: Optional[str] = None # The phone number for the registrar's abuse contact.
    subdomains: Optional[List[str]] = None # An array of subdomain strings. Can be used to collect several subdomains such as those from Domain Generation Algorithms (DGAs).
    subnet: Optional[str] = None # The IP address block (CIDR) associated with a domain.
