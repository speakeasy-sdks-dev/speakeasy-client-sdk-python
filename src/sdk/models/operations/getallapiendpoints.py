from dataclasses import dataclass, field
from typing import List,Optional
from sdk.models import shared


@dataclass
class GetAllAPIEndpointsPathParams:
    api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    

@dataclass
class GetAllAPIEndpointsRequest:
    path_params: GetAllAPIEndpointsPathParams = field(default=None)
    

@dataclass
class GetAllAPIEndpointsResponses:
    api_endpoints: Optional[List[shared.APIEndpoint]] = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    

@dataclass
class GetAllAPIEndpointsResponse:
    content_type: str = field(default=None)
    responses: dict[int, dict[str, GetAllAPIEndpointsResponses]] = field(default=None)
    status_code: int = field(default=None)
    