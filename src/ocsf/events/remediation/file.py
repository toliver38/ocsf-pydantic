from datetime import datetime
from ocsf.objects.metadata import Metadata
from ocsf.objects.observable import Observable
from ocsf.objects.remediation import Remediation
from ocsf.events.remediation.remediation import RemediationActivity
from ocsf.objects.scan import Scan
from ocsf.objects.file import File
from ocsf.events.base import BaseEvent
from enum import Enum

class ActivityId(Enum):
    Unknown: int = 0
    Isolate: int = 1
    Evict: int = 2
    Restore: int = 3
    Harden: int = 4
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
    DoesNotExist: int = 3
    Partial: int = 4
    Unsupported: int = 5
    Error: int = 6
    Other: int = 99

class FileRemediationActivity(RemediationActivity):
    """
    File Remediation Activity events report on attempts at remediating files.
    """

    class_uid: int = 7002 # The unique identifier of a class.
    class_name: str = 'File Remediation Activity' # The event class name.
    category_uid: int = 7 # The category unique identifier of the event.
    category_name: str = 'Remediation' # The event category name.
    type_uid: int # The event/finding type ID.
    type_name: str | None = None # The event/finding type name.
    activity_id: ActivityId # Matches the MITRE D3FEND™ Tactic.
    activity_name: str | None = None # The event activity name.
    command_uid: str # The unique identifier of the remediation command that pertains to this event.
    metadata: Metadata # The metadata associated with the event or a finding.
    time: datetime # The normalized event occurrence time or the finding creation time.
    severity_id: SeverityId # The normalized identifier of the event/finding severity.
    severity: str | None = None # The event/finding severity, normalized to the caption of the severity_id value.
    file: File # The file that pertains to the remediation event.

    # Optional:
    count: int | None = None # The number of times that events in the same logical group occurred during the event Start Time to End Time period.
    countermeasures: list | None = None # The MITRE DEFEND™ Matrix Countermeasures associated with a remediation.
    duration: int | None = None # The event duration or aggregate time, the amount of time the event covers from start_time to end_time in milliseconds.
    end_time: datetime | None = None # The end time of a time period, or the time of the most recent event included in the aggregate event.
    enrichments: list | None = None # The additional information from an external data source, which is associated with the event or a finding.
    message: str | None = None # The description of the event/finding, as defined by the source.
    observables: list[Observable] | None = None # The observables associated with the event or a finding.
    raw_data: str | None = None # The raw event/finding data as received from the source.
    remediation: Remediation | None = None # Describes the recommended remediation steps to address identified issue(s).
    scan: Scan | None = None # The remediation scan that pertains to this event.
    start_time: datetime | None = None # The start time of a time period, or the time of the least recent event included in the aggregate event.
    status_id: StatusId | None = None # The normalized identifier of the event status.
    status: str | None = None # The event status, normalized to the caption of the status_id value.
    status_code: str | None = None # The event status code, as reported by the event source.
    status_detail: str | None = None # The status detail contains additional information about the event/finding outcome.
    timezone_offset: int | None = None # The number of minutes that the reported event time is ahead or behind UTC.
    unmapped: dict | None = None # The attributes that are not mapped to the event schema.
