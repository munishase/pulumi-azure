# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class KeyVault(pulumi.CustomResource):
    """
    Manages a Key Vault.
    
    ~> **NOTE:** It's possible to define Key Vault Access Policies both within the `azurerm_key_vault` resource via the `access_policy` block and by using the `azurerm_key_vault_access_policy` resource. However it's not possible to use both methods to manage Access Policies within a KeyVault, since there'll be conflicts.
    """
    def __init__(__self__, __name__, __opts__=None, access_policies=None, enabled_for_deployment=None, enabled_for_disk_encryption=None, enabled_for_template_deployment=None, location=None, name=None, network_acls=None, resource_group_name=None, sku=None, tags=None, tenant_id=None):
        """Create a KeyVault resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if access_policies and not isinstance(access_policies, list):
            raise TypeError('Expected property access_policies to be a list')
        __self__.access_policies = access_policies
        """
        An access policy block as described below. A maximum of 16 may be declared.
        """
        __props__['accessPolicies'] = access_policies

        if enabled_for_deployment and not isinstance(enabled_for_deployment, bool):
            raise TypeError('Expected property enabled_for_deployment to be a bool')
        __self__.enabled_for_deployment = enabled_for_deployment
        """
        Boolean flag to specify whether Azure Virtual Machines are permitted to retrieve certificates stored as secrets from the key vault. Defaults to `false`.
        """
        __props__['enabledForDeployment'] = enabled_for_deployment

        if enabled_for_disk_encryption and not isinstance(enabled_for_disk_encryption, bool):
            raise TypeError('Expected property enabled_for_disk_encryption to be a bool')
        __self__.enabled_for_disk_encryption = enabled_for_disk_encryption
        """
        Boolean flag to specify whether Azure Disk Encryption is permitted to retrieve secrets from the vault and unwrap keys. Defaults to `false`.
        """
        __props__['enabledForDiskEncryption'] = enabled_for_disk_encryption

        if enabled_for_template_deployment and not isinstance(enabled_for_template_deployment, bool):
            raise TypeError('Expected property enabled_for_template_deployment to be a bool')
        __self__.enabled_for_template_deployment = enabled_for_template_deployment
        """
        Boolean flag to specify whether Azure Resource Manager is permitted to retrieve secrets from the key vault. Defaults to `false`.
        """
        __props__['enabledForTemplateDeployment'] = enabled_for_template_deployment

        if not location:
            raise TypeError('Missing required property location')
        elif not isinstance(location, basestring):
            raise TypeError('Expected property location to be a basestring')
        __self__.location = location
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        __props__['location'] = location

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        Specifies the name of the Key Vault. Changing this forces a new resource to be created.
        """
        __props__['name'] = name

        if network_acls and not isinstance(network_acls, dict):
            raise TypeError('Expected property network_acls to be a dict')
        __self__.network_acls = network_acls
        """
        A `network_acls` block as defined below.
        """
        __props__['networkAcls'] = network_acls

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        elif not isinstance(resource_group_name, basestring):
            raise TypeError('Expected property resource_group_name to be a basestring')
        __self__.resource_group_name = resource_group_name
        """
        The name of the resource group in which to create the Key Vault. Changing this forces a new resource to be created.
        """
        __props__['resourceGroupName'] = resource_group_name

        if not sku:
            raise TypeError('Missing required property sku')
        elif not isinstance(sku, dict):
            raise TypeError('Expected property sku to be a dict')
        __self__.sku = sku
        """
        An SKU block as described below.
        """
        __props__['sku'] = sku

        if tags and not isinstance(tags, dict):
            raise TypeError('Expected property tags to be a dict')
        __self__.tags = tags
        """
        A mapping of tags to assign to the resource.
        """
        __props__['tags'] = tags

        if not tenant_id:
            raise TypeError('Missing required property tenant_id')
        elif not isinstance(tenant_id, basestring):
            raise TypeError('Expected property tenant_id to be a basestring')
        __self__.tenant_id = tenant_id
        """
        The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault.
        """
        __props__['tenantId'] = tenant_id

        __self__.vault_uri = pulumi.runtime.UNKNOWN
        """
        The URI of the Key Vault, used for performing operations on keys and secrets.
        """

        super(KeyVault, __self__).__init__(
            'azure:keyvault/keyVault:KeyVault',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'accessPolicies' in outs:
            self.access_policies = outs['accessPolicies']
        if 'enabledForDeployment' in outs:
            self.enabled_for_deployment = outs['enabledForDeployment']
        if 'enabledForDiskEncryption' in outs:
            self.enabled_for_disk_encryption = outs['enabledForDiskEncryption']
        if 'enabledForTemplateDeployment' in outs:
            self.enabled_for_template_deployment = outs['enabledForTemplateDeployment']
        if 'location' in outs:
            self.location = outs['location']
        if 'name' in outs:
            self.name = outs['name']
        if 'networkAcls' in outs:
            self.network_acls = outs['networkAcls']
        if 'resourceGroupName' in outs:
            self.resource_group_name = outs['resourceGroupName']
        if 'sku' in outs:
            self.sku = outs['sku']
        if 'tags' in outs:
            self.tags = outs['tags']
        if 'tenantId' in outs:
            self.tenant_id = outs['tenantId']
        if 'vaultUri' in outs:
            self.vault_uri = outs['vaultUri']
