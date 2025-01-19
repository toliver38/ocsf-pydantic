from datetime import datetime
from ocsf.events.system import SystemActivity
from typing import Optional
from enum import Enum
from ocsf.objects.actor import Actor
from ocsf.objects.device import Device
from ocsf.objects.metadata import Metadata
from ocsf.objects.observable import Observable
from extensions.windows.objects.windows_resource import WindowsResource

class ActivityId(Enum):
    Unknown: int = 0
    Access: int = 1
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

class WindowsResourceActivity(SystemActivity):
    """
    Windows Resource Activity events report when a process accesses a Windows managed resource object, successful or otherwise.
    """

    class_uid: int = 201003 # The unique identifier of a class.
    class_name: str = 'Windows Resource Activity' # The event class name.
    category_uid: int = 1 # The category unique identifier of the event.
    category_name: str = 'System Activity' # The event category name.
    type_uid: int # The event/finding type ID.
    type_name: str | None = None # The event/finding type name.
    activity_id: ActivityId # The normalized identifier of the activity that triggered the event.
    activity_name: str | None = None # The event activity name.
    actor: Actor # The actor object describes details about the user/role/process that was the source of the activity.
    device: Device # An addressable device, computer system or host.
    metadata: Metadata # The metadata associated with the event or a finding.
    win_resource: WindowsResource # The Windows resource object that was accessed, such as a mutant or timer.
    time: datetime # The normalized event occurrence time or the finding creation time.
    severity_id: SeverityId # The normalized identifier of the event/finding severity.
    severity: str | None = None # The event/finding severity, normalized to the caption of the severity_id value.

    # Optional:
    count: Optional[int] = None # The number of times that events in the same logical group occurred during the event Start Time to End Time period.
    duration: Optional[int] = None # The event duration or aggregate time, the amount of time the event covers from start_time to end_time in milliseconds.
    end_time: Optional[datetime] = None # The end time of a time period, or the time of the most recent event included in the aggregate event.
    enrichments: Optional[list] = None # The additional information from an external data source, which is associated with the event or a finding.
    message: Optional[str] = None # The description of the event/finding, as defined by the source.
    observables: Optional[list[Observable]] = None # The observables associated with the event or a finding.
    raw_data: Optional[str] = None # The raw event/finding data as received from the source.
    start_time: Optional[datetime] = None # The start time of a time period, or the time of the least recent event included in the aggregate event.
    status_id: Optional[StatusId] = None # The normalized identifier of the event status.
    status: Optional[str] = None # The event status, normalized to the caption of the status_id value.
    status_code: Optional[str] = None # The event status code, as reported by the event source.
    status_detail: Optional[str] = None # The status detail contains additional information about the event/finding outcome.
    timezone_offset: Optional[int] = None # The number of minutes that the reported event time is ahead or behind UTC.
    unmapped: Optional[dict] = None # The attributes that are not mapped to the event schema.
