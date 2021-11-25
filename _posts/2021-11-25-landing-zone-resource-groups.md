---
title: "Azure Bicep Landing Zone Series - Resource Groups"
categories:
  - blog
tags:
  - Bicep
  - Azure
  - Design
  - Architecture
---

Welcome to this blog series. This blog series will help you build your Infrastructure as Code landing zone using Bicep. It is your choice how to deploy it. In my examples I will use Azure PowerShell or Azure CLI but feel free to execute the deployment using Azure DevOps or maybe even GitHub Actions.

## Intro

In order to follow this blog series and learn how to hopefully design, create and deploy your own or customers landing zone I recommend the following software & tools installed on your computer before continuing.

* Visual Studio code with the Bicep (and possibly ARM tools for debugging any issues) extension installed.
* Latest Azure PowerShell and/or Azure CLI installed.

And of course at least one Azure subscription with appropriate permissions to create resources, apply policies and assign roles.

Now.. to get started. In this first blog we will create our initial main.bicep file and start to create the groundwork to get something that'll look like a HUB environment.

### Starting with bicep

Start by creating a main.bicep file. In my example I will target the deployment on subscription level, so we set the targetScope to 'Subscription' on top of the file. More info about Bicep's deployment scopes [here](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-to-subscription?tabs=azure-cli){:target="_blank"}.

<script src="https://gist.github.com/rbnmk/2970ab025c269b1356f00e922bf0babf.js?file=1-targetScope-example.bicep"></script>

Next step is to create two starting parameters. I have hardcoded both values, but later in this series we will provide them upon execution of the template to make sure we target the appropriate environment. More info about different type of parameters can be found [here](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/parameters){:target="_blank"}.

<script src="https://gist.github.com/rbnmk/2970ab025c269b1356f00e922bf0babf.js?file=2-parameters-example.bicep"></script>

In the next step we will create a new variable that will contain environment specific configuration settings, which will be a mix of objects & arrays, so make sure to properly define them.

In the example below I create the variable **`envConfig`** and define a object, within this initial object I create the **`hub`** configuration. Inside this object all required or related configuration for the hub will be defined. More info about this can be found on the [docs](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/variables){:target="_blank"}.

Feel free to change as you like or according to your naming convention!

<script src="https://gist.github.com/rbnmk/2970ab025c269b1356f00e922bf0babf.js?file=3-variables-env-config-example.bicep"></script>

Next step is to define our first resource deployment, which will be Resource Groups, because we need at least one to start deploying resources.

Example below: iterating over the **`envConfig[environment].resourceGroups`** array. If you want to learn more about loops, please visit the documentation via this link: [Bicep loops](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/loops){:target="_blank"}.

### Example (Iterating over our earlier created variable array)

<script src="https://gist.github.com/rbnmk/2970ab025c269b1356f00e922bf0babf.js?file=resource-example-2.bicep"></script>

### Deploy the main.bicep file

To deploy the resource groups to a certain subscription make sure your are logged in using `az login`. If you are logged in already make sure you are in the right subscription context by running `az account show`. You can switch subscriptions with `az account set --subscription <000-000-000>`

Or you can use PowerShel: `Connect-AzAccount -SubscriptionId <000-000-000>`

Now to deploy the file you can run the following command:

#### Deployment with either Azure CLI or Azure PowerShell

``` bash
az deployment sub create `
    --template-file .\main.bicep `
    --location WestEurope
```

``` PowerShell
New-AzDeployment -Name BlogExample ` 
    -TemplateFile .\main.bicep `
    -Location WestEurope
```
