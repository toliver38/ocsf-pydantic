from enum import Enum
from pydantic import BaseModel

class JA4FingerprintTypeId(Enum):
    """
    The identifier of the JA4+ fingerprint type.
    """
    Unknown: int = 0
    JA4: int = 1
    JA4Server: int = 2
    JA4HTTP: int = 3
    JA4Latency: int = 4
    JA4X509: int = 5
    JA4SSH: int = 6
    JA4TCP: int = 7
    JA4TCPServer: int = 8
    JA4TCPScan: int = 9
    Other: int = 99

class JA4Fingerprint(BaseModel):
    """
    The JA4Fingerprint object provides information about a JA4+ fingerprint.
    """

    type_id: JA4FingerprintTypeId # The identifier of the JA4+ fingerprint type.
    value: str # The JA4+ fingerprint value.

    # Optional:
    section_a: str | None = None # The 'a' section of the JA4 fingerprint.
    section_b: str | None = None # The 'b' section of the JA4 fingerprint.
    section_c: str | None = None # The 'c' section of the JA4 fingerprint.
    section_d: str | None = None # The 'd' section of the JA4 fingerprint.
    type: str | None = None # The JA4+ fingerprint type as defined by FoxIO.
