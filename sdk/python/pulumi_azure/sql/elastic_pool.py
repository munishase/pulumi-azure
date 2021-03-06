# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class ElasticPool(pulumi.CustomResource):
    creation_date: pulumi.Output[str]
    """
    The creation date of the SQL Elastic Pool.
    """
    db_dtu_max: pulumi.Output[int]
    """
    The maximum DTU which will be guaranteed to all databases in the elastic pool to be created.
    """
    db_dtu_min: pulumi.Output[int]
    """
    The minimum DTU which will be guaranteed to all databases in the elastic pool to be created.
    """
    dtu: pulumi.Output[int]
    """
    The total shared DTU for the elastic pool. Valid values depend on the `edition` which has been defined. Refer to [Azure SQL Database Service Tiers](https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus) for valid combinations.
    """
    edition: pulumi.Output[str]
    """
    The edition of the elastic pool to be created. Valid values are `Basic`, `Standard`, and `Premium`. Refer to [Azure SQL Database Service Tiers](https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus) for details. Changing this forces a new resource to be created.
    """
    location: pulumi.Output[str]
    """
    Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
    """
    name: pulumi.Output[str]
    """
    The name of the elastic pool. This needs to be globally unique. Changing this forces a new resource to be created.
    """
    pool_size: pulumi.Output[int]
    """
    The maximum size in MB that all databases in the elastic pool can grow to. The maximum size must be consistent with combination of `edition` and `dtu` and the limits documented in [Azure SQL Database Service Tiers](https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus). If not defined when creating an elastic pool, the value is set to the size implied by `edition` and `dtu`.
    """
    resource_group_name: pulumi.Output[str]
    """
    The name of the resource group in which to create the elastic pool. This must be the same as the resource group of the underlying SQL server.
    """
    server_name: pulumi.Output[str]
    """
    The name of the SQL Server on which to create the elastic pool. Changing this forces a new resource to be created.
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    def __init__(__self__, resource_name, opts=None, db_dtu_max=None, db_dtu_min=None, dtu=None, edition=None, location=None, name=None, pool_size=None, resource_group_name=None, server_name=None, tags=None, __name__=None, __opts__=None):
        """
        Allows you to manage an Azure SQL Elastic Pool.
        
        > **NOTE:** -  This version of the `Elasticpool` resource is being **deprecated** and should no longer be used. Please use the azurerm_mssql_elasticpool version instead.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] db_dtu_max: The maximum DTU which will be guaranteed to all databases in the elastic pool to be created.
        :param pulumi.Input[int] db_dtu_min: The minimum DTU which will be guaranteed to all databases in the elastic pool to be created.
        :param pulumi.Input[int] dtu: The total shared DTU for the elastic pool. Valid values depend on the `edition` which has been defined. Refer to [Azure SQL Database Service Tiers](https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus) for valid combinations.
        :param pulumi.Input[str] edition: The edition of the elastic pool to be created. Valid values are `Basic`, `Standard`, and `Premium`. Refer to [Azure SQL Database Service Tiers](https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus) for details. Changing this forces a new resource to be created.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the elastic pool. This needs to be globally unique. Changing this forces a new resource to be created.
        :param pulumi.Input[int] pool_size: The maximum size in MB that all databases in the elastic pool can grow to. The maximum size must be consistent with combination of `edition` and `dtu` and the limits documented in [Azure SQL Database Service Tiers](https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus). If not defined when creating an elastic pool, the value is set to the size implied by `edition` and `dtu`.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the elastic pool. This must be the same as the resource group of the underlying SQL server.
        :param pulumi.Input[str] server_name: The name of the SQL Server on which to create the elastic pool. Changing this forces a new resource to be created.
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

        __props__['db_dtu_max'] = db_dtu_max

        __props__['db_dtu_min'] = db_dtu_min

        if dtu is None:
            raise TypeError('Missing required property dtu')
        __props__['dtu'] = dtu

        if edition is None:
            raise TypeError('Missing required property edition')
        __props__['edition'] = edition

        if location is None:
            raise TypeError('Missing required property location')
        __props__['location'] = location

        __props__['name'] = name

        __props__['pool_size'] = pool_size

        if resource_group_name is None:
            raise TypeError('Missing required property resource_group_name')
        __props__['resource_group_name'] = resource_group_name

        if server_name is None:
            raise TypeError('Missing required property server_name')
        __props__['server_name'] = server_name

        __props__['tags'] = tags

        __props__['creation_date'] = None

        super(ElasticPool, __self__).__init__(
            'azure:sql/elasticPool:ElasticPool',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

