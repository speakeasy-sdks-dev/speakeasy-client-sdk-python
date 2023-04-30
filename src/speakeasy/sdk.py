"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from .apiendpoints import APIEndpoints
from .apis import Apis
from .embeds import Embeds
from .metadata import Metadata
from .plugins import Plugins
from .requests import Requests
from .schemas import Schemas
from speakeasy.models import operations, shared
from typing import Optional

SERVER_PROD = "prod"
SERVERS = {
	SERVER_PROD: "https://api.prod.speakeasyapi.dev",
}
"""Contains the list of servers available to the SDK"""

class Speakeasy:
    r"""The Speakeasy API allows teams to manage common operations with their APIs
    https://docs.speakeasyapi.dev - The Speakeasy Platform Documentation
    """
    api_endpoints: APIEndpoints
    r"""REST APIs for managing ApiEndpoint entities"""
    apis: Apis
    r"""REST APIs for managing Api entities"""
    embeds: Embeds
    r"""REST APIs for managing embeds"""
    metadata: Metadata
    r"""REST APIs for managing Version Metadata entities"""
    plugins: Plugins
    r"""REST APIs for managing and running plugins"""
    requests: Requests
    r"""REST APIs for retrieving request information"""
    schemas: Schemas
    r"""REST APIs for managing Schema entities"""

    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str = SERVERS[SERVER_PROD]
    _language: str = "python"
    _sdk_version: str = "1.21.2"
    _gen_version: str = "2.23.4"

    def __init__(self,
                 security: shared.Security = None,
                 server: str = None,
                 server_url: str = None,
                 url_params: dict[str, str] = None,
                 client: requests_http.Session = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param security: The security details required for authentication
        :type security: shared.Security
        :param server: The server by name to use for all operations
        :type server: str
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session        
        """
        self._client = requests_http.Session()
        
        
        if server is not None:
            server_url = SERVERS[server]
        
        if server_url is not None:
            if url_params is not None:
                self._server_url = utils.template_url(server_url, url_params)
            else:
                self._server_url = server_url

        if client is not None:
            self._client = client
        
        self._security_client = utils.configure_security_client(self._client, security)
        

        self._init_sdks()
    
    def _init_sdks(self):
        self.api_endpoints = APIEndpoints(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.apis = Apis(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.embeds = Embeds(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.metadata = Metadata(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.plugins = Plugins(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.requests = Requests(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.schemas = Schemas(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
    def validate_api_key(self) -> operations.ValidateAPIKeyResponse:
        r"""Validate the current api key."""
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/auth/validate'
        
        headers = {}
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ValidateAPIKeyResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Error])
                res.error = out

        return res

    