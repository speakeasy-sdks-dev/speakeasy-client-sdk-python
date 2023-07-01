"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests
from dataclasses import dataclass


SERVER_PROD = 'prod'
SERVERS = {
	SERVER_PROD: 'https://api.prod.speakeasyapi.dev',
}
"""Contains the list of servers available to the SDK"""


@dataclass
class SDKConfiguration:
    client: requests.Session
    security_client: requests.Session
    server_url: str = ''
    server: str = ''
    language: str = 'python'
    openapi_doc_version: str = '0.3.0'
    sdk_version: str = '1.39.0'
    gen_version: str = '2.55.0'

    def get_server_details(self) -> tuple[str, dict[str, str]]:
        if self.server_url:
            return self.server_url.removesuffix('/'), {}
        if not self.server:
            self.server = SERVER_PROD

        return SERVERS[self.server], {}
