// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages an Azure Batch pool.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 * 
 * const azurerm_resource_group_test = new azure.core.ResourceGroup("test", {
 *     location: "%s",
 *     name: "testaccbatch",
 * });
 * const azurerm_storage_account_test = new azure.storage.Account("test", {
 *     accountReplicationType: "LRS",
 *     accountTier: "Standard",
 *     location: azurerm_resource_group_test.location,
 *     name: "testaccsa",
 *     resourceGroupName: azurerm_resource_group_test.name,
 * });
 * const azurerm_batch_account_test = new azure.batch.Account("test", {
 *     location: azurerm_resource_group_test.location,
 *     name: "testaccbatch",
 *     poolAllocationMode: "BatchService",
 *     resourceGroupName: azurerm_resource_group_test.name,
 *     storageAccountId: azurerm_storage_account_test.id,
 *     tags: {
 *         env: "test",
 *     },
 * });
 * const azurerm_batch_pool_test = new azure.batch.Pool("test", {
 *     accountName: azurerm_batch_account_test.name,
 *     autoScale: {
 *         evaluationInterval: "PT15M",
 *         formula: `      startingNumberOfVMs = 1;
 *       maxNumberofVMs = 25;
 *       pendingTaskSamplePercent = $PendingTasks.GetSamplePercent(180 * TimeInterval_Second);
 *       pendingTaskSamples = pendingTaskSamplePercent < 70 ? startingNumberOfVMs : avg($PendingTasks.GetSample(180 *   TimeInterval_Second));
 *       $TargetDedicatedNodes=min(maxNumberofVMs, pendingTaskSamples);
 * `,
 *     },
 *     displayName: "Test Acc Pool Auto",
 *     name: "testaccpool",
 *     nodeAgentSkuId: "batch.node.ubuntu 16.04",
 *     resourceGroupName: azurerm_resource_group_test.name,
 *     startTask: {
 *         commandLine: "echo 'Hello World from $env'",
 *         environment: {
 *             env: "TEST",
 *         },
 *         maxTaskRetryCount: 1,
 *         userIdentity: {
 *             autoUser: {
 *                 elevationLevel: "NonAdmin",
 *                 scope: "Task",
 *             },
 *         },
 *         waitForSuccess: true,
 *     },
 *     storageImageReference: {
 *         offer: "UbuntuServer",
 *         publisher: "Canonical",
 *         sku: "16.04.0-LTS",
 *         version: "latest",
 *     },
 *     vmSize: "Standard_A1",
 * });
 * ```
 */
export class Pool extends pulumi.CustomResource {
    /**
     * Get an existing Pool resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PoolState, opts?: pulumi.CustomResourceOptions): Pool {
        return new Pool(name, <any>state, { ...opts, id: id });
    }

    /**
     * Specifies the name of the Batch account in which the pool will be created. Changing this forces a new resource to be created.
     */
    public readonly accountName: pulumi.Output<string>;
    /**
     * A `auto_scale` block that describes the scale settings when using auto scale.
     */
    public readonly autoScale: pulumi.Output<{ evaluationInterval?: string, formula: string } | undefined>;
    /**
     * Specifies the display name of the Batch pool.
     */
    public readonly displayName: pulumi.Output<string | undefined>;
    /**
     * A `fixed_scale` block that describes the scale settings when using fixed scale.
     */
    public readonly fixedScale: pulumi.Output<{ resizeTimeout?: string, targetDedicatedNodes?: number, targetLowPriorityNodes?: number } | undefined>;
    /**
     * Specifies the name of the Batch pool. Changing this forces a new resource to be created.
     */
    public readonly name: pulumi.Output<string>;
    /**
     * Specifies the Sku of the node agents that will be created in the Batch pool.
     */
    public readonly nodeAgentSkuId: pulumi.Output<string>;
    /**
     * The name of the resource group in which to create the Batch pool. Changing this forces a new resource to be created.
     */
    public readonly resourceGroupName: pulumi.Output<string>;
    /**
     * A `start_task` block that describes the start task settings for the Batch pool.
     */
    public readonly startTask: pulumi.Output<{ commandLine: string, environment?: {[key: string]: any}, maxTaskRetryCount?: number, userIdentity: { autoUser?: { elevationLevel?: string, scope?: string }, userName?: string }, waitForSuccess?: boolean } | undefined>;
    public readonly stopPendingResizeOperation: pulumi.Output<boolean | undefined>;
    /**
     * A `storage_image_reference` for the virtual machines that will compose the Batch pool.
     */
    public readonly storageImageReference: pulumi.Output<{ id?: string, offer: string, publisher: string, sku: string, version: string }>;
    /**
     * Specifies the size of the VM created in the Batch pool.
     */
    public readonly vmSize: pulumi.Output<string>;

    /**
     * Create a Pool resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: PoolArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: PoolArgs | PoolState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: PoolState = argsOrState as PoolState | undefined;
            inputs["accountName"] = state ? state.accountName : undefined;
            inputs["autoScale"] = state ? state.autoScale : undefined;
            inputs["displayName"] = state ? state.displayName : undefined;
            inputs["fixedScale"] = state ? state.fixedScale : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["nodeAgentSkuId"] = state ? state.nodeAgentSkuId : undefined;
            inputs["resourceGroupName"] = state ? state.resourceGroupName : undefined;
            inputs["startTask"] = state ? state.startTask : undefined;
            inputs["stopPendingResizeOperation"] = state ? state.stopPendingResizeOperation : undefined;
            inputs["storageImageReference"] = state ? state.storageImageReference : undefined;
            inputs["vmSize"] = state ? state.vmSize : undefined;
        } else {
            const args = argsOrState as PoolArgs | undefined;
            if (!args || args.accountName === undefined) {
                throw new Error("Missing required property 'accountName'");
            }
            if (!args || args.nodeAgentSkuId === undefined) {
                throw new Error("Missing required property 'nodeAgentSkuId'");
            }
            if (!args || args.resourceGroupName === undefined) {
                throw new Error("Missing required property 'resourceGroupName'");
            }
            if (!args || args.storageImageReference === undefined) {
                throw new Error("Missing required property 'storageImageReference'");
            }
            if (!args || args.vmSize === undefined) {
                throw new Error("Missing required property 'vmSize'");
            }
            inputs["accountName"] = args ? args.accountName : undefined;
            inputs["autoScale"] = args ? args.autoScale : undefined;
            inputs["displayName"] = args ? args.displayName : undefined;
            inputs["fixedScale"] = args ? args.fixedScale : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["nodeAgentSkuId"] = args ? args.nodeAgentSkuId : undefined;
            inputs["resourceGroupName"] = args ? args.resourceGroupName : undefined;
            inputs["startTask"] = args ? args.startTask : undefined;
            inputs["stopPendingResizeOperation"] = args ? args.stopPendingResizeOperation : undefined;
            inputs["storageImageReference"] = args ? args.storageImageReference : undefined;
            inputs["vmSize"] = args ? args.vmSize : undefined;
        }
        super("azure:batch/pool:Pool", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Pool resources.
 */
export interface PoolState {
    /**
     * Specifies the name of the Batch account in which the pool will be created. Changing this forces a new resource to be created.
     */
    readonly accountName?: pulumi.Input<string>;
    /**
     * A `auto_scale` block that describes the scale settings when using auto scale.
     */
    readonly autoScale?: pulumi.Input<{ evaluationInterval?: pulumi.Input<string>, formula: pulumi.Input<string> }>;
    /**
     * Specifies the display name of the Batch pool.
     */
    readonly displayName?: pulumi.Input<string>;
    /**
     * A `fixed_scale` block that describes the scale settings when using fixed scale.
     */
    readonly fixedScale?: pulumi.Input<{ resizeTimeout?: pulumi.Input<string>, targetDedicatedNodes?: pulumi.Input<number>, targetLowPriorityNodes?: pulumi.Input<number> }>;
    /**
     * Specifies the name of the Batch pool. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Specifies the Sku of the node agents that will be created in the Batch pool.
     */
    readonly nodeAgentSkuId?: pulumi.Input<string>;
    /**
     * The name of the resource group in which to create the Batch pool. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName?: pulumi.Input<string>;
    /**
     * A `start_task` block that describes the start task settings for the Batch pool.
     */
    readonly startTask?: pulumi.Input<{ commandLine: pulumi.Input<string>, environment?: pulumi.Input<{[key: string]: any}>, maxTaskRetryCount?: pulumi.Input<number>, userIdentity: pulumi.Input<{ autoUser?: pulumi.Input<{ elevationLevel?: pulumi.Input<string>, scope?: pulumi.Input<string> }>, userName?: pulumi.Input<string> }>, waitForSuccess?: pulumi.Input<boolean> }>;
    readonly stopPendingResizeOperation?: pulumi.Input<boolean>;
    /**
     * A `storage_image_reference` for the virtual machines that will compose the Batch pool.
     */
    readonly storageImageReference?: pulumi.Input<{ id?: pulumi.Input<string>, offer: pulumi.Input<string>, publisher: pulumi.Input<string>, sku: pulumi.Input<string>, version: pulumi.Input<string> }>;
    /**
     * Specifies the size of the VM created in the Batch pool.
     */
    readonly vmSize?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Pool resource.
 */
export interface PoolArgs {
    /**
     * Specifies the name of the Batch account in which the pool will be created. Changing this forces a new resource to be created.
     */
    readonly accountName: pulumi.Input<string>;
    /**
     * A `auto_scale` block that describes the scale settings when using auto scale.
     */
    readonly autoScale?: pulumi.Input<{ evaluationInterval?: pulumi.Input<string>, formula: pulumi.Input<string> }>;
    /**
     * Specifies the display name of the Batch pool.
     */
    readonly displayName?: pulumi.Input<string>;
    /**
     * A `fixed_scale` block that describes the scale settings when using fixed scale.
     */
    readonly fixedScale?: pulumi.Input<{ resizeTimeout?: pulumi.Input<string>, targetDedicatedNodes?: pulumi.Input<number>, targetLowPriorityNodes?: pulumi.Input<number> }>;
    /**
     * Specifies the name of the Batch pool. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Specifies the Sku of the node agents that will be created in the Batch pool.
     */
    readonly nodeAgentSkuId: pulumi.Input<string>;
    /**
     * The name of the resource group in which to create the Batch pool. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName: pulumi.Input<string>;
    /**
     * A `start_task` block that describes the start task settings for the Batch pool.
     */
    readonly startTask?: pulumi.Input<{ commandLine: pulumi.Input<string>, environment?: pulumi.Input<{[key: string]: any}>, maxTaskRetryCount?: pulumi.Input<number>, userIdentity: pulumi.Input<{ autoUser?: pulumi.Input<{ elevationLevel?: pulumi.Input<string>, scope?: pulumi.Input<string> }>, userName?: pulumi.Input<string> }>, waitForSuccess?: pulumi.Input<boolean> }>;
    readonly stopPendingResizeOperation?: pulumi.Input<boolean>;
    /**
     * A `storage_image_reference` for the virtual machines that will compose the Batch pool.
     */
    readonly storageImageReference: pulumi.Input<{ id?: pulumi.Input<string>, offer: pulumi.Input<string>, publisher: pulumi.Input<string>, sku: pulumi.Input<string>, version: pulumi.Input<string> }>;
    /**
     * Specifies the size of the VM created in the Batch pool.
     */
    readonly vmSize: pulumi.Input<string>;
}
