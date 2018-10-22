# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class MetricAlert(pulumi.CustomResource):
    def __init__(__self__, __name__, __opts__=None, actions=None, auto_mitigate=None, criterias=None, description=None, enabled=None, frequency=None, name=None, resource_group_name=None, scopes=None, severity=None, tags=None, window_size=None):
        """Create a MetricAlert resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if actions and not isinstance(actions, list):
            raise TypeError('Expected property actions to be a list')
        __self__.actions = actions
        __props__['actions'] = actions

        if auto_mitigate and not isinstance(auto_mitigate, bool):
            raise TypeError('Expected property auto_mitigate to be a bool')
        __self__.auto_mitigate = auto_mitigate
        __props__['autoMitigate'] = auto_mitigate

        if not criterias:
            raise TypeError('Missing required property criterias')
        elif not isinstance(criterias, list):
            raise TypeError('Expected property criterias to be a list')
        __self__.criterias = criterias
        __props__['criterias'] = criterias

        if description and not isinstance(description, basestring):
            raise TypeError('Expected property description to be a basestring')
        __self__.description = description
        __props__['description'] = description

        if enabled and not isinstance(enabled, bool):
            raise TypeError('Expected property enabled to be a bool')
        __self__.enabled = enabled
        __props__['enabled'] = enabled

        if frequency and not isinstance(frequency, basestring):
            raise TypeError('Expected property frequency to be a basestring')
        __self__.frequency = frequency
        __props__['frequency'] = frequency

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        __props__['name'] = name

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        elif not isinstance(resource_group_name, basestring):
            raise TypeError('Expected property resource_group_name to be a basestring')
        __self__.resource_group_name = resource_group_name
        __props__['resourceGroupName'] = resource_group_name

        if not scopes:
            raise TypeError('Missing required property scopes')
        elif not isinstance(scopes, basestring):
            raise TypeError('Expected property scopes to be a basestring')
        __self__.scopes = scopes
        __props__['scopes'] = scopes

        if severity and not isinstance(severity, int):
            raise TypeError('Expected property severity to be a int')
        __self__.severity = severity
        __props__['severity'] = severity

        if tags and not isinstance(tags, dict):
            raise TypeError('Expected property tags to be a dict')
        __self__.tags = tags
        __props__['tags'] = tags

        if window_size and not isinstance(window_size, basestring):
            raise TypeError('Expected property window_size to be a basestring')
        __self__.window_size = window_size
        __props__['windowSize'] = window_size

        super(MetricAlert, __self__).__init__(
            'azure:monitoring/metricAlert:MetricAlert',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'actions' in outs:
            self.actions = outs['actions']
        if 'autoMitigate' in outs:
            self.auto_mitigate = outs['autoMitigate']
        if 'criterias' in outs:
            self.criterias = outs['criterias']
        if 'description' in outs:
            self.description = outs['description']
        if 'enabled' in outs:
            self.enabled = outs['enabled']
        if 'frequency' in outs:
            self.frequency = outs['frequency']
        if 'name' in outs:
            self.name = outs['name']
        if 'resourceGroupName' in outs:
            self.resource_group_name = outs['resourceGroupName']
        if 'scopes' in outs:
            self.scopes = outs['scopes']
        if 'severity' in outs:
            self.severity = outs['severity']
        if 'tags' in outs:
            self.tags = outs['tags']
        if 'windowSize' in outs:
            self.window_size = outs['windowSize']
