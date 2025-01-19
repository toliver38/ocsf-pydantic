from datetime import datetime
from typing import Optional
from ocsf.objects.actor import Actor
from ocsf.objects.device import Device
from ocsf.events.discovery import Discovery
from extensions.windows.objects.registry_key import RegistryKey
from ocsf.objects.metadata import Metadata
from ocsf.objects.observable import Observable
from enum import Enum

class ActivityId(Enum):
    Unknown: int = 0
    Create: int = 1
    Read: int = 2
    Modify: int = 3
    Delete: int = 4
    Rename: int = 5
    SetSecurity: int = 6
    Restore: int = 7
    Import: int = 8
    Export: int = 9
    Other: int = 99

class SeverityId(Enum):
    Unknown: int = 0
    Informational: int = 1
    Low: int = 2
    Medium: int = 3
    High: int = 4
    Critical: int = 5
    Fatal: int = 6
    Other: int = 99

class StatusId(Enum):
    Unknown: int = 0
    Success: int = 1
    Failure: int = 2
    Other: int = 99

class RegistryKeyActivity(Discovery):
    """
    Registry Key Activity events report when a process performs an action on a Windows registry key.
    """

    class_uid: int = 201001 # The unique identifier of a class.
    class_name: str = 'Registry Key Activity' # The event class name.
    category_uid: int = 1 # The category unique identifier of the event.
    category_name: str = 'System Activity' # The event category name.
    type_uid: int # The event/finding type ID.
    type_name: str | None = None # The event/finding type name.
    activity_id: ActivityId # The normalized identifier of the activity that triggered the event.
    activity_name: str | None = None # The event activity name.
    actor: Actor # The actor that performed the activity on the reg_key object.
    command_uid: str # The unique identifier of the remediation command that pertains to this event.
    device: Device # An addressable device, computer system or host.
    metadata: Metadata # The metadata associated with the event or a finding.
    reg_key: RegistryKey # Describes details about the registry key that triggered the detection.
    time: datetime # The normalized event occurrence time or the finding creation time.
    severity_id: SeverityId # The normalized identifier of the event/finding severity.
    severity: str | None = None # The event/finding severity, normalized to the caption of the severity_id value.

    # Optional:
    access_mask: Optional[int] = None # The access mask in a platform-native format.
    count: Optional[int] = None # The number of times that events in the same logical group occurred during the event Start Time to End Time period.
    create_mask: Optional[str] = None # The original Windows mask that is required to create the object.
    duration: Optional[int] = None # The event duration or aggregate time, the amount of time the event covers from start_time to end_time in milliseconds.
    end_time: Optional[datetime] = None # The end time of a time period, or the time of the most recent event included in the aggregate event.
    enrichments: Optional[list] = None # The additional information from an external data source, which is associated with the event or a finding.
    message: Optional[str] = None # The description of the event/finding, as defined
    observables: Optional[list[Observable]] = None # The observables associated with the event or a finding.
    open_mask: Optional[int] = None # The Windows options needed to open a registry key.
    prev_reg_key: Optional[RegistryKey] = None # The registry key before the mutation.
    raw_data: Optional[str] = None # The raw event/finding data as received from the source.
    start_time: Optional[datetime] = None # The start time of a time period, or the time of the least recent event included in the aggregate event.
    status_id: Optional[StatusId] = None # The normalized identifier of the event status.
    status: Optional[str] = None # The event status, normalized to the caption of the status_id value.
    status_code: Optional[str] = None # The event status code, as reported by the event source.
    status_detail: Optional[str] = None # The status detail contains additional information about the event/finding outcome.
    timezone_offset: Optional[int] = None # The number of minutes that the reported event time is ahead or behind UTC.
    unmapped: Optional[dict] = None # The attributes that are not mapped to the event schema.
