// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this data source to access information about an existing Management Group.
 */
export function getManagementGroup(args: GetManagementGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetManagementGroupResult> {
    return pulumi.runtime.invoke("azure:managementgroups/getManagementGroup:getManagementGroup", {
        "groupId": args.groupId,
    }, opts);
}

/**
 * A collection of arguments for invoking getManagementGroup.
 */
export interface GetManagementGroupArgs {
    /**
     * Specifies the UUID of this Management Group.
     */
    readonly groupId: string;
}

/**
 * A collection of values returned by getManagementGroup.
 */
export interface GetManagementGroupResult {
    /**
     * A friendly name for the Management Group.
     */
    readonly displayName: string;
    /**
     * The ID of any Parent Management Group.
     */
    readonly parentManagementGroupId: string;
    /**
     * A list of Subscription ID's which are assigned to the Management Group.
     */
    readonly subscriptionIds: string[];
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
