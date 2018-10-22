// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this data source to access information about an existing Managed Disk.
func LookupManagedDisk(ctx *pulumi.Context, args *GetManagedDiskArgs) (*GetManagedDiskResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["name"] = args.Name
		inputs["resourceGroupName"] = args.ResourceGroupName
		inputs["tags"] = args.Tags
		inputs["zones"] = args.Zones
	}
	outputs, err := ctx.Invoke("azure:compute/getManagedDisk:getManagedDisk", inputs)
	if err != nil {
		return nil, err
	}
	return &GetManagedDiskResult{
		DiskSizeGb: outputs["diskSizeGb"],
		OsType: outputs["osType"],
		SourceResourceId: outputs["sourceResourceId"],
		SourceUri: outputs["sourceUri"],
		StorageAccountType: outputs["storageAccountType"],
		Tags: outputs["tags"],
		Zones: outputs["zones"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getManagedDisk.
type GetManagedDiskArgs struct {
	// Specifies the name of the Managed Disk.
	Name interface{}
	// Specifies the name of the resource group.
	ResourceGroupName interface{}
	Tags interface{}
	Zones interface{}
}

// A collection of values returned by getManagedDisk.
type GetManagedDiskResult struct {
	// The size of the managed disk in gigabytes.
	DiskSizeGb interface{}
	// The operating system for managed disk. Valid values are `Linux` or `Windows`
	OsType interface{}
	// ID of an existing managed disk that the current resource was created from.
	SourceResourceId interface{}
	// The source URI for the managed disk
	SourceUri interface{}
	// The storage account type for the managed disk.
	StorageAccountType interface{}
	// A mapping of tags assigned to the resource.
	Tags interface{}
	// (Optional) A collection containing the availability zone the managed disk is allocated in.
	Zones interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
