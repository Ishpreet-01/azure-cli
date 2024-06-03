# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *
import json
from azure.cli.core.aaz import AAZUndefined


@register_command(
    "network watcher connection-monitor test-configuration add",
    is_preview=True,
)
class Add(AAZCommand):
    """Add a test configuration to a connection monitor.

    :example: Add a test configuration with HTTP supported
        az network watcher connection-monitor test-configuration add --connection-monitor MyConnectionMonitor --location westus --name MyHTTPTestConfiguration --test-groups DefaultTestGroup --protocol Http --http-request-header name=Host value=bing.com --http- request-header name=UserAgent value=Edge

    :example: Add a test configuration with TCP supported
        az network watcher connection-monitor test-configuration add --connection-monitor MyConnectionMonitor --location westus --name MyHTTPTestConfiguration --test-groups TCPTestGroup DefaultTestGroup --protocol Tcp --tcp-port 4096
    """

    _aaz_info = {
        "version": "2022-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/networkwatchers/{}/connectionmonitors/{}", "2022-01-01", "properties.testConfigurations[]"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.InstanceCreateByJson(ctx=self.ctx)()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.connection_monitor = AAZStrArg(
            options=["--connection-monitor"],
            help="Connection monitor name.",
            required=False,
        )
        _args_schema.watcher_name = AAZStrArg(
            options=["--watcher-name"],
            help="The name of the Network Watcher resource.",
            required=False,
        )
        _args_schema.watcher_rg = AAZResourceGroupNameArg(
            options=["-g", "--watcher-rg"],
            help="Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.",
            required=False,
        )
        _args_schema.test_configuration_name = AAZStrArg(
            options=["-n", "--name", "--test-configuration-name"],
            help="The name of the connection monitor test configuration.",
            required=True,
        )
        _args_schema.preferred_ip_version = AAZStrArg(
            options=["--preferred-ip-version"],
            help="The preferred IP version to use in test evaluation. The connection monitor may choose to use a different version depending on other parameters.  Allowed values: IPv4, IPv6.",
            enum={"IPv4": "IPv4", "IPv6": "IPv6"},
        )
        _args_schema.protocol = AAZStrArg(
            options=["--protocol"],
            help="The protocol to use in test evaluation.  Allowed values: Http, Icmp, Tcp.",
            required=True,
            enum={"Http": "Http", "Icmp": "Icmp", "Tcp": "Tcp"},
        )
        _args_schema.threshold_failed_percent = AAZIntArg(
            options=["--threshold-failed-percent"],
            help="The maximum percentage of failed checks permitted for a test to evaluate as successful.",
        )
        _args_schema.threshold_round_trip_time = AAZFloatArg(
            options=["--threshold-round-trip-time"],
            help="The maximum round-trip time in milliseconds permitted for a test to evaluate as successful.",
        )
        _args_schema.frequency = AAZIntArg(
            options=["--frequency"],
            help="The frequency of test evaluation, in seconds.  Default: 60.",
        )

        # define Arg Group "HTTP Protocol"

        _args_schema = cls._args_schema
        _args_schema.http_method = AAZStrArg(
            options=["--http-method"],
            arg_group="HTTP Protocol",
            help="The HTTP method to use. Allowed values: Get, Post.",
            enum={"Get": "Get", "Post": "Post"},
        )
        _args_schema.http_path = AAZStrArg(
            options=["--http-path"],
            arg_group="HTTP Protocol",
            help="The path component of the URI. For instance, \"/dir1/dir2\".",
        )
        _args_schema.http_port = AAZIntArg(
            options=["--http-port"],
            arg_group="HTTP Protocol",
            help="The port to connect to.",
            fmt=AAZIntArgFormat(
                maximum=65535,
                minimum=0,
            ),
        )
        _args_schema.http_prefer_https = AAZBoolArg(
            options=["--http-prefer-https"],
            arg_group="HTTP Protocol",
            help="Value indicating whether HTTPS is preferred over HTTP in cases where the choice is not explicit.",
        )
        _args_schema.http_request_headers = AAZListArg(
            options=["--http-request-headers"],
            arg_group="HTTP Protocol",
            help="The HTTP headers to transmit with the request.",
            # required=False
        )
        _args_schema.http_valid_status_codes = AAZListArg(
            options=["--http-valid-status-codes"],
            arg_group="HTTP Protocol",
            help="HTTP status codes to consider successful. For instance, \"2xx,301-304,418\".",
        )

        http_request_headers = cls._args_schema.http_request_headers
        http_request_headers.Element = AAZObjectArg()

        _element = cls._args_schema.http_request_headers.Element
        _element.name = AAZStrArg(
            options=["name"],
            help="The name in HTTP header.",
        )
        _element.value = AAZStrArg(
            options=["value"],
            help="The value in HTTP header.",
        )

        http_valid_status_codes = cls._args_schema.http_valid_status_codes
        http_valid_status_codes.Element = AAZStrArg()

        # define Arg Group "ICMP Protocol"

        _args_schema = cls._args_schema
        _args_schema.icmp_disable_trace_route = AAZBoolArg(
            options=["--icmp-disable-trace-route"],
            arg_group="ICMP Protocol",
            help="Value indicating whether path evaluation with trace route should be disabled. false is default.  Allowed values: false, true.",
        )

        # define Arg Group "TCP Protocol"

        _args_schema = cls._args_schema
        _args_schema.tcp_port_behavior = AAZStrArg(
            options=["--tcp-port-behavior"],
            arg_group="TCP Protocol",
            help="Destination port behavior.  Allowed values: ListenIfAvailable,  None.",
            enum={"ListenIfAvailable": "ListenIfAvailable", "None": "None"},
        )
        _args_schema.tcp_disable_trace_route = AAZBoolArg(
            options=["--tcp-disable-trace-route"],
            arg_group="TCP Protocol",
            help="Value indicating whether path evaluation with trace route should be disabled. false is default.  Allowed values: false, true.",
        )
        _args_schema.tcp_port = AAZIntArg(
            options=["--tcp-port"],
            arg_group="TCP Protocol",
            help="The port to connect to.",
            fmt=AAZIntArgFormat(
                maximum=65535,
                minimum=0,
            ),
        )
        return cls._args_schema

    def _execute_operations(self):  
        result = self.InstanceCreateByJson(ctx=self.ctx)()
        return json.loads(result)

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_create(self):
        pass

    @register_callback
    def post_instance_create(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.selectors.subresource.required(), client_flatten=True)

    class SubresourceSelector(AAZJsonSelector):

        def _get(self):
            pass

        def _set(self, value):
            pass

    class InstanceCreateByJson(AAZJsonInstanceCreateOperation):
      

      def __call__(self, *args, **kwargs):
            return self._create_instance()
       
      def clean_dict(self,d):
            
            clean = {}
            for k, v in d.items():
                if isinstance(v, dict):
                    v = self.clean_dict(v)
                elif isinstance(v, str):
                    v = v.strip()
                if v not in [None, 'Undefined', {}, '', AAZUndefined,[]]:
                    clean[k] = v
            return clean


      def _create_instance(self):


        data = {
              "name":str(self.ctx.args.test_configuration_name),
              "protocol":str(self.ctx.args.protocol),
              "frequency":str(self.ctx.args.frequency),
              "preferredIPVersion": self.ctx.args.preferred_ip_version,
              "httpConfiguration": {},
              "icmpConfiguration": {},
              "successThreshold": {},
              "tcpConfiguration": {}

          }
         
        if hasattr(self.ctx.args, "http_method") or hasattr(self.ctx.args, "http_path") or hasattr(self.ctx.args, "http_port") or hasattr(self.ctx.args, "http_prefer_https") or hasattr(self.ctx.args, "http_request_headers") or hasattr(self.ctx.args, "http_valid_status_codes"):
            data["httpConfiguration"]["method"] = getattr(self.ctx.args, "http_method", None)
            data["httpConfiguration"]["path"] = getattr(self.ctx.args, "http_path", None)
            data["httpConfiguration"]["port"] = getattr(self.ctx.args, "http_port", None)
            data["httpConfiguration"]["prefer_https"] = getattr(self.ctx.args, "http_prefer_https", None)
            data["httpConfiguration"]["request_headers"] = []
            data["httpConfiguration"]["valid_status_code_ranges"] = []

            if hasattr(self.ctx.args, "http_valid_status_codes"):
                valid_status_codes = getattr(self.ctx.args, "http_valid_status_codes",[])
                print(valid_status_codes)
                for code in valid_status_codes:
                   data["httpConfiguration"]["valid_status_code_ranges"].append(code)
            

        # Populate request headers
        if hasattr(self.ctx.args, "http_request_headers"):
            request_headers = getattr(self.ctx.args, "http_request_headers", [])
            for header in request_headers:
                data["httpConfiguration"]["request_headers"].append({
                    "name": header.get("name"),
                    "value": header.get("value")
                })

    # Populate icmpConfiguration
        if hasattr(self.ctx.args, "icmp_disable_trace_route") and self.ctx.args.icmp_disable_trace_route is not None:
            data["icmpConfiguration"]["disable_trace_route"] = self.ctx.args.icmp_disable_trace_route

        # Populate successThreshold
        if hasattr(self.ctx.args, "threshold_failed_percent") and self.ctx.args.threshold_failed_percent is not None or hasattr(self.ctx.args, "threshold_round_trip_time") and self.ctx.args.threshold_round_trip_time is not None:
            data["successThreshold"]["checks_failed_percent"] = getattr(self.ctx.args, "threshold_failed_percent", None)
            data["successThreshold"]["round_trip_time_ms"] = getattr(self.ctx.args, "threshold_round_trip_time", None)

        # Populate tcpConfiguration
        if hasattr(self.ctx.args, "tcp_port_behavior") or hasattr(self.ctx.args, "tcp_disable_trace_route") or hasattr(self.ctx.args, "tcp_port"):
            data["tcpConfiguration"]["destination_port_behavior"] = getattr(self.ctx.args, "tcp_port_behavior", None)
            data["tcpConfiguration"]["disable_trace_route"] = getattr(self.ctx.args, "tcp_disable_trace_route", None)
            data["tcpConfiguration"]["port"] = getattr(self.ctx.args, "tcp_port", None)

    
        
        #print(data)

        #removing null and undefined fields from data
        data = {k: v for k, v in data.items() if v is not None and v != 'Undefined' and (not isinstance(v, dict) or any(v.values()))}
        data = self.clean_dict(data)
        data_str = str(data)

        #removing spaces
        data_str = data_str.replace(" ", "")
        
        return data_str


__all__ = ["Add"]










