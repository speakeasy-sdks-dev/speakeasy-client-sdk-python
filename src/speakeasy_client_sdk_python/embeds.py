"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .basesdk import BaseSDK
from speakeasy_client_sdk_python._hooks import HookContext
from speakeasy_client_sdk_python.models import errors, operations, shared
from speakeasy_client_sdk_python.types import BaseModel
import speakeasy_client_sdk_python.utils as utils
from typing import List, Optional, Union

class Embeds(BaseSDK):
    r"""REST APIs for managing embeds"""
    
    
    def get_embed_access_token(
        self, *,
        request: Optional[Union[operations.GetEmbedAccessTokenRequest, operations.GetEmbedAccessTokenRequestTypedDict]] = None,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> operations.GetEmbedAccessTokenResponse:
        r"""Get an embed access token for the current workspace.

        Returns an embed access token for the current workspace. This can be used to authenticate access to externally embedded content.
        Filters can be applied allowing views to be filtered to things like particular customerIds.

        :param request: The request object to send.
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.GetEmbedAccessTokenRequest)
        
        req = self.build_request(
            method="GET",
            path="/v1/workspace/embed-access-token",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_config=timeout_config,
        )
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="getEmbedAccessToken", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
        )
        
        res = operations.GetEmbedAccessTokenResponse(status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        
        if utils.match_response(http_res, "200", "application/json"):
            res.embed_access_token_response = utils.unmarshal_json(http_res.text, Optional[shared.EmbedAccessTokenResponse])
        elif utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        elif utils.match_response(http_res, "default", "application/json"):
            res.error = utils.unmarshal_json(http_res.text, Optional[errors.Error])
        else:
            content_type = http_res.headers.get("Content-Type")
            raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

        return res
    
    
    async def get_embed_access_token_async(
        self, *,
        request: Optional[Union[operations.GetEmbedAccessTokenRequest, operations.GetEmbedAccessTokenRequestTypedDict]] = None,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> operations.GetEmbedAccessTokenResponse:
        r"""Get an embed access token for the current workspace.

        Returns an embed access token for the current workspace. This can be used to authenticate access to externally embedded content.
        Filters can be applied allowing views to be filtered to things like particular customerIds.

        :param request: The request object to send.
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.GetEmbedAccessTokenRequest)
        
        req = self.build_request(
            method="GET",
            path="/v1/workspace/embed-access-token",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_config=timeout_config,
        )
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="getEmbedAccessToken", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
        )
        
        res = operations.GetEmbedAccessTokenResponse(status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        
        if utils.match_response(http_res, "200", "application/json"):
            res.embed_access_token_response = utils.unmarshal_json(http_res.text, Optional[shared.EmbedAccessTokenResponse])
        elif utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        elif utils.match_response(http_res, "default", "application/json"):
            res.error = utils.unmarshal_json(http_res.text, Optional[errors.Error])
        else:
            content_type = http_res.headers.get("Content-Type")
            raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

        return res
    
    
    def get_valid_embed_access_tokens(
        self, *,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> operations.GetValidEmbedAccessTokensResponse:
        r"""Get all valid embed access tokens for the current workspace.

        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        req = self.build_request(
            method="GET",
            path="/v1/workspace/embed-access-tokens/valid",
            base_url=base_url,
            url_variables=url_variables,
            request=None,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_config=timeout_config,
        )
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="getValidEmbedAccessTokens", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
        )
        
        res = operations.GetValidEmbedAccessTokensResponse(status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        
        if utils.match_response(http_res, "200", "application/json"):
            res.embed_tokens = utils.unmarshal_json(http_res.text, Optional[List[shared.EmbedToken]])
        elif utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        elif utils.match_response(http_res, "default", "application/json"):
            res.error = utils.unmarshal_json(http_res.text, Optional[errors.Error])
        else:
            content_type = http_res.headers.get("Content-Type")
            raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

        return res
    
    
    async def get_valid_embed_access_tokens_async(
        self, *,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> operations.GetValidEmbedAccessTokensResponse:
        r"""Get all valid embed access tokens for the current workspace.

        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        req = self.build_request(
            method="GET",
            path="/v1/workspace/embed-access-tokens/valid",
            base_url=base_url,
            url_variables=url_variables,
            request=None,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_config=timeout_config,
        )
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="getValidEmbedAccessTokens", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
        )
        
        res = operations.GetValidEmbedAccessTokensResponse(status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        
        if utils.match_response(http_res, "200", "application/json"):
            res.embed_tokens = utils.unmarshal_json(http_res.text, Optional[List[shared.EmbedToken]])
        elif utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        elif utils.match_response(http_res, "default", "application/json"):
            res.error = utils.unmarshal_json(http_res.text, Optional[errors.Error])
        else:
            content_type = http_res.headers.get("Content-Type")
            raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

        return res
    
    
    def revoke_embed_access_token(
        self, *,
        request: Union[operations.RevokeEmbedAccessTokenRequest, operations.RevokeEmbedAccessTokenRequestTypedDict],
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> operations.RevokeEmbedAccessTokenResponse:
        r"""Revoke an embed access EmbedToken.

        :param request: The request object to send.
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.RevokeEmbedAccessTokenRequest)
        
        req = self.build_request(
            method="DELETE",
            path="/v1/workspace/embed-access-tokens/{tokenID}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_config=timeout_config,
        )
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="revokeEmbedAccessToken", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
        )
        
        res = operations.RevokeEmbedAccessTokenResponse(status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        
        if utils.match_response(http_res, "200", "*"):
            pass
        elif utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        elif utils.match_response(http_res, "default", "application/json"):
            res.error = utils.unmarshal_json(http_res.text, Optional[errors.Error])
        else:
            content_type = http_res.headers.get("Content-Type")
            raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

        return res
    
    
    async def revoke_embed_access_token_async(
        self, *,
        request: Union[operations.RevokeEmbedAccessTokenRequest, operations.RevokeEmbedAccessTokenRequestTypedDict],
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> operations.RevokeEmbedAccessTokenResponse:
        r"""Revoke an embed access EmbedToken.

        :param request: The request object to send.
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.RevokeEmbedAccessTokenRequest)
        
        req = self.build_request(
            method="DELETE",
            path="/v1/workspace/embed-access-tokens/{tokenID}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_config=timeout_config,
        )
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="revokeEmbedAccessToken", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
        )
        
        res = operations.RevokeEmbedAccessTokenResponse(status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        
        if utils.match_response(http_res, "200", "*"):
            pass
        elif utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        elif utils.match_response(http_res, "default", "application/json"):
            res.error = utils.unmarshal_json(http_res.text, Optional[errors.Error])
        else:
            content_type = http_res.headers.get("Content-Type")
            raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

        return res
    