---
id: 75
title: Using objects as parameter input for your ARM template deployment
date: 2020-03-31T14:19:03+02:00
author: Robin Makkus
layout: post
guid: http://www.rbnmk.net/?p=75
permalink: /2020/03/31/using-objects-as-parameter-input-for-your-arm-template-deployment/
ssb_old_counts:
  - 'a:5:{s:7:"twitter";i:0;s:9:"pinterest";i:0;s:7:"fbshare";i:0;s:6:"reddit";i:0;s:6:"tumblr";i:0;}'
ssb_total_counts:
  - "0"
ssb_cache_timestamp:
  - "443242"
image: http://rbnmk.net/wp-content/uploads/2020/03/ARM-Templates-e1585660696492.jpg
categories:
  - ARM Templates
  - Azure
  - SysAdmin
tags:
  - cloud
  - parameters
  - script
  - template
  - vscode
---
I often try to make my deployments as dynamically as possible but for some resources this is not possible at all. Think about a VNET with multiple subnets and possibly a NSG. I try to overcome this by providing these not-so-dynamically-created values by using an object as parameter. 

In this blog I will learn you how to deploy a use an object type parameter for your VNET and Subnet deployment. Before you start take a look at the pre-requisites.

  * Azure Subscription with at least contributor rights
  * I assume that you have some experience with ARM templates and know how to deploy them

First we need to create the ARM template. I have one on my [Github](https://github.com/rbnmk/azurerm/blob/master/networking/vnet.json) which is ready for use (along with the [parameter file](https://github.com/rbnmk/azurerm/blob/master/networking/vnet.parameters.json) below). This template can be used for deploying 1 vnet with multiple subnets.

In the following picture I will explain the details of the ARM template:<figure class="wp-block-image size-large">

<img loading="lazy" width="1024" height="708" src="/wp-content/uploads/2020/03/image-2-1024x708.png" alt="" class="wp-image-76" srcset="https://i2.wp.com/rbnmk.net/wp-content/uploads/2020/03/image-2.png?resize=1024%2C708 1024w, https://i2.wp.com/rbnmk.net/wp-content/uploads/2020/03/image-2.png?resize=300%2C207 300w, https://i2.wp.com/rbnmk.net/wp-content/uploads/2020/03/image-2.png?resize=768%2C531 768w, https://i2.wp.com/rbnmk.net/wp-content/uploads/2020/03/image-2.png?resize=1536%2C1062 1536w, https://i2.wp.com/rbnmk.net/wp-content/uploads/2020/03/image-2.png?resize=2048%2C1416 2048w, https://i2.wp.com/rbnmk.net/wp-content/uploads/2020/03/image-2.png?resize=676%2C467 676w, https://i2.wp.com/rbnmk.net/wp-content/uploads/2020/03/image-2.png?w=1160 1160w, https://i2.wp.com/rbnmk.net/wp-content/uploads/2020/03/image-2.png?w=1740 1740w" sizes="(max-width: 580px) 100vw, 580px" /> </figure> 

  1. This is the parameter we are going to fill with the needed information. Important is the &#8220;type&#8221; is set to &#8220;object&#8221;.
  2. In this part we select the parameter values by using the . (dot) operator.
  3. Because we want to create multiple subnets we are using a copy statement to iterate over the values in the supplied object parameter, again by using the . (dot) operator
  4. This outputs the name of the deployed VNET.

Below is a snippet of the object we can provide as a parameter to the template: &#8220;parameters&#8221;:{ &#8220;VNetSettings&#8221;:{ &#8220;value&#8221;:{ {<Values>} }

If you look closely in the example below you&#8217;ll notice that the values for &#8220;Address Prefixes&#8221; and &#8220;Subnets&#8221; are provided as an array. (between the brackets [])

Now edit the parameter file to your liking and try to deploy the template via your preferred deployment tool. In this example I use Powershell with the New-AzResourceGroupDeployment cmdlet.

<blockquote class="wp-block-quote">
  <p>
    <strong>$Location</strong> = &#8220;West Europe&#8221;<br /><strong>$ResourceGroupName</strong> = &#8220;Network&#8221;
  </p>
  
  <p>
    <strong>New-AzResourceGroup</strong> -ResourceGroupName <strong>$ResourceGroupName</strong> -Location $Location
  </p>
  
  <p>
    <strong>New-AzResourceGroupDeployment</strong> -ResourceGroupName <strong>$ResourceGroupName</strong> -TemplateFile <em>.\networking\vnet.json</em> -TemplateParameterFile <em>.\networking\vnet.parameters.json</em>
  </p>
</blockquote>



Now you&#8217;ve learned how to use an object as a parameter. I find this very easy and convenient to use throughout my deployments for several resources. Thank you for reading and stay safe!