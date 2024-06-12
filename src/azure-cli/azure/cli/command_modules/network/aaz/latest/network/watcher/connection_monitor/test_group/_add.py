# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

import json
import sys

from azure.cli.core.aaz import *

@register_command(
    "network watcher connection-monitor test-group add",
    is_preview=True,
)
class Add(AAZCommand):
    """Create a test group object using endpoints and test configurations.

    :example: Create a test group along with existing endpoint and test configuration via their names
        az network watcher connection-monitor test-group create --name MyTestGroup --sources [$src1 $src2] --destinations [$dst1] --test-configurations [$test1 $test2]

    """

    _aaz_info = {
        "version": "2022-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/networkwatchers/{}/connectionmonitors/{}", "2022-01-01", "properties.testGroups[]"],
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
        _args_schema.disable = AAZBoolArg(
            options=["--disable"],
            help="Value indicating whether test group is disabled. false is  default.  Allowed values: false, true.",
        )
        _args_schema.test_group_name = AAZStrArg(
            options=["-n", "--name", "--test-group-name"],
            help="The name of the connection monitor test group.",
            required=True,
        )

        # used to group together command line arguments
        # define Arg Group "V2 Endpoint"

        _args_schema = cls._args_schema
        _args_schema.destinations = AAZListArg(
            options=["--destinations"],
            arg_group="V2 Endpoint",
            help="List of destination endpoint names.",
            required=True,
        )
        _args_schema.sources = AAZListArg(
            options=["--sources"],
            arg_group="V2 Endpoint",
            help="List of source endpoint names.",
            required=True,
        )

        destinations = cls._args_schema.destinations
        destinations.Element = AAZObjectArg()
        destinations.Element.name = AAZStrArg(
            options=["--name"],
            help="Name of the destination endpoint.",
        )
        destinations.Element.address = AAZStrArg(
            options=["--address"],
            help="Address of the connection monitor destination (IP or domain name).",
        )
        destinations.Element.resource_id = AAZStrArg(
            options=["--resource-id"],
            help="The ID of the resource used as the destination by connection monitor.",
        )
        destinations.Element.type = AAZStrArg(
            options=["--type"],
            help="The endpoint type.  Allowed values: AzureArcVM, AzureSubnet, AzureVM, AzureVMSS, AzureVNet, ExternalAddress, MMAWorkspaceMachine, MMAWorkspaceNetwork.",
            enum={"AzureArcVM": "AzureArcVM", "AzureSubnet": "AzureSubnet", "AzureVM": "AzureVM", "AzureVMSS": "AzureVMSS", "AzureVNet": "AzureVNet", "ExternalAddress": "ExternalAddress", "MMAWorkspaceMachine": "MMAWorkspaceMachine", "MMAWorkspaceNetwork": "MMAWorkspaceNetwork"},
        )
        destinations.Element.coverage_level = AAZStrArg(
            options=["--coverage-level"],
            help="Test coverage for the endpoint. Allowed values: AboveAverage, Average, BelowAverage, Default, Full, Low",
            enum={"AboveAverage": "AboveAverage", "Average": "Average", "BelowAverage": "BelowAverage", "Default": "Default", "Full": "Full", "Low": "Low"},
        )

        destinations.Element.scope = AAZObjectArg()
        destinations.Element.scope.exclude = AAZListArg(
            options=["--scope-exclude"],
            help="List of items which needs to be excluded from the endpoint scope.",
        )
        destinations.Element.scope.exclude.Element = AAZObjectArg()
        destinations.Element.scope.exclude.Element.address = AAZStrArg(
            options=["address"],
            help="The address of the endpoint item. Supported types are IPv4/IPv6 subnet mask or IPv4/IPv6 IP address.",
        )
        destinations.Element.scope.include = AAZListArg(
            options=["--scope-include"],
            help="List of items which needs to be excluded from the endpoint scope.",
        )
        destinations.Element.scope.include.Element = AAZObjectArg()
        destinations.Element.scope.include.Element.address = AAZStrArg(
            options=["address"],
            help="The address of the endpoint item. Supported types are IPv4/IPv6 subnet mask or IPv4/IPv6 IP address.",
        )

        sources = cls._args_schema.sources
        sources.Element = AAZObjectArg()

        sources.Element.name = AAZStrArg(
            options=["--name"],
            help="Name of the source endpoint.",
        )
        sources.Element.address = AAZStrArg(
            options=["--address"],
            help="Address of the connection monitor destination (IP or domain name).",
        )
        sources.Element.resource_id = AAZStrArg(
            options=["--resource-id"],
            help="The ID of the resource used as the destination by connection monitor.",
        )
        sources.Element.type = AAZStrArg(
            options=["--type"],
            help="The endpoint type.  Allowed values: AzureArcVM, AzureSubnet, AzureVM, AzureVMSS, AzureVNet, ExternalAddress, MMAWorkspaceMachine, MMAWorkspaceNetwork.",
            enum={"AzureArcVM": "AzureArcVM", "AzureSubnet": "AzureSubnet", "AzureVM": "AzureVM", "AzureVMSS": "AzureVMSS", "AzureVNet": "AzureVNet", "ExternalAddress": "ExternalAddress", "MMAWorkspaceMachine": "MMAWorkspaceMachine", "MMAWorkspaceNetwork": "MMAWorkspaceNetwork"},
        )
        sources.Element.coverage_level = AAZStrArg(
            options=["--coverage-level"],
            help="Test coverage for the endpoint. Allowed values: AboveAverage, Average, BelowAverage, Default, Full, Low",
            enum={"AboveAverage": "AboveAverage", "Average": "Average", "BelowAverage": "BelowAverage", "Default": "Default", "Full": "Full", "Low": "Low"},
        )
        sources.Element.scope = AAZObjectArg()
        sources.Element.scope.exclude = AAZListArg(
            options=["--scope-exclude"],
            help="List of items which needs to be excluded from the endpoint scope.",
        )
        sources.Element.scope.exclude.Element = AAZObjectArg()
        sources.Element.scope.exclude.Element.address = AAZStrArg(
            options=["address"],
            help="The address of the endpoint item. Supported types are IPv4/IPv6 subnet mask or IPv4/IPv6 IP address.",
        )
        sources.Element.scope.include = AAZListArg(
            options=["--scope-include"],
            help="List of items which needs to be excluded from the endpoint scope.",
        )
        sources.Element.scope.include.Element = AAZObjectArg()
        sources.Element.scope.include.Element.address = AAZStrArg(
            options=["address"],
            help="The address of the endpoint item. Supported types are IPv4/IPv6 subnet mask or IPv4/IPv6 IP address.",
        )

        # define Arg Group "V2 Test Configuration"

        _args_schema = cls._args_schema
        _args_schema.test_configurations = AAZListArg(
            options=["--test-configurations"],
            arg_group="V2 Test Configuration",
            help="List of test configuration names.",
            required=True,
        )

        test_configurations = cls._args_schema.test_configurations
        test_configurations.Element = AAZObjectArg()

        _element = cls._args_schema.test_configurations.Element

        _element.name = AAZStrArg(
            options=["--name", "--test-configuration-name"],
            help="Name of test configuration"
        )
        _element.protocol = AAZStrArg(
            options=["--protocol"],
            help="The protocol to use in test evaluation.  Allowed values: Http, Icmp, Tcp.",
            enum={"Http": "Http", "Icmp": "Icmp", "Tcp": "Tcp"},
        )
        _element.frequency = AAZStrArg(
            options=["--frequency"],
            help="Frequency of test evaluation"
        )
        _element.location = AAZStrArg(
            options=["--location"],
            help="Location to create a test configuration"
        )

        _element.http_configuration = AAZObjectArg(
            options=["http-configuration"],
            help="The parameters used to perform test evaluation over HTTP.",
        )
        _element.icmp_configuration = AAZObjectArg(
            options=["icmp-configuration"],
            help="The parameters used to perform test evaluation over ICMP.",
        )

        _element.preferred_ip_version = AAZStrArg(
            options=["preferred-ip-version"],
            help="The preferred IP version to use in test evaluation. The connection monitor may choose to use a different version depending on other parameters.",
            enum={"IPv4": "IPv4", "IPv6": "IPv6"},
        )
        _element.success_threshold = AAZObjectArg(
            options=["success-threshold"],
            help="The threshold for declaring a test successful.",
        )
        _element.tcp_configuration = AAZObjectArg(
            options=["tcp-configuration"],
            help="The parameters used to perform test evaluation over TCP.",
        )

        http_configuration = cls._args_schema.test_configurations.Element.http_configuration
        http_configuration.method = AAZStrArg(
            options=["method"],
            help="The HTTP method to use.",
            enum={"Get": "Get", "Post": "Post"},
        )
        http_configuration.path = AAZStrArg(
            options=["path"],
            help="The path component of the URI. For instance, \"/dir1/dir2\".",
        )
        http_configuration.port = AAZIntArg(
            options=["port"],
            help="The port to connect to.",
            fmt=AAZIntArgFormat(
                maximum=65535,
                minimum=0,
            ),
        )
        http_configuration.prefer_https = AAZBoolArg(
            options=["prefer-https"],
            help="Value indicating whether HTTPS is preferred over HTTP in cases where the choice is not explicit.",
        )
        http_configuration.request_headers = AAZListArg(
            options=["request-headers"],
            help="The HTTP headers to transmit with the request.",
        )
        http_configuration.valid_status_code_ranges = AAZListArg(
            options=["valid-status-code-ranges"],
            help="HTTP status codes to consider successful. For instance, \"2xx,301-304,418\".",
        )

        request_headers = cls._args_schema.test_configurations.Element.http_configuration.request_headers
        request_headers.Element = AAZObjectArg()

        _element = cls._args_schema.test_configurations.Element.http_configuration.request_headers.Element
        _element.name = AAZStrArg(
            options=["name"],
            help="The name in HTTP header.",
        )
        _element.value = AAZStrArg(
            options=["value"],
            help="The value in HTTP header.",
        )

        valid_status_code_ranges = cls._args_schema.test_configurations.Element.http_configuration.valid_status_code_ranges
        valid_status_code_ranges.Element = AAZStrArg()

        icmp_configuration = cls._args_schema.test_configurations.Element.icmp_configuration
        icmp_configuration.disable_trace_route = AAZBoolArg(
            options=["disable-trace-route"],
            help="Value indicating whether path evaluation with trace route should be disabled.",
        )

        success_threshold = cls._args_schema.test_configurations.Element.success_threshold
        success_threshold.checks_failed_percent = AAZIntArg(
            options=["checks-failed-percent"],
            help="The maximum percentage of failed checks permitted for a test to evaluate as successful.",
        )
        success_threshold.round_trip_time_ms = AAZFloatArg(
            options=["round-trip-time-ms"],
            help="The maximum round-trip time in milliseconds permitted for a test to evaluate as successful.",
        )

        tcp_configuration = cls._args_schema.test_configurations.Element.tcp_configuration
        tcp_configuration.destination_port_behavior = AAZStrArg(
            options=["destination-port-behavior"],
            help="Destination port behavior.",
            enum={"ListenIfAvailable": "ListenIfAvailable", "None": "None"},
        )
        tcp_configuration.disable_trace_route = AAZBoolArg(
            options=["disable-trace-route"],
            help="Value indicating whether path evaluation with trace route should be disabled.",
        )
        tcp_configuration.port = AAZIntArg(
            options=["port"],
            help="The port to connect to.",
            fmt=AAZIntArgFormat(
                maximum=65535,
                minimum=0,
            ),
        )

        return cls._args_schema

    class InstanceCreateByJson(AAZJsonInstanceCreateOperation):

        def __call__(self, *args, **kwargs):
            return self._create_instance()

        #we are required to parse these explicitly as they are not being parsed by the aaz framework becuase eariler we did not pass objects inside a command as we are doing now
        def parse_arg(self, arg_index):
            if arg_index is not None:
                # The next element in sys.argv is the value of the argument
                arg = sys.argv[arg_index + 1]
                print("arg=", arg)

                # If arg is a list, convert each string in the list to a dictionary
                if isinstance(arg, list):
                    arg_list = []
                    for s in arg:
                        # Replace single quotes with double quotes to make it a valid JSON string
                        s = s.replace("'", '"')
                        # Parse the string into a dictionary
                        try:
                            arg_dict = json.loads(s)
                            arg_list.append(arg_dict)
                        except json.JSONDecodeError as e:
                            print(f"Failed to parse argument: {e}")
                else:
                    #converting it to a list because in create command we have test groups that contain list of sources, destinations and test configurations
                    # If arg is not a list, just replace single quotes with double quotes and parse it to convert it to a valid JSON string
                    arg = arg.replace("'", '"')
                    try:
                        arg_list = json.loads(arg)
                    except json.JSONDecodeError as e:
                        print(f"Failed to parse argument: {e}")
                        arg_list = []

                return arg_list

            return []


        def _create_instance(self):
            #comment to debug
            destinations_index = sys.argv.index('--destinations') if '--destinations' in sys.argv else None
            sources_index = sys.argv.index('--sources') if '--sources' in sys.argv else None
            test_configurations_index = sys.argv.index('--test-configurations') if '--test-configurations' in sys.argv else None

            destinations_list = self.parse_arg(destinations_index)
            sources_list = self.parse_arg(sources_index)
            test_configurations_list = self.parse_arg(test_configurations_index)


            data ={
                "testGroupName" : str(self.ctx.args.test_group_name),
                "sources" : sources_list,
                "destinations" : destinations_list,
                "testConfigurations" : test_configurations_list
            }

            data_str = str(data)
            data_str = data_str.replace(" ","")
            return data_str


__all__ = ["Add"]
