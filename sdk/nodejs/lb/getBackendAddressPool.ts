// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this data source to access information about an existing Load Balancer Backend Address Pool.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 * 
 * const testLB = pulumi.output(azure.lb.getLB({
 *     name: "example-lb",
 *     resourceGroupName: "example-resources",
 * }));
 * const testBackendAddressPool = pulumi.output(azure.lb.getBackendAddressPool({
 *     loadbalancerId: testLB.apply(testLB => testLB.id),
 *     name: "first",
 * }));
 * 
 * export const backendAddressPoolId = testBackendAddressPool.apply(testBackendAddressPool => testBackendAddressPool.id);
 * ```
 */
export function getBackendAddressPool(args: GetBackendAddressPoolArgs, opts?: pulumi.InvokeOptions): Promise<GetBackendAddressPoolResult> {
    return pulumi.runtime.invoke("azure:lb/getBackendAddressPool:getBackendAddressPool", {
        "loadbalancerId": args.loadbalancerId,
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getBackendAddressPool.
 */
export interface GetBackendAddressPoolArgs {
    /**
     * The ID of the Load Balancer in which the Backend Address Pool exists.
     */
    readonly loadbalancerId: string;
    /**
     * Specifies the name of the Backend Address Pool.
     */
    readonly name: string;
}

/**
 * A collection of values returned by getBackendAddressPool.
 */
export interface GetBackendAddressPoolResult {
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
