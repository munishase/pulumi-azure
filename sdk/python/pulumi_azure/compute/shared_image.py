# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class SharedImage(pulumi.CustomResource):
    """
    Manages a Shared Image within a Shared Image Gallery.
    
    -> **NOTE** Shared Image Galleries are currently in Public Preview. You can find more information, including [how to register for the Public Preview here](https://azure.microsoft.com/en-gb/blog/announcing-the-public-preview-of-shared-image-gallery/).
    """
    def __init__(__self__, __name__, __opts__=None, description=None, eula=None, gallery_name=None, identifier=None, location=None, name=None, os_type=None, privacy_statement_uri=None, release_note_uri=None, resource_group_name=None, tags=None):
        """Create a SharedImage resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if description and not isinstance(description, basestring):
            raise TypeError('Expected property description to be a basestring')
        __self__.description = description
        """
        A description of this Shared Image.
        """
        __props__['description'] = description

        if eula and not isinstance(eula, basestring):
            raise TypeError('Expected property eula to be a basestring')
        __self__.eula = eula
        """
        The End User Licence Agreement for the Shared Image.
        """
        __props__['eula'] = eula

        if not gallery_name:
            raise TypeError('Missing required property gallery_name')
        elif not isinstance(gallery_name, basestring):
            raise TypeError('Expected property gallery_name to be a basestring')
        __self__.gallery_name = gallery_name
        """
        Specifies the name of the Shared Image Gallery in which this Shared Image should exist. Changing this forces a new resource to be created.
        """
        __props__['galleryName'] = gallery_name

        if not identifier:
            raise TypeError('Missing required property identifier')
        elif not isinstance(identifier, dict):
            raise TypeError('Expected property identifier to be a dict')
        __self__.identifier = identifier
        __props__['identifier'] = identifier

        if not location:
            raise TypeError('Missing required property location')
        elif not isinstance(location, basestring):
            raise TypeError('Expected property location to be a basestring')
        __self__.location = location
        """
        Specifies the supported Azure location where the Shared Image Gallery exists. Changing this forces a new resource to be created.
        """
        __props__['location'] = location

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        Specifies the name of the Shared Image. Changing this forces a new resource to be created.
        """
        __props__['name'] = name

        if not os_type:
            raise TypeError('Missing required property os_type')
        elif not isinstance(os_type, basestring):
            raise TypeError('Expected property os_type to be a basestring')
        __self__.os_type = os_type
        """
        The type of Operating System present in this Shared Image. Possible values are `Linux` and `Windows`.
        """
        __props__['osType'] = os_type

        if privacy_statement_uri and not isinstance(privacy_statement_uri, basestring):
            raise TypeError('Expected property privacy_statement_uri to be a basestring')
        __self__.privacy_statement_uri = privacy_statement_uri
        """
        The URI containing the Privacy Statement associated with this Shared Image.
        """
        __props__['privacyStatementUri'] = privacy_statement_uri

        if release_note_uri and not isinstance(release_note_uri, basestring):
            raise TypeError('Expected property release_note_uri to be a basestring')
        __self__.release_note_uri = release_note_uri
        """
        The URI containing the Release Notes associated with this Shared Image.
        """
        __props__['releaseNoteUri'] = release_note_uri

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        elif not isinstance(resource_group_name, basestring):
            raise TypeError('Expected property resource_group_name to be a basestring')
        __self__.resource_group_name = resource_group_name
        """
        The name of the resource group in which the Shared Image Gallery exists. Changing this forces a new resource to be created.
        """
        __props__['resourceGroupName'] = resource_group_name

        if tags and not isinstance(tags, dict):
            raise TypeError('Expected property tags to be a dict')
        __self__.tags = tags
        """
        A mapping of tags to assign to the Shared Image.
        """
        __props__['tags'] = tags

        super(SharedImage, __self__).__init__(
            'azure:compute/sharedImage:SharedImage',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'description' in outs:
            self.description = outs['description']
        if 'eula' in outs:
            self.eula = outs['eula']
        if 'galleryName' in outs:
            self.gallery_name = outs['galleryName']
        if 'identifier' in outs:
            self.identifier = outs['identifier']
        if 'location' in outs:
            self.location = outs['location']
        if 'name' in outs:
            self.name = outs['name']
        if 'osType' in outs:
            self.os_type = outs['osType']
        if 'privacyStatementUri' in outs:
            self.privacy_statement_uri = outs['privacyStatementUri']
        if 'releaseNoteUri' in outs:
            self.release_note_uri = outs['releaseNoteUri']
        if 'resourceGroupName' in outs:
            self.resource_group_name = outs['resourceGroupName']
        if 'tags' in outs:
            self.tags = outs['tags']