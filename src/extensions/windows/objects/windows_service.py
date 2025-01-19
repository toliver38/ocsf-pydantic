from pydantic import BaseModel
from typing import Optional
from enum import Enum

class ServiceCategoryId(Enum):
    Unknown: int = 0
    KernelMode: int = 1
    UserMode: int = 2
    Other: int = 99

class ServiceErrorControlId(Enum):
    Unknown: int = 0
    Ignore: int = 1
    Normal: int = 2
    Severe: int = 3
    Critical: int = 4
    Other: int = 99

class ServiceStartTypeId(Enum):
    Unknown: int = 0
    Boot: int = 1
    System: int = 2
    Auto: int = 3
    Demand: int = 4
    Disabled: int = 5
    Other: int = 99

class ServiceTypeId(Enum):
    Unknown: int = 0
    KernelDriver: int = 1
    FileSystemDriver: int = 2
    OwnProcess: int = 3
    ShareProcess: int = 4
    Other: int = 99

class WindowsService(BaseModel):
    """
    The Windows Service object describes a Windows service.
    """

    name: str # The unique name of the service.
    cmd_line: Optional[str] = None # The full command line used to launch the service.
    labels: Optional[list[str]] = None # The list of labels associated with the service.
    load_order_group: Optional[str] = None # The name of the load ordering group of which this service is a member.
    service_category_id: Optional[ServiceCategoryId] = None # The normalized identifier of the service category.
    service_category: Optional[str] = None # The service category, normalized to the caption of the service_category_id value.
    service_dependencies: Optional[list[str]] = None # The names of other services upon which this service has a dependency.
    service_error_control_id: Optional[ServiceErrorControlId] = None # The normalized identifier of the service error control.
    service_error_control: Optional[str] = None # The service error control, normalized to the caption of the service_error_control_id value.
    service_start_name: Optional[str] = None # For a user mode service, this attribute represents the name of the account under which the service is run. For a kernel mode driver, this attribute represents the object name used to load the driver.
    service_start_type_id: Optional[ServiceStartTypeId] = None # The normalized identifier of the service start type.
    service_start_type: Optional[str] = None # The service start type, normalized to the caption of the service_start_type_id value.
    service_type_id: Optional[ServiceTypeId] = None # The normalized identifier of the service type.
    service_type: Optional[str] = None # The service type, normalized to the caption of the service_type_id value.
    uid: Optional[str] = None # The unique identifier of the service.
    version: Optional[str] = None # The version of the service.
