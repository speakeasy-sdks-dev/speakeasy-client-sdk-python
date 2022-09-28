from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared


@dataclass
class DeleteAPIV1PathParams:
    api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = field(default=None, metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class DeleteAPIV1Request:
    path_params: DeleteAPIV1PathParams = field(default=None)
    

@dataclass
class DeleteAPIV1Responses:
    error: Optional[shared.Error] = field(default=None)
    

@dataclass
class DeleteAPIV1Response:
    content_type: str = field(default=None)
    responses: dict[int, dict[str, DeleteAPIV1Responses]] = field(default=None)
    status_code: int = field(default=None)
    
