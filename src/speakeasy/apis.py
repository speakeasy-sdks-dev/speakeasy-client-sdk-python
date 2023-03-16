import requests as requests_http
from . import utils
from speakeasy.models import operations, shared
from typing import Optional

class Apis:
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
        
    def delete_api(self, request: operations.DeleteAPIRequest) -> operations.DeleteAPIResponse:
        r"""Delete an Api.
        Delete a particular version of an Api. The will also delete all associated ApiEndpoints, Metadata, Schemas & Request Logs (if using a Postgres datastore).
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteAPIRequest, base_url, '/v1/apis/{apiID}/version/{versionID}', request)
        
        headers = {}
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteAPIResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Error])
                res.error = out

        return res

    def generate_open_api_spec(self, request: operations.GenerateOpenAPISpecRequest) -> operations.GenerateOpenAPISpecResponse:
        r"""Generate an OpenAPI specification for a particular Api.
        This endpoint will generate any missing operations in any registered OpenAPI document if the operation does not already exist in the document.
        Returns the original document and the newly generated document allowing a diff to be performed to see what has changed.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GenerateOpenAPISpecRequest, base_url, '/v1/apis/{apiID}/version/{versionID}/generate/openapi', request)
        
        headers = {}
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GenerateOpenAPISpecResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.GenerateOpenAPISpecDiff])
                res.generate_open_api_spec_diff = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Error])
                res.error = out

        return res

    def generate_postman_collection(self, request: operations.GeneratePostmanCollectionRequest) -> operations.GeneratePostmanCollectionResponse:
        r"""Generate a Postman collection for a particular Api.
        Generates a postman collection containing all endpoints for a particular API. Includes variables produced for any path/query/header parameters included in the OpenAPI document.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GeneratePostmanCollectionRequest, base_url, '/v1/apis/{apiID}/version/{versionID}/generate/postman', request)
        
        headers = {}
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GeneratePostmanCollectionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/octet-stream'):
                res.postman_collection = http_res.content
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Error])
                res.error = out

        return res

    def get_all_api_versions(self, request: operations.GetAllAPIVersionsRequest) -> operations.GetAllAPIVersionsResponse:
        r"""Get all Api versions for a particular ApiEndpoint.
        Get all Api versions for a particular ApiEndpoint.
        Supports filtering the versions based on metadata attributes.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetAllAPIVersionsRequest, base_url, '/v1/apis/{apiID}', request)
        
        headers = {}
        query_params = utils.get_query_params(operations.GetAllAPIVersionsRequest, request)
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAllAPIVersionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.API]])
                res.apis = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Error])
                res.error = out

        return res

    def get_apis(self, request: operations.GetApisRequest) -> operations.GetApisResponse:
        r"""Get a list of Apis for a given workspace
        Get a list of all Apis and their versions for a given workspace.
        Supports filtering the APIs based on metadata attributes.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/apis'
        
        headers = {}
        query_params = utils.get_query_params(operations.GetApisRequest, request)
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetApisResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.API]])
                res.apis = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Error])
                res.error = out

        return res

    def upsert_api(self, request: operations.UpsertAPIRequest) -> operations.UpsertAPIResponse:
        r"""Upsert an Api
        Upsert an Api. If the Api does not exist, it will be created.
        If the Api exists, it will be updated.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.UpsertAPIRequest, base_url, '/v1/apis/{apiID}', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "api_input", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpsertAPIResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.API])
                res.api = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Error])
                res.error = out

        return res

    