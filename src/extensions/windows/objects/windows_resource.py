from pydantic import BaseModel
from typing import Optional
from enum import Enum

class TypeId(Enum):
    Unknown: int = 0
    Directory: int = 1
    Event: int = 2
    Timer: int = 3
    Device: int = 4
    Mutant: int = 5
    Type: int = 6
    File: int = 7
    Token: int = 8
    Thread: int = 9
    Section: int = 10
    WindowStation: int = 11
    DebugObject: int = 12
    FilterCommunicationPort: int = 13
    EventPair: int = 14
    Driver: int = 15
    IoCompletion: int = 16
    Controller: int = 17
    SymbolicLink: int = 18
    WmiGuid: int = 19
    Process: int = 20
    Profile: int = 21
    Desktop: int = 22
    KeyedEvent: int = 23
    Adapter: int = 24
    Key: int = 25
    WaitablePort: int = 26
    Callback: int = 27
    Semaphore: int = 28
    Job: int = 29
    Port: int = 30
    FilterConnectionPort: int = 31
    ALPCPort: int = 32
    SAM_ALIAS: int = 33
    SAM_GROUP: int = 34
    SAM_USER: int = 35
    SAM_DOMAIN: int = 36
    SAM_SERVER: int = 37
    Other: int = 99

class WindowsResource(BaseModel):
    """
    The Windows resource object describes a resource object managed by Windows, such as mutant or timer.
    """

    type_id: TypeId # The normalized type identifier of the Windows resource object accessed.
    name: Optional[str] = None # The name of the resource object.
    uid: Optional[str] = None # The Windows provided handle identifier for the resource object.
    data: Optional[dict] = None # Additional data describing the resource.
    details: Optional[str] = None # The string detailing the attributes of the resource object.
    labels: Optional[list[str]] = None # The list of labels/tags associated to a resource.
    svc_name: Optional[str] = None # The Windows service acting as the object server for the resource object, such as Security or Security Account Manager.
    type: Optional[str] = None # The type of the Windows resource object.
