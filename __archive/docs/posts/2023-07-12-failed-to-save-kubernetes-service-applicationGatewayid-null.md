---
date: 
  created: 2023-07-12 08:00:00
authors: 
  - rbnmk
categories:
  - Azure
tags:
  - Azure
  - AzureKubernetes
  - AKS
  - ApplicationGatewayAKSAddon
  - ApplicationGateway
authors:
  - rbnmk
comments: true
---

# Failed to save Kubernetes service - addonProfiles.ingressApplicationGateway.config.applicationGatewayId is invalid

I ran into an issue when deploying Azure Kubernetes services using ARM Templates. We previously set the ingress-agw addon to configure the ingress using an application gateway. We recently moved to the Azure Application Gateway Ingress Controller using Helm and simply set the addon configuration to 'null' but that creates a conflict when making other changes such as changing the SKU (Pricing Tier) of the cluster.

<!-- more -->

We noticed that our clusters were set to the Free SKU but we are actually deploying with the Standard SKU. When we tried to change the SKU in the portal we got the following error:

![AKS Error 1](../assets/images/aks_error_1.png)

Error description in text:

Failed to save Kubernetes service. Error: Property id '' at path 'properties.addonProfiles.ingressApplicationGateway.config.applicationGatewayId' is invalid. Expect fully qualified resource Id that start with '/subscriptions/{subscriptionId}' or '/providers/{resourceProviderNamespace}/'
{: .notice--warning}

## The solution

[This Github issue](https://github.com/Azure/azure-cli/issues/24971){:target="_blank"} actually pointed me in the right direction after I tried removing the addon from the ARM-template didnt fix it.

For this solution I used Azure CLI (PowerShell) and the AKS-preview addon. Make sure you set your az cli context to the subscription where your AKS-cluster is created.

Please check carefully if you can run this command against your environment before executing!
{: .notice--warning}

## (Optional) Set the subscription context

```PowerShell
$aksSubscriptionName = "aksSubscription"
az account set --subscription $aksSubscriptionName
```

## Disable the add-on

```PowerShell
$aksName = "aks"
$aksRgName = "aksrg"
az aks disable-addons --addon 'ingress-appgw' --resource-group $aksRgName -n $aksName
```

## Update the cluster SKU

I still could not update the SKU using my ARM-template so I used Azure CLI to configure (update the sku) for my AKS-cluster.

```PowerShell
$aksName = "aks"
$aksRgName = "aksrg"
az aks update --resource-group $aksRgName -n $aksName --tier 'Standard'
```

Now verify if the cluster is set to the Standard SKU:

![AKS Standard SKU](../assets/images/aks_sku_standard.png)

I also checked if the SKU is set correctly after an ARM-template deployment. It was not reset to Free so I think it's all good now. I hope that Microsoft Azure will provide better error messages in the future for these kind of issues.

That's it for today, hope it helped you out - would be happy to know if it helped you (or not)!