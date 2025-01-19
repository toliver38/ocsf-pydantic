from pydantic import BaseModel
from typing import Optional, List
from enum import Enum
from ocsf.objects.autonomous_system import AutonomousSystem
from ocsf.objects.location import GeoLocation
from ocsf.objects.whois import Whois
from ocsf.objects.kill_chain_phase import KillChainPhase
from ocsf.objects.attack import MITREATTCK
from ocsf.objects.dns_answer import DNSAnswer
from ocsf.objects.digital_signature import DigitalSignature
from ocsf.objects.email import Email
from ocsf.objects.email_auth import EmailAuthentication
from ocsf.objects.vulnerability import VulnerabilityDetails

class ConfidenceId(Enum):
    Unknown: int = 0
    Low: int = 1
    Medium: int = 2
    High: int = 3
    Other: int = 99

class IndicatorTypeId(Enum):
    Unknown: int = 0
    IPAddress: int = 1
    Domain: int = 2
    Hostname: int = 3
    Hash: int = 4
    URL: int = 5
    UserAgent: int = 6
    DigitalCertificate: int = 7
    Email: int = 8
    EmailAddress: int = 9
    Vulnerability: int = 10
    Other: int = 99

class TrafficLightProtocol(Enum):
    AMBER = "TLP:AMBER"
    AMBER_STRICT = "TLP:AMBER+STRICT"
    CLEAR = "TLP:CLEAR"
    GREEN = "TLP:GREEN"
    RED = "TLP:RED"

class Osint(BaseModel):
    """
    The OSINT (Open Source Intelligence) object contains details related to an indicator such as the indicator itself, related indicators, geolocation, registrar information, subdomains, analyst commentary, and other contextual information. This information can be used to further enrich a detection or finding by providing decisioning support to other analysts and engineers.
    """

    comment: Optional[str] = None # Analyst commentary or source commentary about an indicator or OSINT analysis.
    autonomous_system: Optional[AutonomousSystem] = None # Any pertinent autonomous system information related to an indicator or OSINT analysis.
    confidence_id: Optional[ConfidenceId] = None # The normalized confidence refers to the accuracy of collected information related to the OSINT or how pertinent an indicator or analysis is to a specific event or finding.
    confidence: Optional[str] = None # The confidence of an indicator being malicious and/or pertinent, normalized to the caption of the confidence_id value.
    location: Optional[GeoLocation] = None # Any pertinent geolocation information related to an indicator or OSINT analysis.
    value: str # The actual indicator value in scope, e.g., a SHA-256 hash hexdigest or a domain name.
    type_id: IndicatorTypeId # The OSINT indicator type ID.
    kill_chain: Optional[List[KillChainPhase]] = None # Lockheed Martin Kill Chain Phases pertinent to an indicator or OSINT analysis.
    attacks: Optional[List[MITREATTCK]] = None # MITRE ATT&CK Tactics, Techniques, and/or Procedures (TTPs) pertinent to an indicator or OSINT analysis.
    name: Optional[str] = None # The name of the entity.
    answers: Optional[List[DNSAnswer]] = None # Any pertinent DNS answers information related to an indicator or OSINT analysis.
    signatures: Optional[List[DigitalSignature]] = None # Any digital signatures or hashes related to an indicator or OSINT analysis.
    email: Optional[Email] = None # Any email information pertinent to an indicator or OSINT analysis.
    email_auth: Optional[EmailAuthentication] = None # Any email authentication information pertinent to an indicator or OSINT analysis.
    subdomains: Optional[List[str]] = None # Any pertinent subdomain information - such as those generated by a Domain Generation Algorithm - related to an indicator or OSINT analysis.
    vulnerabilities: Optional[List[VulnerabilityDetails]] = None # Any vulnerabilities related to an indicator or OSINT analysis.
    src_url: Optional[str] = None # The source URL of an indicator or OSINT analysis, e.g., a URL back to a TIP, report, or otherwise.
    tlp: TrafficLightProtocol # The Traffic Light Protocol was created to facilitate greater sharing of potentially sensitive information and more effective collaboration.
    type: Optional[str] = None # The OSINT indicator type.
    uid: Optional[str] = None # The unique identifier of the entity.
    vendor_name: Optional[str] = None # The vendor name of a tool which generates intelligence or provides indicators.
    whois: Optional[Whois] = None # Any pertinent WHOIS information related to an indicator or OSINT analysis.
