"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .basesdk import BaseSDK
from speakeasy_client_sdk_python._hooks import HookContext
from speakeasy_client_sdk_python.models import errors, operations, shared
from speakeasy_client_sdk_python.types import BaseModel, Nullable, UNSET
import speakeasy_client_sdk_python.utils as utils
from typing import List, Optional, Union

class Events(BaseSDK):
    r"""REST APIs for capturing event data"""
    
    
    def get_workspace_events_by_target(
        self, *,
        request: Union[operations.GetWorkspaceEventsByTargetRequest, operations.GetWorkspaceEventsByTargetRequestTypedDict],
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> operations.GetWorkspaceEventsByTargetResponse:
        r"""Load recent events for a particular workspace

        :param request: The request object to send.
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.GetWorkspaceEventsByTargetRequest)
        
        req = self.build_request(
            method="GET",
            path="/v1/workspace/{workspaceID}/events/targets/{targetID}/events",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            _globals=operations.GetWorkspaceEventsByTargetGlobals(
                workspace_id=self.sdk_configuration.globals.workspace_id,
            ),
            security=self.sdk_configuration.security,
            timeout_config=timeout_config,
        )
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="getWorkspaceEventsByTarget", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
        )
        
        res = operations.GetWorkspaceEventsByTargetResponse(status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        
        if utils.match_response(http_res, "200", "application/json"):
            res.cli_event_batch = utils.unmarshal_json(http_res.text, Optional[List[shared.CliEvent]])
        elif utils.match_response(http_res, "4XX", "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        elif utils.match_response(http_res, "5XX", "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.ErrorData)
            raise errors.Error(data=data)
        else:
            content_type = http_res.headers.get("Content-Type")
            raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

        return res
    
    
    async def get_workspace_events_by_target_async(
        self, *,
        request: Union[operations.GetWorkspaceEventsByTargetRequest, operations.GetWorkspaceEventsByTargetRequestTypedDict],
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> operations.GetWorkspaceEventsByTargetResponse:
        r"""Load recent events for a particular workspace

        :param request: The request object to send.
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.GetWorkspaceEventsByTargetRequest)
        
        req = self.build_request(
            method="GET",
            path="/v1/workspace/{workspaceID}/events/targets/{targetID}/events",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            _globals=operations.GetWorkspaceEventsByTargetGlobals(
                workspace_id=self.sdk_configuration.globals.workspace_id,
            ),
            security=self.sdk_configuration.security,
            timeout_config=timeout_config,
        )
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="getWorkspaceEventsByTarget", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
        )
        
        res = operations.GetWorkspaceEventsByTargetResponse(status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        
        if utils.match_response(http_res, "200", "application/json"):
            res.cli_event_batch = utils.unmarshal_json(http_res.text, Optional[List[shared.CliEvent]])
        elif utils.match_response(http_res, "4XX", "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        elif utils.match_response(http_res, "5XX", "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.ErrorData)
            raise errors.Error(data=data)
        else:
            content_type = http_res.headers.get("Content-Type")
            raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

        return res
    
    
    def get_workspace_targets(
        self, *,
        request: Optional[Union[operations.GetWorkspaceTargetsRequest, operations.GetWorkspaceTargetsRequestTypedDict]] = None,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> operations.GetWorkspaceTargetsResponse:
        r"""Load targets for a particular workspace

        :param request: The request object to send.
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.GetWorkspaceTargetsRequest)
        
        req = self.build_request(
            method="GET",
            path="/v1/workspace/{workspaceID}/events/targets",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            _globals=operations.GetWorkspaceTargetsGlobals(
                workspace_id=self.sdk_configuration.globals.workspace_id,
            ),
            security=self.sdk_configuration.security,
            timeout_config=timeout_config,
        )
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="getWorkspaceTargets", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
        )
        
        res = operations.GetWorkspaceTargetsResponse(status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        
        if utils.match_response(http_res, "200", "application/json"):
            res.target_sdk_list = utils.unmarshal_json(http_res.text, Optional[List[shared.TargetSDK]])
        elif utils.match_response(http_res, "4XX", "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        elif utils.match_response(http_res, "5XX", "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.ErrorData)
            raise errors.Error(data=data)
        else:
            content_type = http_res.headers.get("Content-Type")
            raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

        return res
    
    
    async def get_workspace_targets_async(
        self, *,
        request: Optional[Union[operations.GetWorkspaceTargetsRequest, operations.GetWorkspaceTargetsRequestTypedDict]] = None,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> operations.GetWorkspaceTargetsResponse:
        r"""Load targets for a particular workspace

        :param request: The request object to send.
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.GetWorkspaceTargetsRequest)
        
        req = self.build_request(
            method="GET",
            path="/v1/workspace/{workspaceID}/events/targets",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            _globals=operations.GetWorkspaceTargetsGlobals(
                workspace_id=self.sdk_configuration.globals.workspace_id,
            ),
            security=self.sdk_configuration.security,
            timeout_config=timeout_config,
        )
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="getWorkspaceTargets", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
        )
        
        res = operations.GetWorkspaceTargetsResponse(status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        
        if utils.match_response(http_res, "200", "application/json"):
            res.target_sdk_list = utils.unmarshal_json(http_res.text, Optional[List[shared.TargetSDK]])
        elif utils.match_response(http_res, "4XX", "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        elif utils.match_response(http_res, "5XX", "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.ErrorData)
            raise errors.Error(data=data)
        else:
            content_type = http_res.headers.get("Content-Type")
            raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

        return res
    
    
    def post_workspace_events(
        self, *,
        request: Union[operations.PostWorkspaceEventsRequest, operations.PostWorkspaceEventsRequestTypedDict],
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> operations.PostWorkspaceEventsResponse:
        r"""Post events for a specific workspace

        Sends an array of events to be stored for a particular workspace.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.PostWorkspaceEventsRequest)
        
        req = self.build_request(
            method="POST",
            path="/v1/workspace/{workspaceID}/events",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            _globals=operations.PostWorkspaceEventsGlobals(
                workspace_id=self.sdk_configuration.globals.workspace_id,
            ),
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request.request_body, False, False, "json", List[shared.CliEvent]),
            timeout_config=timeout_config,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig("backoff", utils.BackoffStrategy(100, 2000, 1.5, 60000), True)

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "408",
                "500",
                "502",
                "503"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="postWorkspaceEvents", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        res = operations.PostWorkspaceEventsResponse(status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        
        if utils.match_response(http_res, "2XX", "*"):
            pass
        elif utils.match_response(http_res, "4XX", "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        elif utils.match_response(http_res, "5XX", "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.ErrorData)
            raise errors.Error(data=data)
        else:
            content_type = http_res.headers.get("Content-Type")
            raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

        return res
    
    
    async def post_workspace_events_async(
        self, *,
        request: Union[operations.PostWorkspaceEventsRequest, operations.PostWorkspaceEventsRequestTypedDict],
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> operations.PostWorkspaceEventsResponse:
        r"""Post events for a specific workspace

        Sends an array of events to be stored for a particular workspace.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.PostWorkspaceEventsRequest)
        
        req = self.build_request(
            method="POST",
            path="/v1/workspace/{workspaceID}/events",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            _globals=operations.PostWorkspaceEventsGlobals(
                workspace_id=self.sdk_configuration.globals.workspace_id,
            ),
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request.request_body, False, False, "json", List[shared.CliEvent]),
            timeout_config=timeout_config,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig("backoff", utils.BackoffStrategy(100, 2000, 1.5, 60000), True)

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "408",
                "500",
                "502",
                "503"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="postWorkspaceEvents", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        res = operations.PostWorkspaceEventsResponse(status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        
        if utils.match_response(http_res, "2XX", "*"):
            pass
        elif utils.match_response(http_res, "4XX", "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        elif utils.match_response(http_res, "5XX", "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.ErrorData)
            raise errors.Error(data=data)
        else:
            content_type = http_res.headers.get("Content-Type")
            raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

        return res
    
    
    def search_workspace_events(
        self, *,
        request: Optional[Union[operations.SearchWorkspaceEventsRequest, operations.SearchWorkspaceEventsRequestTypedDict]] = None,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> operations.SearchWorkspaceEventsResponse:
        r"""Search events for a particular workspace by any field

        :param request: The request object to send.
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.SearchWorkspaceEventsRequest)
        
        req = self.build_request(
            method="GET",
            path="/v1/workspace/{workspaceID}/events",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            _globals=operations.SearchWorkspaceEventsGlobals(
                workspace_id=self.sdk_configuration.globals.workspace_id,
            ),
            security=self.sdk_configuration.security,
            timeout_config=timeout_config,
        )
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="searchWorkspaceEvents", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
        )
        
        res = operations.SearchWorkspaceEventsResponse(status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        
        if utils.match_response(http_res, "200", "application/json"):
            res.cli_event_batch = utils.unmarshal_json(http_res.text, Optional[List[shared.CliEvent]])
        elif utils.match_response(http_res, "4XX", "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        elif utils.match_response(http_res, "5XX", "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.ErrorData)
            raise errors.Error(data=data)
        else:
            content_type = http_res.headers.get("Content-Type")
            raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

        return res
    
    
    async def search_workspace_events_async(
        self, *,
        request: Optional[Union[operations.SearchWorkspaceEventsRequest, operations.SearchWorkspaceEventsRequestTypedDict]] = None,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> operations.SearchWorkspaceEventsResponse:
        r"""Search events for a particular workspace by any field

        :param request: The request object to send.
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.SearchWorkspaceEventsRequest)
        
        req = self.build_request(
            method="GET",
            path="/v1/workspace/{workspaceID}/events",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            _globals=operations.SearchWorkspaceEventsGlobals(
                workspace_id=self.sdk_configuration.globals.workspace_id,
            ),
            security=self.sdk_configuration.security,
            timeout_config=timeout_config,
        )
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="searchWorkspaceEvents", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
        )
        
        res = operations.SearchWorkspaceEventsResponse(status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        
        if utils.match_response(http_res, "200", "application/json"):
            res.cli_event_batch = utils.unmarshal_json(http_res.text, Optional[List[shared.CliEvent]])
        elif utils.match_response(http_res, "4XX", "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        elif utils.match_response(http_res, "5XX", "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.ErrorData)
            raise errors.Error(data=data)
        else:
            content_type = http_res.headers.get("Content-Type")
            raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

        return res
    