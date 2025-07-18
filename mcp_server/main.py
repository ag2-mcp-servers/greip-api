# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T03:16:34+00:00



import argparse
import json
import os
from typing import *
from typing import Optional

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import BaseSecurity
from fastapi import Query

app = MCPProxy(
    contact={
        'email': 'info@greip.io',
        'name': 'Greip Support',
        'url': 'https://greip.io/contact',
    },
    description='This documentation shows how to use Greip API, By highlighting the API methods, options and some other features that allow you to get the most of this API.',
    termsOfService='https://greip.io/terms',
    title='Greip API',
    version='1.0.0',
    servers=[
        {'description': 'Production server', 'url': 'https://gregeoip.com'},
        {'description': 'Development server', 'url': 'https://dev.gregeoip.com'},
    ],
)


@app.get(
    '/BulkLookup',
    description=""" BulkLookup endpoint: Returns the geolocation data of multiple IP Addresses. """,
    tags=['ip_address_lookup', 'geographical_information_fetching'],
)
def get__bulk_lookup(
    key: str,
    ips: str = ...,
    params: Optional[str] = None,
    lang: Optional[str] = None,
    format: Optional[str] = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/Country',
    description=""" Country endpoint: Returns the information of a specific country by passing the `countrCode`. """,
    tags=['geographical_information_fetching'],
)
def get__country(
    key: str,
    country_code: str = Query(..., alias='CountryCode'),
    params: Optional[str] = None,
    lang: Optional[str] = None,
    format: Optional[str] = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/GeoIP',
    description=""" GeoIP endpoint: Returns the geolocation data of the visitor. """,
    tags=['ip_address_lookup', 'geographical_information_fetching'],
)
def get__geo_i_p(
    key: str,
    params: Optional[str] = None,
    lang: Optional[str] = None,
    format: Optional[str] = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/IPLookup',
    description=""" IPLookup endpoint: Returns the geolocation data of a specific IP Address. """,
    tags=['ip_address_lookup', 'geographical_information_fetching'],
)
def get__i_p_lookup(
    key: str,
    ip: str = ...,
    params: Optional[str] = None,
    lang: Optional[str] = None,
    format: Optional[str] = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/badWords',
    description=""" badWords endpoint: Detects whether user inputs contain profanity or not. """,
    tags=['text_content_filter'],
)
def get_bad_words(
    key: str,
    text: str = ...,
    list_bad_words: Optional[str] = Query(None, alias='listBadWords'),
    score_only: Optional[str] = Query(None, alias='scoreOnly'),
    format: Optional[str] = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
