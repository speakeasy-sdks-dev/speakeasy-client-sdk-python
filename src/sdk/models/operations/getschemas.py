from dataclasses import dataclass, field
from typing import List,Optional
from sdk.models import shared


@dataclass
class GetSchemasPathParams:
    api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = field(default=None, metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class GetSchemasRequest:
    path_params: GetSchemasPathParams = field(default=None)
    

@dataclass
class GetSchemasResponses:
    error: Optional[shared.Error] = field(default=None)
    schemata: Optional[List[shared.Schema]] = field(default=None)
    

@dataclass
class GetSchemasResponse:
    content_type: str = field(default=None)
    responses: dict[int, dict[str, GetSchemasResponses]] = field(default=None)
    status_code: int = field(default=None)
    