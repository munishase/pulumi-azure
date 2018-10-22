// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package automation

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages a Automation DSC Node Configuration.
type DscNodeConfiguration struct {
	s *pulumi.ResourceState
}

// NewDscNodeConfiguration registers a new resource with the given unique name, arguments, and options.
func NewDscNodeConfiguration(ctx *pulumi.Context,
	name string, args *DscNodeConfigurationArgs, opts ...pulumi.ResourceOpt) (*DscNodeConfiguration, error) {
	if args == nil || args.AutomationAccountName == nil {
		return nil, errors.New("missing required argument 'AutomationAccountName'")
	}
	if args == nil || args.ContentEmbedded == nil {
		return nil, errors.New("missing required argument 'ContentEmbedded'")
	}
	if args == nil || args.ResourceGroupName == nil {
		return nil, errors.New("missing required argument 'ResourceGroupName'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["automationAccountName"] = nil
		inputs["contentEmbedded"] = nil
		inputs["name"] = nil
		inputs["resourceGroupName"] = nil
	} else {
		inputs["automationAccountName"] = args.AutomationAccountName
		inputs["contentEmbedded"] = args.ContentEmbedded
		inputs["name"] = args.Name
		inputs["resourceGroupName"] = args.ResourceGroupName
	}
	inputs["configurationName"] = nil
	s, err := ctx.RegisterResource("azure:automation/dscNodeConfiguration:DscNodeConfiguration", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &DscNodeConfiguration{s: s}, nil
}

// GetDscNodeConfiguration gets an existing DscNodeConfiguration resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDscNodeConfiguration(ctx *pulumi.Context,
	name string, id pulumi.ID, state *DscNodeConfigurationState, opts ...pulumi.ResourceOpt) (*DscNodeConfiguration, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["automationAccountName"] = state.AutomationAccountName
		inputs["configurationName"] = state.ConfigurationName
		inputs["contentEmbedded"] = state.ContentEmbedded
		inputs["name"] = state.Name
		inputs["resourceGroupName"] = state.ResourceGroupName
	}
	s, err := ctx.ReadResource("azure:automation/dscNodeConfiguration:DscNodeConfiguration", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &DscNodeConfiguration{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *DscNodeConfiguration) URN() *pulumi.URNOutput {
	return r.s.URN
}

// ID is this resource's unique identifier assigned by its provider.
func (r *DscNodeConfiguration) ID() *pulumi.IDOutput {
	return r.s.ID
}

// The name of the automation account in which the DSC Node Configuration is created. Changing this forces a new resource to be created.
func (r *DscNodeConfiguration) AutomationAccountName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["automationAccountName"])
}

func (r *DscNodeConfiguration) ConfigurationName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["configurationName"])
}

// The PowerShell DSC Node Configuration (mof content).
func (r *DscNodeConfiguration) ContentEmbedded() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["contentEmbedded"])
}

// Specifies the name of the DSC Node Configuration. Changing this forces a new resource to be created.
func (r *DscNodeConfiguration) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The name of the resource group in which the DSC Node Configuration is created. Changing this forces a new resource to be created.
func (r *DscNodeConfiguration) ResourceGroupName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["resourceGroupName"])
}

// Input properties used for looking up and filtering DscNodeConfiguration resources.
type DscNodeConfigurationState struct {
	// The name of the automation account in which the DSC Node Configuration is created. Changing this forces a new resource to be created.
	AutomationAccountName interface{}
	ConfigurationName interface{}
	// The PowerShell DSC Node Configuration (mof content).
	ContentEmbedded interface{}
	// Specifies the name of the DSC Node Configuration. Changing this forces a new resource to be created.
	Name interface{}
	// The name of the resource group in which the DSC Node Configuration is created. Changing this forces a new resource to be created.
	ResourceGroupName interface{}
}

// The set of arguments for constructing a DscNodeConfiguration resource.
type DscNodeConfigurationArgs struct {
	// The name of the automation account in which the DSC Node Configuration is created. Changing this forces a new resource to be created.
	AutomationAccountName interface{}
	// The PowerShell DSC Node Configuration (mof content).
	ContentEmbedded interface{}
	// Specifies the name of the DSC Node Configuration. Changing this forces a new resource to be created.
	Name interface{}
	// The name of the resource group in which the DSC Node Configuration is created. Changing this forces a new resource to be created.
	ResourceGroupName interface{}
}
