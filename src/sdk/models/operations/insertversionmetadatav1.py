from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared


@dataclass
class InsertVersionMetadataV1PathParams:
    api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = field(default=None, metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class InsertVersionMetadataV1Request:
    path_params: InsertVersionMetadataV1PathParams = field(default=None)
    request: shared.VersionMetadata = field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass
class InsertVersionMetadataV1Responses:
    error: Optional[shared.Error] = field(default=None)
    raw_response: bytes = field(default=None)
    version_metadata: Optional[shared.VersionMetadata] = field(default=None)
    

@dataclass
class InsertVersionMetadataV1Response:
    content_type: str = field(default=None)
    responses: dict[int, dict[str, InsertVersionMetadataV1Responses]] = field(default=None)
    status_code: int = field(default=None)
    
