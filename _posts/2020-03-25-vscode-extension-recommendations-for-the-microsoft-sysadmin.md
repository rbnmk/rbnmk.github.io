---
title: "VSCode extension recommendations for the Microsoft SysAdmin!"
date: 2020-03-25T14:43:20+02:00
#author: Robin Makkus
#layout: post
permalink: /2020/03/25/vscode-extension-recommendations-for-the-microsoft-sysadmin/
categories:
  - blog
  - Extensions
  - SysAdmin
  - VSCode
tags:
  - automation
  - azure
  - cloud
  - powershell
  - scripting
---



I am currently transitioning from traditional day to day sysadmin work to DevOps / automation work. Which means I happen to spend more time writing code (mostly Infrastructure related) than actually configuring stuff via the GUI. I mostly work with Microsoft products like Microsoft PowerShell, Microsoft Azure, Microsoft 365 and Azure DevOps, so that&#8217;s what I will be recommending extensions and other settings for.

First off, VSCode is similar to Visual Studio but I find it more lightweight and it fills my needs with the use of several extensions. VSCode is also cross-platform available which is in my opinion a must these days. It can run on Windows, MacOS and Linux. If you don&#8217;t have VSCode yet, you can download it here: <a href="https://code.visualstudio.com/" target="_blank" rel="noreferrer noopener" aria-label=" (opens in a new tab)">https://code.visualstudio.com/</a>

## My extension recommendations

<div class="wp-block-group">
  <div class="wp-block-group__inner-container">
    <p class="has-text-align-left">
      <strong>I do write scripts for Powershell but I use ISE, how can I use VSCode?</strong><br />If you work with PowerShell I definitely recommend using VSCode and <a href="https://marketplace.visualstudio.com/items?itemName=ms-vscode.PowerShell" target="_blank" rel="noreferrer noopener" aria-label=" (opens in a new tab)">the Powershell extension</a>. The extension essentially helps you with writing PowerShell scripts by providing certain snippets-as-you-type, auto-completing and it also helps you format you scripts to make them more readable. It recently received an update for PowerShell Core with an PowerShell ISE mode included, if you liked ISE so much&#8230;.
    </p>
  </div>
</div>

**How about ARM Templates? I find them hard to write or don&#8217;t know where to start.**  
Are you planning to write ARM-templates or if you&#8217;re new to ARM (JSON) templates I definitely recommend these extensions! <a rel="noreferrer noopener" aria-label="Azure Resource Manager (ARM) Tools  (opens in a new tab)" href="https://marketplace.visualstudio.com/items?itemName=msazurermtools.azurerm-vscode-tools" target="_blank">Azure Resource Manager (ARM) Tools </a>, just like the Powershell extension snippets and helps you format the JSON in correct format. It also provides a nice outline for finding your way in complex and longer ARM-templates! <figure class="wp-block-image size-large">

![](https://i2.wp.com/www.rbnmk.nethttp//rbnmk.net.transurl.nl/wp-content/uploads/2020/03/armsnippet-5.gif?w=580&ssl=1) </figure> 

If you combine this extension with the <a href="https://marketplace.visualstudio.com/items?itemName=wilfriedwoivre.arm-params-generator" target="_blank" rel="noreferrer noopener" aria-label=" (opens in a new tab)">ARM Param generator extension</a> you&#8217;ll be happy to write and edit ARM-templates!<figure class="wp-block-image">

![demo.gif](https://i2.wp.com/github.com/wilfriedwoivre/vscode-arm-params-generator/raw/master/demo.gif?w=580&ssl=1) </figure> 

**What about Azure Pipelines? Can VSCode do it too?**  
If you want to start writing Azure Pipelines in code you can use the <a rel="noreferrer noopener" aria-label=" (opens in a new tab)" href="https://marketplace.visualstudio.com/items?itemName=ms-azure-devops.azure-pipelines" target="_blank">Azure Pipelines extension</a> to help you with getting started. <figure class="wp-block-image is-resized">

<img loading="lazy" src="https://i1.wp.com/raw.githubusercontent.com/microsoft/azure-pipelines-vscode/master/resources/configure-pipeline.gif?resize=580%2C327&#038;ssl=1" alt="Configure Pipeline Demo" width="580" height="327" /> </figure> 

It&#8217;s essentially writing in YAML, but the extension adds it&#8217;s value by providing syntax highlighting and suggestions related to Azure Pipelines. Be sure to check this out and get up to speed with Azure Pipelines!

**I usually edit or read CSVs in MS Excel, but can I do it in VSCode?**  
I often use a csv as input for a script. To make the CSV more readable in VSCode I use the <a rel="noreferrer noopener" aria-label=" (opens in a new tab)" href="https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv" target="_blank">Rainbow CSV extension</a>, which simply assigns a color to every column, thus making it more readable and easier to work with.<figure class="wp-block-image">

![screenshot](https://i2.wp.com/i.imgur.com/PRFKVIN.png?w=580&ssl=1) </figure> 

Last but not least I use the <a rel="noreferrer noopener" aria-label=" (opens in a new tab)" href="https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons" target="_blank">VScode icons extension</a> which basically enhances the file explorer folder and file icons. It helps you distinguish the difference between a csv, ps1 or yml file by changing the icon based on the extension of the file or the name of the folder.  
  
That&#8217;s it to get you started. Do you want to recommend any extensions to me? Please get in touch!