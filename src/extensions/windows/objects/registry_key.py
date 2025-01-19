from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class RegistryKey(BaseModel):
    """
    The registry key object describes a Windows registry key.
    """
    modified_time: Optional[datetime] = None
    path: str
    security_descriptor: Optional[str] = None
    is_system: Optional[bool] = None