from pydantic import BaseModel
from typing import Optional
from enum import Enum

class TimeSpanTypeId(Enum):
    Unknown: int = 0
    Milliseconds: int = 1
    Seconds: int = 2
    Minutes: int = 3
    Hours: int = 4
    Days: int = 5
    Weeks: int = 6
    Months: int = 7
    Years: int = 8
    Other: int = 99

class TimeSpan(BaseModel):
    """
    The Time Span object represents different time period durations. If a timespan is fractional, i.e. crosses one period, e.g. a week and 3 days, more than one may be populated since each member is of integral type. In that case type_id if present should be set to Other.
    """

    duration_days: Optional[int] = None # The duration of the time span in days.
    duration_hours: Optional[int] = None # The duration of the time span in hours.
    duration: Optional[int] = None # The duration of the time span in milliseconds.
    duration_mins: Optional[int] = None # The duration of the time span in minutes.
    duration_months: Optional[int] = None # The duration of the time span in months.
    duration_secs: Optional[int] = None # The duration of the time span in seconds.
    duration_weeks: Optional[int] = None # The duration of the time span in weeks.
    duration_years: Optional[int] = None # The duration of the time span in years.
    type: Optional[str] = None # The type of time span duration the object represents.
    type_id: Optional[TimeSpanTypeId] = None # The normalized identifier for the time span duration type.
