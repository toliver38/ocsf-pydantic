from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class RegistryValue(BaseModel):
    """
    The registry value object describes a Windows registry value.
    """

    data: Optional[dict] = Field(None, description="The data of the registry value.")
    is_default: Optional[bool] = Field(None, description="The indication of whether the value is from a default value name. For example, the value name could be missing.")
    modified_time: Optional[datetime] = Field(None, description="The time when the registry value was last modified.")
    name: str = Field(..., description="The name of the registry value.")
    path: str = Field(..., description="The full path to the registry key, where the value is located.")
    is_system: Optional[bool] = Field(None, description="The indication of whether the object is part of the operating system.")
    type: Optional[str] = Field(None, description="A string representation of the value type as specified in Registry Value Types.")
    type_id: Optional[int] = Field(None, description="The value type ID. 0: Unknown, 1: REG_BINARY, 2: REG_DWORD, 3: REG_DWORD_BIG_ENDIAN, 4: REG_EXPAND_SZ, 5: REG_LINK, 6: REG_MULTI_SZ, 7: REG_NONE, 8: REG_QWORD, 9: REG_QWORD_LITTLE_ENDIAN, 10: REG_SZ, 99: Other")

    class Config:
        schema_extra = {
            "example": {
                "data": {"example_key": "example_value"},
                "is_default": False,
                "modified_time": "2023-10-01T12:00:00Z",
                "name": "ExampleName",
                "path": "HKEY_LOCAL_MACHINE\\Software\\Example",
                "is_system": True,
                "type": "REG_SZ",
                "type_id": 10
            }
        }