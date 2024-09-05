"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from enum import Enum
from speakeasy_client_sdk_python import utils
from speakeasy_client_sdk_python._hooks import HookContext
from speakeasy_client_sdk_python.models import errors, operations, shared
from speakeasy_client_sdk_python.types import BaseModel, OptionalNullable, SDKError, UNSET
from typing import List, Optional, Union, cast

class GenerateRequestPostmanCollectionAcceptEnum(str, Enum):
    APPLICATION_JSON = "application/json"
    APPLICATION_OCTET_STREAM = "application/octet-stream"

class Requests(BaseSDK):
    r"""REST APIs for retrieving request information"""
    
    
    def generate_request_postman_collection(
        self, *,
        request: Union[operations.GenerateRequestPostmanCollectionRequest, operations.GenerateRequestPostmanCollectionRequestTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        accept_header_override: Optional[GenerateRequestPostmanCollectionAcceptEnum] = None
    ) -> operations.GenerateRequestPostmanCollectionResponse:
        r"""Generate a Postman collection for a particular request.

        Generates a Postman collection for a particular request.
        Allowing it to be replayed with the same inputs that were captured by the SDK.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param accept_header_override: Override the default accept header for this method
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.GenerateRequestPostmanCollectionRequest)
        request = cast(operations.GenerateRequestPostmanCollectionRequest, request)
        
        req = self.build_request(
            method="GET",
            path="/v1/eventlog/{requestID}/generate/postman",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value=accept_header_override.value if accept_header_override is not None else "application/json;q=1, application/octet-stream;q=0",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="generateRequestPostmanCollection", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            stream=True,
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/octet-stream"):
            return operations.GenerateRequestPostmanCollectionResponse(postman_collection=http_res, status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        if utils.match_response(http_res, "default", "application/json"):
            return operations.GenerateRequestPostmanCollectionResponse(error=utils.unmarshal_json(utils.stream_to_text(http_res), Optional[errors.Error]), status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def generate_request_postman_collection_async(
        self, *,
        request: Union[operations.GenerateRequestPostmanCollectionRequest, operations.GenerateRequestPostmanCollectionRequestTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        accept_header_override: Optional[GenerateRequestPostmanCollectionAcceptEnum] = None
    ) -> operations.GenerateRequestPostmanCollectionResponse:
        r"""Generate a Postman collection for a particular request.

        Generates a Postman collection for a particular request.
        Allowing it to be replayed with the same inputs that were captured by the SDK.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param accept_header_override: Override the default accept header for this method
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.GenerateRequestPostmanCollectionRequest)
        request = cast(operations.GenerateRequestPostmanCollectionRequest, request)
        
        req = self.build_request(
            method="GET",
            path="/v1/eventlog/{requestID}/generate/postman",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value=accept_header_override.value if accept_header_override is not None else "application/json;q=1, application/octet-stream;q=0",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="generateRequestPostmanCollection", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            stream=True,
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/octet-stream"):
            return operations.GenerateRequestPostmanCollectionResponse(postman_collection=http_res, status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        if utils.match_response(http_res, "default", "application/json"):
            return operations.GenerateRequestPostmanCollectionResponse(error=utils.unmarshal_json(utils.stream_to_text(http_res), Optional[errors.Error]), status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    def get_request_from_event_log(
        self, *,
        request: Union[operations.GetRequestFromEventLogRequest, operations.GetRequestFromEventLogRequestTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.GetRequestFromEventLogResponse:
        r"""Get information about a particular request.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.GetRequestFromEventLogRequest)
        request = cast(operations.GetRequestFromEventLogRequest, request)
        
        req = self.build_request(
            method="GET",
            path="/v1/eventlog/{requestID}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="getRequestFromEventLog", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return operations.GetRequestFromEventLogResponse(unbounded_request=utils.unmarshal_json(http_res.text, Optional[shared.UnboundedRequest]), status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        if utils.match_response(http_res, "default", "application/json"):
            return operations.GetRequestFromEventLogResponse(error=utils.unmarshal_json(http_res.text, Optional[errors.Error]), status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def get_request_from_event_log_async(
        self, *,
        request: Union[operations.GetRequestFromEventLogRequest, operations.GetRequestFromEventLogRequestTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.GetRequestFromEventLogResponse:
        r"""Get information about a particular request.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.GetRequestFromEventLogRequest)
        request = cast(operations.GetRequestFromEventLogRequest, request)
        
        req = self.build_request(
            method="GET",
            path="/v1/eventlog/{requestID}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="getRequestFromEventLog", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return operations.GetRequestFromEventLogResponse(unbounded_request=utils.unmarshal_json(http_res.text, Optional[shared.UnboundedRequest]), status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        if utils.match_response(http_res, "default", "application/json"):
            return operations.GetRequestFromEventLogResponse(error=utils.unmarshal_json(http_res.text, Optional[errors.Error]), status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    def query_event_log(
        self, *,
        request: Optional[Union[operations.QueryEventLogRequest, operations.QueryEventLogRequestTypedDict]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.QueryEventLogResponse:
        r"""Query the event log to retrieve a list of requests.

        Supports retrieving a list of request captured by the SDK for this workspace.
        Allows the filtering of requests on a number of criteria such as ApiID, VersionID, Path, Method, etc.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.QueryEventLogRequest)
        request = cast(operations.QueryEventLogRequest, request)
        
        req = self.build_request(
            method="GET",
            path="/v1/eventlog/query",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="queryEventLog", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return operations.QueryEventLogResponse(bounded_requests=utils.unmarshal_json(http_res.text, Optional[List[shared.BoundedRequest]]), status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        if utils.match_response(http_res, "default", "application/json"):
            return operations.QueryEventLogResponse(error=utils.unmarshal_json(http_res.text, Optional[errors.Error]), status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def query_event_log_async(
        self, *,
        request: Optional[Union[operations.QueryEventLogRequest, operations.QueryEventLogRequestTypedDict]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.QueryEventLogResponse:
        r"""Query the event log to retrieve a list of requests.

        Supports retrieving a list of request captured by the SDK for this workspace.
        Allows the filtering of requests on a number of criteria such as ApiID, VersionID, Path, Method, etc.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.QueryEventLogRequest)
        request = cast(operations.QueryEventLogRequest, request)
        
        req = self.build_request(
            method="GET",
            path="/v1/eventlog/query",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="queryEventLog", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return operations.QueryEventLogResponse(bounded_requests=utils.unmarshal_json(http_res.text, Optional[List[shared.BoundedRequest]]), status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        if utils.match_response(http_res, "default", "application/json"):
            return operations.QueryEventLogResponse(error=utils.unmarshal_json(http_res.text, Optional[errors.Error]), status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
