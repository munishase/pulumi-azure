// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Gets information about an existing Service Principal associated with an Application within Azure Active Directory.
 * 
 * > **NOTE:** The Azure Active Directory resources have been split out into [a new AzureAD Provider](http://terraform.io/docs/providers/azuread/index.html) - as such the AzureAD resources within the AzureRM Provider are deprecated and will be removed in the next major version (2.0). Information on how to migrate from the existing resources to the new AzureAD Provider can be found here.
 * 
 * > **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.
 * 
 * ## Example Usage (by Application Display Name)
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 * 
 * const test = pulumi.output(azure.ad.getServicePrincipal({
 *     displayName: "my-awesome-application",
 * }));
 * ```
 * 
 * ## Example Usage (by Application ID)
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 * 
 * const test = pulumi.output(azure.ad.getServicePrincipal({
 *     applicationId: "00000000-0000-0000-0000-000000000000",
 * }));
 * ```
 * 
 * ## Example Usage (by Object ID)
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 * 
 * const test = pulumi.output(azure.ad.getServicePrincipal({
 *     objectId: "00000000-0000-0000-0000-000000000000",
 * }));
 * ```
 */
export function getServicePrincipal(args?: GetServicePrincipalArgs, opts?: pulumi.InvokeOptions): Promise<GetServicePrincipalResult> {
    args = args || {};
    return pulumi.runtime.invoke("azure:ad/getServicePrincipal:getServicePrincipal", {
        "applicationId": args.applicationId,
        "displayName": args.displayName,
        "objectId": args.objectId,
    }, opts);
}

/**
 * A collection of arguments for invoking getServicePrincipal.
 */
export interface GetServicePrincipalArgs {
    /**
     * The ID of the Azure AD Application for which to create a Service Principal.
     */
    readonly applicationId?: string;
    /**
     * The Display Name of the Azure AD Application associated with this Service Principal.
     */
    readonly displayName?: string;
    /**
     * The ID of the Azure AD Service Principal.
     */
    readonly objectId?: string;
}

/**
 * A collection of values returned by getServicePrincipal.
 */
export interface GetServicePrincipalResult {
    readonly applicationId: string;
    readonly displayName: string;
    readonly objectId: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
