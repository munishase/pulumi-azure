// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this data source to access information about an Image.
func Lookupmage(ctx *pulumi.Context, args *GetImageArgs) (*GetImageResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["name"] = args.Name
		inputs["nameRegex"] = args.NameRegex
		inputs["resourceGroupName"] = args.ResourceGroupName
		inputs["sortDescending"] = args.SortDescending
	}
	outputs, err := ctx.Invoke("azure:compute/getImage:getImage", inputs)
	if err != nil {
		return nil, err
	}
	ret := GetImageResult{}
	if v, ok := outputs["dataDisks"]; ok {
		ret.DataDisks = v
	}
	if v, ok := outputs["location"]; ok {
		ret.Location = v
	}
	if v, ok := outputs["osDisks"]; ok {
		ret.OsDisks = v
	}
	if v, ok := outputs["tags"]; ok {
		ret.Tags = v
	}
	return &ret, nil
}

// A collection of arguments for invoking getImage.
type GetImageArgs struct {
	// The name of the Image.
	Name interface{}
	// Regex pattern of the image to match.
	NameRegex interface{}
	// The Name of the Resource Group where this Image exists.
	ResourceGroupName interface{}
	// By default when matching by regex, images are sorted by name in ascending order and the first match is chosen, to sort descending, set this flag.
	SortDescending interface{}
}

// A collection of values returned by getImage.
type GetImageResult struct {
	// a collection of `data_disk` blocks as defined below.
	DataDisks interface{}
	// the Azure Location where this Image exists.
	Location interface{}
	// a `os_disk` block as defined below.
	OsDisks interface{}
	// a mapping of tags to assigned to the resource.
	Tags interface{}
}