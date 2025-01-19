from pydantic import BaseModel
from typing import Optional

class MitreD3fendTechnique(BaseModel):
    """
    The MITRE D3FEND™ Technique object describes the leaf defensive technique ID and/or name associated to a countermeasure, as defined by D3FEND™ Matrix.
    """

    name: Optional[str] = None # The name of the defensive technique, as defined by D3FEND™ Matrix. For example: IO Port Restriction.
    src_url: Optional[str] = None # The versioned permalink of the defensive technique, as defined by D3FEND™ Matrix. For example: https://d3fend.mitre.org/technique/d3f:IOPortRestriction/.
    uid: Optional[str] = None # The unique identifier of the defensive technique, as defined by D3FEND™ Matrix. For example: D3-IOPR.
