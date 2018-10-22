// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package network

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this data source to access information about an existing Route Table.
func LookupRouteTable(ctx *pulumi.Context, args *GetRouteTableArgs) (*GetRouteTableResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["name"] = args.Name
		inputs["resourceGroupName"] = args.ResourceGroupName
	}
	outputs, err := ctx.Invoke("azure:network/getRouteTable:getRouteTable", inputs)
	if err != nil {
		return nil, err
	}
	return &GetRouteTableResult{
		Location: outputs["location"],
		Routes: outputs["routes"],
		Subnets: outputs["subnets"],
		Tags: outputs["tags"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getRouteTable.
type GetRouteTableArgs struct {
	// The name of the Route Table.
	Name interface{}
	// The name of the Resource Group in which the Route Table exists.
	ResourceGroupName interface{}
}

// A collection of values returned by getRouteTable.
type GetRouteTableResult struct {
	// The Azure Region in which the Route Table exists.
	Location interface{}
	// One or more `route` blocks as documented below.
	Routes interface{}
	// The collection of Subnets associated with this route table.
	Subnets interface{}
	// A mapping of tags assigned to the Route Table.
	Tags interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
