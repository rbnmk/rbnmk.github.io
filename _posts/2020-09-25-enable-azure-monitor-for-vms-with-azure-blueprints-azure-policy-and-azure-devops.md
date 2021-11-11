---
id: 123
title: Enable Azure Monitor for VMs with Azure Blueprints, Azure Policy and Azure DevOps
date: 2020-09-25T08:32:02+02:00
#author: Robin Makkus
#layout: post
guid: http://rbnmk.net/?p=123
permalink: /2020/09/25/enable-azure-monitor-for-vms-with-azure-blueprints-azure-policy-and-azure-devops/
categories:
  - Azure
  - Azure Blueprints
  - Azure DevOps
  - Azure Policy
tags:
  - cloud
  - devops
  - governance
  - monitoring
---

It&#8217;s been a long time since I wrote a blog, but i&#8217;ll try to write one more often. In this blog I will show you how to enable Azure Monitor for VMs and VM Scale sets with Azure Policy and Azure DevOps using Azure Blueprints. In this post I assume you have some experience with at least some of the mentioned products.

To follow the steps you need to have a couple of pre-requisites.

  * Access to an Azure Subscription.
  * Access to Azure DevOps with a Service Connection (Service Principal) that has Owner permission on the subscription.
  * Have the <a rel="noreferrer noopener" href="https://marketplace.visualstudio.com/items?itemName=nepeters.azure-blueprints" target="_blank">Azure DevOps Blueprint extension</a> installed in your DevOps organization.
  * Your favorite IDE to edit the Azure Blueprint files.

If you want to know more about what you can do with Azure Blueprints please read through the <a href="https://docs.microsoft.com/nl-nl/azure/governance/blueprints/overview" data-type="URL" data-id="https://docs.microsoft.com/nl-nl/azure/governance/blueprints/overview" target="_blank" rel="noreferrer noopener">Microsoft Docs</a> to get you up to speed!

To get started with the Azure Blueprint you can download the files from here: <a href="https://github.com/rbnmk/Blueprints/tree/master/AzureMonitor" data-type="URL" data-id="https://github.com/rbnmk/Blueprints/tree/master/AzureMonitor">Github</a>

<div class="wp-block-image">
  <figure class="alignright size-full"><img loading="lazy" width="239" height="215" src="https://i1.wp.com/rbnmk.net/wp-content/uploads/2020/09/image-1.png?resize=239%2C215&#038;ssl=1" alt="" class="wp-image-125" /><figcaption>The folder should look like this.</figcaption></figure>
</div>

We don&#8217;t go to deep into the blueprint files now but in my example we also deploy a new Resource Group and a Log Analytics workspace to connect the VMs to. You can remove this from the **Blueprint.json** file and just point to an existing Log Analytics workspace if you want. Edit the **azMonitoringWorkspaceName** parameter in the **assignment.json** file with the existing workspace name and remove the resource group references in both the **blueprint.json** and **assignment.json** file. Last but not least remove the **logAnalytics.json** template file from the artifacts folder.

While the Blueprint files are set up in a generic way we only need to make two changes in the **assignment.json** file. This is basically what you would call a parameter file.

You can update the name and location of the resource group and you can update the name of the Log Analytics workspace in the **assignment.json** file. Of course if you want you can try it with the default values as well.

Next up is creating the Azure DevOps YAML pipeline. Working with Blueprints is a 2-step process. First you publish a blueprint and after publishing the blueprint you assign the blueprint to either a subscription or management group. The mentioned extension makes it easy to deploy and maintain the blueprint definition via CI/CD.

##### Let&#8217;s get started with the technical stuff..

###### 1. Create a new pipeline.

For this purpose I have a <a rel="noreferrer noopener" href="https://gist.github.com/rbnmk/3b0b18bdbf88654969bdc2a17b075d50" data-type="URL" data-id="https://gist.github.com/rbnmk/3b0b18bdbf88654969bdc2a17b075d50" target="_blank">very basic pipeline</a>, which can also be found in the root of my Github blueprints repository. 

###### 2. Edit the Service Connection variable with the name of your service connection in Azure DevOps.<figure class="wp-block-image size-large">

<img loading="lazy" width="362" height="57" src="https://i1.wp.com/rbnmk.net/wp-content/uploads/2020/09/image-3.png?resize=362%2C57&#038;ssl=1" alt="" class="wp-image-127" srcset="https://i1.wp.com/rbnmk.net/wp-content/uploads/2020/09/image-3.png?w=362 362w, https://i1.wp.com/rbnmk.net/wp-content/uploads/2020/09/image-3.png?resize=300%2C47 300w" sizes="(max-width: 362px) 100vw, 362px" /> </figure> 

###### 3. Run the pipeline.

<div class="wp-block-group">
  <div class="wp-block-group__inner-container">
    <p>
      Look at the Blueprints assigned blueprints page if it was successfull you can view the Azure Policy blade as well. It will take a couple of minutes for results to show up though.
    </p>
  </div>
</div><figure class="wp-block-image size-large">

<img loading="lazy" width="570" height="154" src="https://i2.wp.com/rbnmk.net/wp-content/uploads/2020/09/image-4.png?resize=570%2C154&#038;ssl=1" alt="" class="wp-image-128" srcset="https://i2.wp.com/rbnmk.net/wp-content/uploads/2020/09/image-4.png?w=570 570w, https://i2.wp.com/rbnmk.net/wp-content/uploads/2020/09/image-4.png?resize=300%2C81 300w" sizes="(max-width: 570px) 100vw, 570px" /> </figure> 

After a couple of minutes you should be able to see the results in the Azure Policy blade, as you can see I am not fully compliant. I can create a remediation task to solve this. New VMs and Scale sets will be remediated upon creation.<figure class="wp-block-image size-full">

<img loading="lazy" width="580" height="103" src="https://i2.wp.com/rbnmk.net/wp-content/uploads/2020/09/image-8.png?resize=580%2C103&#038;ssl=1" alt="" class="wp-image-147" srcset="https://i2.wp.com/rbnmk.net/wp-content/uploads/2020/09/image-8.png?w=1452 1452w, https://i2.wp.com/rbnmk.net/wp-content/uploads/2020/09/image-8.png?resize=300%2C54 300w, https://i2.wp.com/rbnmk.net/wp-content/uploads/2020/09/image-8.png?resize=1024%2C183 1024w, https://i2.wp.com/rbnmk.net/wp-content/uploads/2020/09/image-8.png?resize=768%2C137 768w, https://i2.wp.com/rbnmk.net/wp-content/uploads/2020/09/image-8.png?resize=1200%2C214 1200w" sizes="(max-width: 580px) 100vw, 580px" /> </figure> 

Now you&#8217;ve learned what you can do when combining these great tools. I hope I inspired you to use either one of these tools for your environments.

Deploy your Azure Blueprints with Azure DevOps automatically enabling Virtual Machines to be monitored with Azure Monitor! If you run into a problem or have questions let me know. 😄

Resources used to write this blog:

  * <a href="https://docs.microsoft.com/nl-nl/azure/governance/blueprints/overview" target="_blank" rel="noreferrer noopener">https://docs.microsoft.com/nl-nl/azure/governance/blueprints/overview</a>
  * <a href="https://marketplace.visualstudio.com/items?itemName=nepeters.azure-blueprints" target="_blank" rel="noreferrer noopener">https://marketplace.visualstudio.com/items?itemName=nepeters.azure-blueprints</a>
  * <a href="https://docs.microsoft.com/en-us/azure/governance/policy/samples/built-in-policies" target="_blank" rel="noreferrer noopener">https://docs.microsoft.com/en-us/azure/governance/policy/samples/built-in-policies</a>
  * <a href="https://docs.microsoft.com/nl-nl/azure/governance/policy/" target="_blank" rel="noreferrer noopener">https://docs.microsoft.com/nl-nl/azure/governance/policy/</a>