from pydantic import BaseModel
from typing import Optional

class MitreD3fendTactic(BaseModel):
    """
    The MITRE D3FEND™ Tactic object describes the tactic ID and/or name that is associated to an attack, as defined by D3FEND™ Matrix.
    """

    name: Optional[str] = None # The tactic name that is associated with the defensive technique, as defined by D3FEND™ Matrix. For example: Isolate.
    src_url: Optional[str] = None # The versioned permalink of the defensive tactic, as defined by D3FEND™ Matrix. For example: https://d3fend.mitre.org/tactic/d3f:Isolate/.
    uid: Optional[str] = None # The unique identifier of the entity.
