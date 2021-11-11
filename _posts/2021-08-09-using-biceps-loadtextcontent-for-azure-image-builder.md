---
id: 186
title: 'Using Bicep&#8217;s loadTextContent() for Azure Image Builder'
date: 2021-08-09T15:12:28+02:00
#author: Robin Makkus
#layout: post
guid: https://rbnmk.net/?p=186
permalink: /2021/08/09/using-biceps-loadtextcontent-for-azure-image-builder/
categories:
  - ARM Templates
  - Azure
  - Bicep
  - DevOps
  - Powershell
  - SysAdmin
tags:
  - automation
  - azure
  - builder
  - image
  - management
  - script
---
Recently I started using Azure Image Builder together with Azure Biceps ability to load a script from a separate file. In this blog I will show you how to deploy & build a simple image template and distribute it to either a VHD or Shared Image Gallery.

Before you start make sure you have the latest Azure Bicep and Az.PowerShell module or Azure CLI installed and have access to an Azure subscription / Resource Group to deploy and build the templates.

In this example I am going to use Chocolatey to install some tools and use the Install-WindowsFeature cmdlet for installing RSAT on a Windows Server 2019 system. For me this sounds like the typical jumphost configuration.

All example files can be found on my <a rel="noreferrer noopener" href="https://github.com/rbnmk/bicep-loadcontent-image-builder" data-type="URL" data-id="https://github.com/rbnmk/bicep-loadcontent-image-builder" target="_blank">GitHub</a> for reference, so feel free to adjust them to your needs or clone to your pc for usage throughout this blog.

To use Azure Image Builder we need a User Assigned Identity that has access to the template (or resource group) in which this template is going to be deployed. In this example I use the Contributor role, if you want to use least privilege you can create a custom role, see <a href="https://docs.microsoft.com/en-us/azure/virtual-machines/windows/image-builder-gallery#assign-permissions-for-identity-to-distribute-images" data-type="URL" data-id="https://docs.microsoft.com/en-us/azure/virtual-machines/windows/image-builder-gallery#assign-permissions-for-identity-to-distribute-images">Microsoft docs</a> for more information.



In my repository I have one <a href="https://github.com/rbnmk/bicep-loadcontent-image-builder/blob/975a4dd5bfba83d00c25ae51c6b642de73c12d8b/main.bicep" data-type="URL" data-id="https://github.com/rbnmk/bicep-loadcontent-image-builder/blob/975a4dd5bfba83d00c25ae51c6b642de73c12d8b/main.bicep">main.bicep</a>, which orchestrates the deployment and uses the files in the subfolders (modules, scripts)

  1. It will create a resource group.
  2. It will create the required User Assigned Managed Identity.
  3. It will assign the User Assign Managed Identity the Contributor role on the earlier deployed Resource Group.
  4. It will deploy the Image Template to Azure.

We can inspect the <a href="https://github.com/rbnmk/bicep-loadcontent-image-builder/blob/975a4dd5bfba83d00c25ae51c6b642de73c12d8b/scripts/jumphost-config.ps1" data-type="URL" data-id="https://github.com/rbnmk/bicep-loadcontent-image-builder/blob/975a4dd5bfba83d00c25ae51c6b642de73c12d8b/scripts/jumphost-config.ps1">jumphost-config.ps1</a> file, which simply runs a couple of PowerShell cmdlets to install software with Chocolatey. We could copy this in the bicep file directly, which is OK.. but how about importing the file into the bicep at compile time and enjoy Intellisense from our IDE while authoring the PowerShell script? We can do this by using the loadTextContent() function in Bicep.



In the module folder, file: [vm-image-template-pwsh.bicep](https://github.com/rbnmk/bicep-loadcontent-image-builder/blob/975a4dd5bfba83d00c25ae51c6b642de73c12d8b/modules/vm-image-template-pwsh.bicep) we see the following variable, it will simply import the contents of the file into the bicep file (red text):

<pre class="wp-block-code"><code>var inlineScript = &#91;
  {
    type: 'PowerShell'
    name: 'PowerShellScript'
    runAsSystem: true
    runElevated: true
    inline: &#91;
     &lt;strong> &lt;span class="has-inline-color has-accent-color">loadTextContent('../scripts/jumphost-config.ps1')&lt;/span>&lt;/strong>
    ]
    validExitCodes: &#91;
      0
      3010 // Reboot required
    ]
  }
]</code></pre>

<span class="has-inline-color has-accent-color">Unfortunately we can&#8217;t set the name of the file as a parameter due to the fact that it would be unknown which file to load at compilation time. (More info on why can be found on <a href="https://github.com/Azure/bicep/issues/3816">Github</a> Issue for Azure Bicep)</span>

Note: for the full spec of the arm template possibilities for Azure Image Builder <a href="https://docs.microsoft.com/en-us/azure/virtual-machines/linux/image-builder-json" data-type="URL" data-id="https://docs.microsoft.com/en-us/azure/virtual-machines/linux/image-builder-json">see this page</a>.

To deploy the bicep files (and end up with a usable template in Azure) simply run the following line of code or provide your own parameter names inline or using a JSON parameter file.



Azure PowerShell

<div class="wp-block-group">
  <div class="wp-block-group__inner-container">
    <pre class="wp-block-code"><code>New-AzDeployment -Name "Azure-Image-Builder-Deployment" -Location "WestEurope" -TemplateFile .\main.bicep</code></pre>
    
    <p>
      Azure CLI
    </p>
    
    <pre class="wp-block-code"><code>az deployment sub create --name "Azure-Image-Builder-Deployment" --location "WestEurope" --template-file ".\main.bicep"</code></pre>
  </div>
</div>

If everything was successful you should end up with the aforementioned resources: A Resource Group with a Managed Identity & Image Template resource.<figure class="wp-block-image size-full">

<img loading="lazy" width="580" height="282" src="https://i1.wp.com/rbnmk.net/wp-content/uploads/2021/08/image.png?resize=580%2C282&#038;ssl=1" alt="" class="wp-image-192" srcset="https://i1.wp.com/rbnmk.net/wp-content/uploads/2021/08/image.png?w=859 859w, https://i1.wp.com/rbnmk.net/wp-content/uploads/2021/08/image.png?resize=300%2C146 300w, https://i1.wp.com/rbnmk.net/wp-content/uploads/2021/08/image.png?resize=768%2C374 768w" sizes="(max-width: 580px) 100vw, 580px" /> </figure> 

If we inspect the &#8220;Export Template&#8221; section of the Image Template you should see the contents of the PowerShell script, ready to be executed.<figure class="wp-block-image size-large is-resized">

<img loading="lazy" src="https://i0.wp.com/rbnmk.net/wp-content/uploads/2021/08/image-5-1024x251.png?resize=580%2C142&#038;ssl=1" alt="" class="wp-image-203" width="580" height="142" srcset="https://i0.wp.com/rbnmk.net/wp-content/uploads/2021/08/image-5.png?resize=1024%2C251 1024w, https://i0.wp.com/rbnmk.net/wp-content/uploads/2021/08/image-5.png?resize=300%2C74 300w, https://i0.wp.com/rbnmk.net/wp-content/uploads/2021/08/image-5.png?resize=768%2C188 768w, https://i0.wp.com/rbnmk.net/wp-content/uploads/2021/08/image-5.png?resize=1200%2C294 1200w, https://i0.wp.com/rbnmk.net/wp-content/uploads/2021/08/image-5.png?w=1297 1297w" sizes="(max-width: 580px) 100vw, 580px" /> <figcaption>Contents of the Export Template section</figcaption></figure> 

To start the build click on the Image Template resource and hit the build button. In a next blog I will show you how you can create a VM from this!

Note: At this time we cannot update / replace an existing Image Template file in Azure. If you want to run the template multiple times remove the Image Template in Azure or change the name of the ImageTemplate.