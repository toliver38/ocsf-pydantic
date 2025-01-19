from pydantic import BaseModel
from typing import Optional
from ocsf.objects.d3fend_tactic import MitreD3fendTactic
from ocsf.objects.d3fend_technique import MitreD3fendTechnique

class MitreD3fend(BaseModel):
    """
    The MITRE D3FEND™ object describes the tactic, technique & sub-technique associated with a countermeasure as defined in D3FEND™ Matrix.
    """

    d3f_tactic: Optional[MitreD3fendTactic] = None # The Tactic object describes the tactic ID and/or name that is associated with a countermeasure, as defined by D3FEND™ Matrix.
    d3f_technique: Optional[MitreD3fendTechnique] = None # The Defend Technique object describes the technique ID and/or name associated with a countermeasure, as defined by D3FEND™ Matrix.
    version: Optional[str] = None # The D3FEND™ Matrix version.
