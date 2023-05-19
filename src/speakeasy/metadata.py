"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from speakeasy.models import operations, shared
from typing import Optional

class Metadata:
    r"""REST APIs for managing Version Metadata entities"""
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests_http.Session, security_client: requests_http.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        
    
    def delete_version_metadata(self, request: operations.DeleteVersionMetadataRequest) -> operations.DeleteVersionMetadataResponse:
        r"""Delete metadata for a particular apiID and versionID."""
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteVersionMetadataRequest, base_url, '/v1/apis/{apiID}/version/{versionID}/metadata/{metaKey}/{metaValue}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteVersionMetadataResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Error])
                res.error = out

        return res

    
    def get_version_metadata(self, request: operations.GetVersionMetadataRequest) -> operations.GetVersionMetadataResponse:
        r"""Get all metadata for a particular apiID and versionID."""
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetVersionMetadataRequest, base_url, '/v1/apis/{apiID}/version/{versionID}/metadata', request)
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetVersionMetadataResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.VersionMetadata]])
                res.version_metadata = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Error])
                res.error = out

        return res

    
    def insert_version_metadata(self, request: operations.InsertVersionMetadataRequest) -> operations.InsertVersionMetadataResponse:
        r"""Insert metadata for a particular apiID and versionID."""
        base_url = self._server_url
        
        url = utils.generate_url(operations.InsertVersionMetadataRequest, base_url, '/v1/apis/{apiID}/version/{versionID}/metadata', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "version_metadata_input", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.InsertVersionMetadataResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.VersionMetadata])
                res.version_metadata = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Error])
                res.error = out

        return res

    