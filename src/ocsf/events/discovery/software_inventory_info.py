from datetime import datetime
from pydantic import BaseModel
from ocsf.objects.device import Device
from ocsf.objects.metadata import Metadata
from ocsf.objects.package import SoftwarePackage
from ocsf.objects.actor import Actor
from ocsf.objects.observable import Observable
from ocsf.objects.product import Product
from ocsf.events.discovery.discovery import Discovery
from enum import Enum

class ActivityId(Enum):
    Unknown: int = 0
    Log: int = 1
    Collect: int = 2
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

class SoftwareInventoryInfo(Discovery):
    """
    Software Inventory Info events report device software inventory data that is either logged or proactively collected.
    """
    class_uid: int = 5020 # The unique identifier of a class.
    class_name: str = 'Software Inventory Info' # The event class name.
    category_uid: int = 5 # The category unique identifier of the event.
    category_name: str = 'Discovery' # The event category name.
    type_uid: int # The event/finding type ID.
    type_name: str | None = None # The event/finding type name.
    activity_id: ActivityId # The normalized identifier of the activity that triggered the event.
    activity_name: str | None = None # The event activity name.
    device: Device # The device that is being discovered by an inventory process.
    metadata: Metadata # The metadata associated with the event or a finding.
    package: SoftwarePackage # The device software that is being discovered by an inventory process.
    time: datetime # The normalized event occurrence time or the finding creation time.

    # Optional:
    actor: Actor | None = None # The actor object describes details about the user/role/process that was the source of the activity.
    count: int | None = None # The number of times that events in the same logical group occurred during the event Start Time to End Time period.
    duration: int | None = None # The event duration or aggregate time, the amount of time the event covers from start_time to end_time in milliseconds.
    end_time: datetime | None = None # The end time of a time period, or the time of the most recent event included in the aggregate event.
    enrichments: list | None = None # The additional information from an external data source, which is associated with the event or a finding.
    message: str | None = None # The description of the event/finding, as defined by the source.
    observables: list[Observable] | None = None # The observables associated with the event or a finding.
    product: Product | None = None # Additional product attributes that have been discovered or enriched from a catalog or other external source.
    raw_data: str | None = None # The raw event/finding data as received from the source.
    severity_id: SeverityId # The normalized identifier of the event/finding severity.
    severity: str | None = None # The event/finding severity, normalized to the caption of the severity_id value.
    start_time: datetime | None = None # The start time of a time period, or the time of the least recent event included in the aggregate event.
    status_id: StatusId | None = None # The normalized identifier of the event status.
    status: str | None = None # The event status, normalized to the caption of the status_id value.
    status_code: str | None = None # The event status code, as reported by the event source.
    status_detail: str | None = None # The status detail contains additional information about the event/finding outcome.
    timezone_offset: int | None = None # The number of minutes that the reported event time is ahead or behind UTC.
    unmapped: dict | None = None # The attributes that are not mapped to the event schema.
