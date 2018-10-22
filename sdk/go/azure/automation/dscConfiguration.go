// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package automation

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages a Automation DSC Configuration.
type DscConfiguration struct {
	s *pulumi.ResourceState
}

// NewDscConfiguration registers a new resource with the given unique name, arguments, and options.
func NewDscConfiguration(ctx *pulumi.Context,
	name string, args *DscConfigurationArgs, opts ...pulumi.ResourceOpt) (*DscConfiguration, error) {
	if args == nil || args.AutomationAccountName == nil {
		return nil, errors.New("missing required argument 'AutomationAccountName'")
	}
	if args == nil || args.ContentEmbedded == nil {
		return nil, errors.New("missing required argument 'ContentEmbedded'")
	}
	if args == nil || args.Location == nil {
		return nil, errors.New("missing required argument 'Location'")
	}
	if args == nil || args.ResourceGroupName == nil {
		return nil, errors.New("missing required argument 'ResourceGroupName'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["automationAccountName"] = nil
		inputs["contentEmbedded"] = nil
		inputs["description"] = nil
		inputs["location"] = nil
		inputs["logVerbose"] = nil
		inputs["name"] = nil
		inputs["resourceGroupName"] = nil
	} else {
		inputs["automationAccountName"] = args.AutomationAccountName
		inputs["contentEmbedded"] = args.ContentEmbedded
		inputs["description"] = args.Description
		inputs["location"] = args.Location
		inputs["logVerbose"] = args.LogVerbose
		inputs["name"] = args.Name
		inputs["resourceGroupName"] = args.ResourceGroupName
	}
	inputs["state"] = nil
	s, err := ctx.RegisterResource("azure:automation/dscConfiguration:DscConfiguration", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &DscConfiguration{s: s}, nil
}

// GetDscConfiguration gets an existing DscConfiguration resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDscConfiguration(ctx *pulumi.Context,
	name string, id pulumi.ID, state *DscConfigurationState, opts ...pulumi.ResourceOpt) (*DscConfiguration, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["automationAccountName"] = state.AutomationAccountName
		inputs["contentEmbedded"] = state.ContentEmbedded
		inputs["description"] = state.Description
		inputs["location"] = state.Location
		inputs["logVerbose"] = state.LogVerbose
		inputs["name"] = state.Name
		inputs["resourceGroupName"] = state.ResourceGroupName
		inputs["state"] = state.State
	}
	s, err := ctx.ReadResource("azure:automation/dscConfiguration:DscConfiguration", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &DscConfiguration{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *DscConfiguration) URN() *pulumi.URNOutput {
	return r.s.URN
}

// ID is this resource's unique identifier assigned by its provider.
func (r *DscConfiguration) ID() *pulumi.IDOutput {
	return r.s.ID
}

// The name of the automation account in which the DSC Configuration is created. Changing this forces a new resource to be created.
func (r *DscConfiguration) AutomationAccountName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["automationAccountName"])
}

// The PowerShell DSC Configuration script.
func (r *DscConfiguration) ContentEmbedded() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["contentEmbedded"])
}

// Description to go with DSC Configuration.
func (r *DscConfiguration) Description() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["description"])
}

// Must be the same location as the Automation Account.
func (r *DscConfiguration) Location() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["location"])
}

// Verbose log option.
func (r *DscConfiguration) LogVerbose() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["logVerbose"])
}

// Specifies the name of the DSC Configuration. Changing this forces a new resource to be created.
func (r *DscConfiguration) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The name of the resource group in which the DSC Configuration is created. Changing this forces a new resource to be created.
func (r *DscConfiguration) ResourceGroupName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["resourceGroupName"])
}

func (r *DscConfiguration) State() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["state"])
}

// Input properties used for looking up and filtering DscConfiguration resources.
type DscConfigurationState struct {
	// The name of the automation account in which the DSC Configuration is created. Changing this forces a new resource to be created.
	AutomationAccountName interface{}
	// The PowerShell DSC Configuration script.
	ContentEmbedded interface{}
	// Description to go with DSC Configuration.
	Description interface{}
	// Must be the same location as the Automation Account.
	Location interface{}
	// Verbose log option.
	LogVerbose interface{}
	// Specifies the name of the DSC Configuration. Changing this forces a new resource to be created.
	Name interface{}
	// The name of the resource group in which the DSC Configuration is created. Changing this forces a new resource to be created.
	ResourceGroupName interface{}
	State interface{}
}

// The set of arguments for constructing a DscConfiguration resource.
type DscConfigurationArgs struct {
	// The name of the automation account in which the DSC Configuration is created. Changing this forces a new resource to be created.
	AutomationAccountName interface{}
	// The PowerShell DSC Configuration script.
	ContentEmbedded interface{}
	// Description to go with DSC Configuration.
	Description interface{}
	// Must be the same location as the Automation Account.
	Location interface{}
	// Verbose log option.
	LogVerbose interface{}
	// Specifies the name of the DSC Configuration. Changing this forces a new resource to be created.
	Name interface{}
	// The name of the resource group in which the DSC Configuration is created. Changing this forces a new resource to be created.
	ResourceGroupName interface{}
}
