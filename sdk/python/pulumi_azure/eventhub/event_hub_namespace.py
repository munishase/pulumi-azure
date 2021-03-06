# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class EventHubNamespace(pulumi.CustomResource):
    auto_inflate_enabled: pulumi.Output[bool]
    """
    Is Auto Inflate enabled for the EventHub Namespace?
    """
    capacity: pulumi.Output[int]
    """
    Specifies the Capacity / Throughput Units for a `Standard` SKU namespace. Valid values range from 1 - 20.
    """
    default_primary_connection_string: pulumi.Output[str]
    """
    The primary connection string for the authorization
    rule `RootManageSharedAccessKey`.
    """
    default_primary_key: pulumi.Output[str]
    """
    The primary access key for the authorization rule `RootManageSharedAccessKey`.
    """
    default_secondary_connection_string: pulumi.Output[str]
    """
    The secondary connection string for the
    authorization rule `RootManageSharedAccessKey`.
    """
    default_secondary_key: pulumi.Output[str]
    """
    The secondary access key for the authorization rule `RootManageSharedAccessKey`.
    """
    kafka_enabled: pulumi.Output[bool]
    """
    Is Kafka enabled for the EventHub Namespace? Defaults to `false`.
    """
    location: pulumi.Output[str]
    """
    Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
    """
    maximum_throughput_units: pulumi.Output[int]
    """
    Specifies the maximum number of throughput units when Auto Inflate is Enabled. Valid values range from 1 - 20.
    """
    name: pulumi.Output[str]
    """
    Specifies the name of the EventHub Namespace resource. Changing this forces a new resource to be created.
    """
    resource_group_name: pulumi.Output[str]
    """
    The name of the resource group in which to create the namespace. Changing this forces a new resource to be created.
    """
    sku: pulumi.Output[str]
    """
    Defines which tier to use. Valid options are `Basic` and `Standard`.
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    def __init__(__self__, resource_name, opts=None, auto_inflate_enabled=None, capacity=None, kafka_enabled=None, location=None, maximum_throughput_units=None, name=None, resource_group_name=None, sku=None, tags=None, __name__=None, __opts__=None):
        """
        Manage an EventHub Namespace.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] auto_inflate_enabled: Is Auto Inflate enabled for the EventHub Namespace?
        :param pulumi.Input[int] capacity: Specifies the Capacity / Throughput Units for a `Standard` SKU namespace. Valid values range from 1 - 20.
        :param pulumi.Input[bool] kafka_enabled: Is Kafka enabled for the EventHub Namespace? Defaults to `false`.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[int] maximum_throughput_units: Specifies the maximum number of throughput units when Auto Inflate is Enabled. Valid values range from 1 - 20.
        :param pulumi.Input[str] name: Specifies the name of the EventHub Namespace resource. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the namespace. Changing this forces a new resource to be created.
        :param pulumi.Input[str] sku: Defines which tier to use. Valid options are `Basic` and `Standard`.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['auto_inflate_enabled'] = auto_inflate_enabled

        __props__['capacity'] = capacity

        __props__['kafka_enabled'] = kafka_enabled

        if location is None:
            raise TypeError('Missing required property location')
        __props__['location'] = location

        __props__['maximum_throughput_units'] = maximum_throughput_units

        __props__['name'] = name

        if resource_group_name is None:
            raise TypeError('Missing required property resource_group_name')
        __props__['resource_group_name'] = resource_group_name

        if sku is None:
            raise TypeError('Missing required property sku')
        __props__['sku'] = sku

        __props__['tags'] = tags

        __props__['default_primary_connection_string'] = None
        __props__['default_primary_key'] = None
        __props__['default_secondary_connection_string'] = None
        __props__['default_secondary_key'] = None

        super(EventHubNamespace, __self__).__init__(
            'azure:eventhub/eventHubNamespace:EventHubNamespace',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

