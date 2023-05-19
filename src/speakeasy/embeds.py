"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from speakeasy.models import operations, shared
from typing import Optional

class Embeds:
    r"""REST APIs for managing embeds"""
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
        
    
    def get_embed_access_token(self, request: operations.GetEmbedAccessTokenRequest) -> operations.GetEmbedAccessTokenResponse:
        r"""Get an embed access token for the current workspace.
        Returns an embed access token for the current workspace. This can be used to authenticate access to externally embedded content.
        Filters can be applied allowing views to be filtered to things like particular customerIds.
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/workspace/embed-access-token'
        headers = {}
        query_params = utils.get_query_params(operations.GetEmbedAccessTokenRequest, request)
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetEmbedAccessTokenResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.EmbedAccessTokenResponse])
                res.embed_access_token_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Error])
                res.error = out

        return res

    
    def get_valid_embed_access_tokens(self) -> operations.GetValidEmbedAccessTokensResponse:
        r"""Get all valid embed access tokens for the current workspace."""
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/workspace/embed-access-tokens/valid'
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetValidEmbedAccessTokensResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.EmbedToken]])
                res.embed_tokens = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Error])
                res.error = out

        return res

    
    def revoke_embed_access_token(self, request: operations.RevokeEmbedAccessTokenRequest) -> operations.RevokeEmbedAccessTokenResponse:
        r"""Revoke an embed access EmbedToken."""
        base_url = self._server_url
        
        url = utils.generate_url(operations.RevokeEmbedAccessTokenRequest, base_url, '/v1/workspace/embed-access-tokens/{tokenID}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.RevokeEmbedAccessTokenResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Error])
                res.error = out

        return res

    