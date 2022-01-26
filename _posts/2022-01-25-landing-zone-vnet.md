---
title: "Azure Bicep Landing Zone Series - Hub Virtual Network"
date: 2022-01-27 08:00:00
header:
  og_image: "assets/images/BicepLogoImage.png"
  teaser: "assets/images/BicepLogoImage.png"
categories:
  - blog
tags:
  - Bicep
  - Azure
  - Design
  - Architecture
---

Welcome to this blog series. To follow the steps in this blog I recommend checking out my [previous blog]({ % post_url /blog/2022-01-06-landing-zone-tags %}){:target="_blank"} or [start here.]({% post_url 2022-01-01-landing-zone-resource-groups %}){:target="_blank"} This blog series will help you build your Infrastructure as Code landing zone using Bicep. It is your choice how to deploy it. In my examples I will use Azure PowerShell or Azure CLI but feel free to execute the deployment using Azure DevOps or maybe even GitHub Actions.

The latest version of the entire landing zone code can be found in my [GitHub repository](https://github.com/rbnmk/bicep-build-your-landing-zone){:target="_blank"}, created specifically for this blog series.

## Intro

In the [previous blog]({% post_url /blog/2022-01-06-landing-zone-tags %}){:target="_blank"} we added tags to our resource groups. In this blog we will start with creating an important resource, the virtual network. In my scenario it will be the network for the HUB environment, which could contain (in a real scenario) for example a firewall, virtual network gateway, application gateway or maybe identity services like Active Directory. At this moment we will simply lay some groundwork for these services to be able to land in this virtual network.

Important to know is that a virtual network in Bicep consists of several components but the main components are the virtual network itself and which subnets it contains. While subnets can be deployed independently from the VNET I strongly recommend always deploying the VNET with all required subnets and add new subnets to the existing deployment if required, otherwise you'll run into issues while deploying. Some of these issues are described [here](https://github.com/Azure/azure-quickstart-templates/issues/2786) and [here](https://docs.microsoft.com/en-us/azure/azure-resource-manager/templates/deployment-modes#incremental-mode).
{: .notice--warning}

## The VNET object

We will define the configuration for the VNET, Subnet and NSG's in one object that will contain several layers of configuration. I will dig a little bit deeper into the resources below.

## Network Security Groups

It is recommended to use a network security group for every subnet. This will be the first layer of protection of the devices connected to your subnet(s). I have created a module that can deploy a Network Security Group by providing the following parameters. These values will be available in the final envConfig object!

* Network Security Group name
* Network Security Group rules
  * In this parameter you will define the rules that make up your NSG.
* Network Security Group ruleset
  * This parameter helps out if you want to deploy some of the required rules for example when you want to deploy an Azure Bastion host. These rules cannot always be found easily so I made this to help me out on the various deployments I work on most often.
  * Note: This is not something that is available out of the box, this is my idea and I just want to share this to you! {: .notice--warning}

## Create the VNET configuration

We will start by adding the minimal required details for a virtual network. For that we need an address space, for this example I will use the following config, for now we will deploy a single subnet which will be used for a [Bastion Host](https://docs.microsoft.com/en-us/azure/bastion/bastion-overview){:target="_blank"}:

* VNET Name: hub-vnet-1
* VNET Address space: 10.0.42.0/23
* Subnet Name: AzureBastionSubnet (This name is required for Azure Bastion to work!)
* Subnet Address space: 10.0.42/25
* Subnet NSG Name: hub-nsg-bastion
* Subnet NSG Security Rules: Allow SSH (tcp/22) and RDP (tcp/3389) to the Virtual Network service tag, which basically means to all resources connected to this VNET (including peered VNETs).
* Subnet NSG RuleSet: bastion

## Updating the configuration

Adding the above configuration to the envConfig variable will look like this, if you look closely you will notice I have added an virtualNetworks array([]), which can contain one to many virtual networks, in this example we will configure just one VNET:

<script src="https://gist.github.com/rbnmk/11e6175b7765e870be4eb53ef50eb6eb.js?file=envConfig.bicep"></script>

## Adding the modules and executing them in the correct order

If you don't know what Bicep modules are I recommend reading [the documentation](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/modules) before continuing. In short: modules are basically pre-defined bicep templates that you might want to re-use throughout your deployments to maintain consistency and have a default way of deploying certain (parts) of the environment.
{: .notice--info}

In the repository I have created a folder called '**modules**', which we will continue to use throughout the course of these series. In this folder I have created 3 module files:

* [network.bicep](https://gist.github.com/rbnmk/11e6175b7765e870be4eb53ef50eb6eb#file-network-bicep){:target="_blank"}: Wrapper around the NSG and VNET modules. This helps with NSG's being created before the VNET is deployed. Some values need to 'exist' before we can reference them, therefore it is set up this way.
* [nsg.bicep](https://gist.github.com/rbnmk/11e6175b7765e870be4eb53ef50eb6eb#file-nsg-bicep){:target="_blank"}: Simple module that will deploy an NSG.
* [vnet.bicep](https://gist.github.com/rbnmk/11e6175b7765e870be4eb53ef50eb6eb#file-vnet-bicep){:target="_blank"}: Module that will deploy an VNET with subnets and attaches NSG's if provided.

## Using the bicep modules

In the main.bicep we will add another snippet as shown below.

* We will only call the [network.bicep](https://gist.github.com/rbnmk/11e6175b7765e870be4eb53ef50eb6eb#file-network-bicep){:target="_blank"} module, which will receive our Virtual Network (with subnet) and Network Security Group configuration.
* The [network.bicep](https://gist.github.com/rbnmk/11e6175b7765e870be4eb53ef50eb6eb#file-network-bicep){:target="_blank"} module will orchestrate it in a way in which it makes sure to deploy the Network Security Group first.
* The Virtual Network will be deployed with the subnet and if configured properly the Network Security Group(s) will be attached!
* For each Virtual Network in the Environment Config we will call the [network.bicep](https://gist.github.com/rbnmk/11e6175b7765e870be4eb53ef50eb6eb#file-network-bicep){:target="_blank"} module with the corresponding configuration.
* We scope this deployment to the network resource group by selecting the first resource group from the resourceGroups array. As with most languages it starts counting at 0, therefore we set the scope to ResourceGroups[0].

Add this to your main.bicep:

<script src="https://gist.github.com/rbnmk/11e6175b7765e870be4eb53ef50eb6eb.js?file=module-network.bicep"></script>

Deploy the updated main.bicep file with either Az PowerShell or Az CLI. If you want to quickly get the latest version from my GitHub repo, you can use the `git clone https://github.com/rbnmk/bicep-build-your-landing-zone` command!

{% highlight powershell %}
az deployment sub create --name BlogExample --template-file .\main.bicep --location WestEurope
{% endhighlight %}

{% highlight powershell %}
New-AzDeployment -Name BlogExample -TemplateFile .\main.bicep -Location WestEurope
{% endhighlight %}

You have now successfully deployed the HUB network, which we will connect to the spoke network in the next blog so be sure to come back to found out how you can do this using Bicep.