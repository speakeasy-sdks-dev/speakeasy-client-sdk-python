"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .httpclient import AsyncHttpClient, HttpClient
from .sdkconfiguration import SDKConfiguration
from .utils.logger import Logger, get_default_logger
from .utils.retries import RetryConfig
import httpx
from speakeasy_client_sdk_python import utils
from speakeasy_client_sdk_python._hooks import SDKHooks
from speakeasy_client_sdk_python.apiendpoints import APIEndpoints
from speakeasy_client_sdk_python.apis import Apis
from speakeasy_client_sdk_python.artifacts import Artifacts
from speakeasy_client_sdk_python.auth import Auth
from speakeasy_client_sdk_python.embeds import Embeds
from speakeasy_client_sdk_python.events import Events
from speakeasy_client_sdk_python.github import Github
from speakeasy_client_sdk_python.metadata import Metadata
from speakeasy_client_sdk_python.models import internal, shared
from speakeasy_client_sdk_python.organizations import Organizations
from speakeasy_client_sdk_python.reports import Reports
from speakeasy_client_sdk_python.requests import Requests
from speakeasy_client_sdk_python.schemas import Schemas
from speakeasy_client_sdk_python.shorturls import ShortURLs
from speakeasy_client_sdk_python.suggest import Suggest
from speakeasy_client_sdk_python.types import OptionalNullable, UNSET
from speakeasy_client_sdk_python.workspaces import Workspaces
from typing import Callable, Dict, Optional, Union


class Speakeasy(BaseSDK):
    r"""Speakeasy API: The Speakeasy API allows teams to manage common operations with their APIs
    /docs - The Speakeasy Platform Documentation
    """

    apis: Apis
    r"""REST APIs for managing Api entities"""
    api_endpoints: APIEndpoints
    r"""REST APIs for managing ApiEndpoint entities"""
    metadata: Metadata
    r"""REST APIs for managing Version Metadata entities"""
    schemas: Schemas
    r"""REST APIs for managing Schema entities"""
    artifacts: Artifacts
    r"""REST APIs for working with Registry artifacts"""
    auth: Auth
    r"""REST APIs for managing Authentication"""
    requests: Requests
    r"""REST APIs for retrieving request information"""
    github: Github
    organizations: Organizations
    reports: Reports
    r"""REST APIs for managing reports"""
    short_ur_ls: ShortURLs
    r"""REST APIs for managing short URLs"""
    suggest: Suggest
    r"""REST APIs for managing LLM OAS suggestions"""
    embeds: Embeds
    r"""REST APIs for managing embeds"""
    workspaces: Workspaces
    events: Events
    r"""REST APIs for capturing event data"""

    def __init__(
        self,
        security: Optional[
            Union[shared.Security, Callable[[], shared.Security]]
        ] = None,
        workspace_id: Optional[str] = None,
        server: Optional[str] = None,
        server_url: Optional[str] = None,
        url_params: Optional[Dict[str, str]] = None,
        client: Optional[HttpClient] = None,
        async_client: Optional[AsyncHttpClient] = None,
        retry_config: OptionalNullable[RetryConfig] = UNSET,
        timeout_ms: Optional[int] = None,
        debug_logger: Optional[Logger] = None,
    ) -> None:
        r"""Instantiates the SDK configuring it with the provided parameters.

        :param security: The security details required for authentication
        :param workspace_id: Configures the workspace_id parameter for all supported operations
        :param server: The server by name to use for all methods
        :param server_url: The server URL to use for all methods
        :param url_params: Parameters to optionally template the server URL with
        :param client: The HTTP client to use for all synchronous methods
        :param async_client: The Async HTTP client to use for all asynchronous methods
        :param retry_config: The retry configuration to use for all supported methods
        :param timeout_ms: Optional request timeout applied to each operation in milliseconds
        """
        if client is None:
            client = httpx.Client()

        assert issubclass(
            type(client), HttpClient
        ), "The provided client must implement the HttpClient protocol."

        if async_client is None:
            async_client = httpx.AsyncClient()

        if debug_logger is None:
            debug_logger = get_default_logger()

        assert issubclass(
            type(async_client), AsyncHttpClient
        ), "The provided async_client must implement the AsyncHttpClient protocol."

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        _globals = internal.Globals(
            workspace_id=utils.get_global_from_env(workspace_id, "WORKSPACE_ID", str),
        )

        BaseSDK.__init__(
            self,
            SDKConfiguration(
                client=client,
                async_client=async_client,
                globals=_globals,
                security=security,
                server_url=server_url,
                server=server,
                retry_config=retry_config,
                timeout_ms=timeout_ms,
                debug_logger=debug_logger,
            ),
        )

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(
            current_server_url, self.sdk_configuration.client
        )
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration.__dict__["_hooks"] = hooks

        self._init_sdks()

    def _init_sdks(self):
        self.apis = Apis(self.sdk_configuration)
        self.api_endpoints = APIEndpoints(self.sdk_configuration)
        self.metadata = Metadata(self.sdk_configuration)
        self.schemas = Schemas(self.sdk_configuration)
        self.artifacts = Artifacts(self.sdk_configuration)
        self.auth = Auth(self.sdk_configuration)
        self.requests = Requests(self.sdk_configuration)
        self.github = Github(self.sdk_configuration)
        self.organizations = Organizations(self.sdk_configuration)
        self.reports = Reports(self.sdk_configuration)
        self.short_ur_ls = ShortURLs(self.sdk_configuration)
        self.suggest = Suggest(self.sdk_configuration)
        self.embeds = Embeds(self.sdk_configuration)
        self.workspaces = Workspaces(self.sdk_configuration)
        self.events = Events(self.sdk_configuration)
