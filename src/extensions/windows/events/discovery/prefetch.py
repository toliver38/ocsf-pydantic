from datetime import datetime
from enum import Enum
from ocsf.objects.metadata import Metadata
from ocsf.events.discovery import Discovery
from ocsf.objects.observable import Observable
from ocsf.objects.query_info import QueryInformation
from typing import Optional

class ActivityId(Enum):
    Unknown: int = 0
    Query: int = 1
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

class QueryResultId(Enum):
    Unknown: int = 0
    Exists: int = 1
    Partial: int = 2
    DoesNotExist: int = 3
    Error: int = 4
    Unsupported: int = 5
    Other: int = 99

class PrefetchQuery(Discovery):
    """
    Prefetch Query events report information about Windows prefetch files.
    """

    class_uid: int = 205019 # The unique identifier of a class.
    class_name: str = 'Prefetch Query' # The event class name.
    category_uid: int = 5 # The category unique identifier of the event.
    category_name: str = 'Discovery' # The event category name.
    type_uid: int # The event/finding type ID.
    type_name: str | None = None # The event/finding type name.
    activity_id: ActivityId # The normalized identifier of the activity that triggered the event.
    activity_name: str | None = None # The event activity name.
    metadata: Metadata # The metadata associated with the event or a finding.
    name: str # The name of the prefetch file that is the target of the query.
    query_result_id: QueryResultId # The normalized identifier of the query result.
    time: datetime # The normalized event occurrence time or the finding creation time.
    severity_id: SeverityId # The normalized identifier of the event/finding severity.
    severity: str | None = None # The event/finding severity, normalized to the caption of the severity_id value.

    # Optional:
    count: Optional[int] = None # The number of times that events in the same logical group occurred during the event Start Time to End Time period.
    duration: Optional[int] = None # The event duration or aggregate time, the amount of time the event covers from start_time to end_time in milliseconds.
    end_time: Optional[datetime] = None # The end time of a time period, or the time of the most recent event included in the aggregate event.
    enrichments: Optional[list] = None # The additional information from an external data source, which is associated with the event or a finding.
    last_run_time: Optional[datetime] = None # The prefetch file last run time.
    message: Optional[str] = None # The description of the event/finding, as defined by the source.
    observables: Optional[list[Observable]] = None # The observables associated with the event or a finding.
    query_info: Optional[QueryInformation] = None # The search details associated with the query request.
    query_result: Optional[str] = None # The result of the query.
    raw_data: Optional[str] = None # The raw event/finding data as received from the source.
    run_count: Optional[int] = None # The prefetch file run count.
    start_time: Optional[datetime] = None # The start time of a time period, or the time of the least recent event included in the aggregate event.
    status_id: Optional[StatusId] = None # The normalized identifier of the event status.
    status: Optional[str] = None # The event status, normalized to the caption of the status_id value.
    status_code: Optional[str] = None # The event status code, as reported by the event source.
    status_detail: Optional[str] = None # The status detail contains additional information about the event/finding outcome.
    timezone_offset: Optional[int] = None # The number of minutes that the reported event time is ahead or behind UTC.
    unmapped: Optional[dict] = None # The attributes that are not mapped to the event schema.
