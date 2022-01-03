---
title: "Azure Bicep Landing Zone Series - Tags"
date: 2022-01-06 08:00:00
categories:
  - blog
tags:
  - Bicep
  - Azure
  - Design
  - Architecture
published: true
---

Welcome to this blog series. To follow the steps in this blog I recommend checking out my [previous blog]({ % post_url /blog/2022-01-01-landing-zone-resource-groups %}){:target="_blank"}. This blog series will help you build your Infrastructure as Code landing zone using Bicep. It is your choice how to deploy it. In my examples I will use Azure PowerShell or Azure CLI but feel free to execute the deployment using Azure DevOps or maybe even GitHub Actions.

The latest version of the code can be found in my [GitHub repository](https://github.com/rbnmk/bicep-build-your-landing-zone){:target="_blank"}, created specifically for this blog series.

## Intro

In the [previous blog]({% post_url /blog/2022-01-01-landing-zone-resource-groups %}){:target="_blank"} we started with our main.bicep file, some parameters, variables and a resource group deployment. In this blog we will add tags to these resource groups that can be used for reporting and numerous other tasks or reasons.

In this blog we will to a relatively simple task but it is not always done from the start. I like to include most of the tags right from the first deployment. Tags can applied to almost every Azure resource and can help you with identifying certain parts of the environment or even with reporting or monitoring purposes.

## Adding tags to resource groups and resources

In order to add tags to resource groups we will create an object in Bicep, and make sure to apply this to every resource group we are deploying. I usually start with simple tags and update them throughout the lifetime of the environment. In this example we start with a simple set.

* Environment: This tag will tell us, by looking at the resource which environment it belongs to.
* Solution: This tag wil tell us to which solution this resource belongs.
* Customer: This tag wi tell us for which customer this resource is used. This can come in handy when looking at a lot of resources via i.e. Azure Lighthouse (from an MSP or Large Enterprise perspective)

## Adding the tags and applying them to the resources and resource groups

We currently only have the HUB environment, so we will create the default tags and environment specific tags objects.

In the envConfig variable I add the object _tags on top and inside the 'hub' environment I will add the _environmentTags object.

<script src="https://gist.github.com/rbnmk/c91f59f8cb580191ef0b3d31f7fd91f1.js?file=1-blog-lz-tags-envconfig.bicep"></script>

Now to add it to our already created resource group in the previous blog add the following to your resource group resource.

<script src="https://gist.github.com/rbnmk/c91f59f8cb580191ef0b3d31f7fd91f1.js?file=2-blog-lz-tags-resource-group-with-tags.bicep"></script>

In the example above you see me using the [union()](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-array#union){:target="_blank"} function. It is used to combine two of the same objects. Duplicate values are only included once, which is handy.

Deploy the updated main.bicep file with either Az PowerShell or Az CLI.

{% highlight powershell %}
az deployment sub create --name BlogExample --template-file .\main.bicep --location WestEurope
{% endhighlight %}

{% highlight powershell %}
New-AzDeployment -Name BlogExample -TemplateFile .\main.bicep -Location WestEurope
{% endhighlight %}

You have now succesfully added tags to your resource groups. Next up is using our first module, which will be a VNET that we will deploy in the HUB!