// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package containerservice

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this data source to access information about an existing Container Registry.
func LookupRegistry(ctx *pulumi.Context, args *GetRegistryArgs) (*GetRegistryResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["name"] = args.Name
		inputs["resourceGroupName"] = args.ResourceGroupName
	}
	outputs, err := ctx.Invoke("azure:containerservice/getRegistry:getRegistry", inputs)
	if err != nil {
		return nil, err
	}
	return &GetRegistryResult{
		AdminEnabled: outputs["adminEnabled"],
		AdminPassword: outputs["adminPassword"],
		AdminUsername: outputs["adminUsername"],
		Location: outputs["location"],
		LoginServer: outputs["loginServer"],
		Sku: outputs["sku"],
		StorageAccountId: outputs["storageAccountId"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getRegistry.
type GetRegistryArgs struct {
	// The name of the Container Registry.
	Name interface{}
	// The Name of the Resource Group where this Container Registry exists.
	ResourceGroupName interface{}
}

// A collection of values returned by getRegistry.
type GetRegistryResult struct {
	// Is the Administrator account enabled for this Container Registry.
	AdminEnabled interface{}
	// The Password associated with the Container Registry Admin account - if the admin account is enabled.
	AdminPassword interface{}
	// The Username associated with the Container Registry Admin account - if the admin account is enabled.
	AdminUsername interface{}
	// The Azure Region in which this Container Registry exists.
	Location interface{}
	// The URL that can be used to log into the container registry.
	LoginServer interface{}
	// The SKU of this Container Registry, such as `Basic`.
	Sku interface{}
	// The ID of the Storage Account used for this Container Registry. This is only returned for `Classic` SKU's.
	StorageAccountId interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
