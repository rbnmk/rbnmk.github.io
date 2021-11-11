---
id: 98
title: Enable Azure Disk Encryption by using Powershell inside ARM Templates
date: 2020-05-06T14:30:00+02:00
#author: Robin Makkus
#layout: post
guid: http://www.rbnmk.net/?p=98
permalink: /2020/05/06/enable-azure-disk-encryption-by-using-deployment-script-in-arm-templates/
ssb_old_counts:
  - 'a:5:{s:7:"twitter";i:0;s:9:"pinterest";i:0;s:7:"fbshare";i:0;s:6:"reddit";i:0;s:6:"tumblr";i:0;}'
ssb_total_counts:
  - "0"
ssb_cache_timestamp:
  - "443125"
categories:
  - ARM Templates
  - Azure
  - Powershell
tags:
  - azure
  - deploymentscript
  - microsoft
  - preview
---
As of today there is no way of creating keys within your Key Vault deployment using ARM only. If you are using Azure DevOps you probably have a Powershell task taking care of this stuff. I am looking for ways to use the Deployment Script feature in ARM template to reduce the amount of tasks needed for your ARM template deployment. To learn more about the feature please take a look at this page: <https://docs.microsoft.com/en-us/azure/azure-resource-manager/templates/template-tutorial-deployment-script>

Before you get started you need to have access to or (to create) the following resources in your Azure subscription:

  * Azure Key Vault
  * Azure VM

To use the Deployment Script feature in the resources section of your ARM template we need to create a User Assigned Identity. This Identity will be used to authenticate against your Azure resources, in our example the Key Vault. Add the following snippet to your ARM template to create a User Assigned Identity.

In my template I create the Key Vault as well, but if the Key Vault already exists it should only add the access policy for the just created Identity. If you&#8217;ve worked with Key vault before you know that you don&#8217;t have access to the secrets inside the Key Vault by default, you always need to create an access policy. 

In the snippet below I create the Key Vault and the access policy for creating new keys as well.

As you can see this Key Vault resource is part of the same template so I reference the User Assigned Identity and reference the Principal Id (Object Id) by using the dot operator.

<blockquote class="wp-block-quote">
  <p>
    [reference(parameters(&#8216;userAssignedIdentityName&#8217;)).principalId]
  </p>
</blockquote>

Next up is the Deployment script but before we continue.. Add the following to your variables section in the ARM template before you continue to the last part of the ARM template:

The next part can be a bit tricky if you use VSCode to format your document. I choose to use an inline Powershell script but you can supply any script (i.e. on Github too!) when you format your ARM Template it destroys your inline Powershell part, please use it carefully. Hopefully Microsoft will update their extension to support this.

This is the deployment script. In the deployment script we reference the variables to fill in the User Assigned Identity used for running the script and we also provide the needed variables to the inline Powershell script.

We provide the Azure Powershell version so be sure that you use cmdlets that can be used in the version. At this moment only 3.0 is supported. (You can use Azure CLI too!)

We also use the $DeploymentScriptOutputs variable to Output the created Key Id so we can use this in the last part of the ARM template as a parameter.

For enabling Disk Encryption (ADE) we use the VM extension. In the snippet below I use a nested template to deploy the extension because the VM I want to enable ADE resides in an other Resource Group. A nested template can be used to target your deployment into an other resource group.

You can also download the full template from my <a href="https://github.com/rbnmk/ARM/blob/master/Deployment%20Script/vm-enable-keyvault-diskencryption.json" data-type="URL" data-id="https://github.com/rbnmk/ARM/blob/master/Deployment%20Script/vm-enable-keyvault-diskencryption.json" target="_blank" rel="noreferrer noopener">Github</a>!

Thank you for reading. I am still looking for ways to incorporate Deployment script in my templates. If you have ideas feel free to share!

Resources used to create this blog and ARM template:

  * <https://docs.microsoft.com/en-us/azure/azure-resource-manager/templates/template-tutorial-deployment-script>
  * <https://docs.microsoft.com/en-us/azure/azure-resource-manager/templates/template-tutorial-deploy-vm-extensions>
  * <https://docs.microsoft.com/en-us/azure/templates/microsoft.resources/2019-10-01-preview/deploymentscripts>