---
id: 71
title: 'Azure Update Management: You have requested to create an update configuration on a machine that is not registered for Update Management'
date: 2020-03-27T09:08:03+02:00
author: Robin Makkus
layout: post
guid: http://www.rbnmk.net/?p=71
permalink: /2020/03/27/azure-update-management-you-have-requested-to-create-an-update-configuration-on-a-machine-that-is-not-registered-for-update-management/
ssb_old_counts:
  - 'a:5:{s:7:"twitter";i:0;s:9:"pinterest";i:0;s:7:"fbshare";i:0;s:6:"reddit";i:0;s:6:"tumblr";i:0;}'
ssb_total_counts:
  - "0"
ssb_cache_timestamp:
  - "443214"
categories:
  - Powershell
  - SysAdmin
tags:
  - automation
  - azure
  - management
  - update
---
We have several customers running with our Update Management solution via Azure Automation. We schedule the deployments via Powershell and Azure DevOps. I have ran into several issues after migrating VM&#8217;s to Azure or moving VM&#8217;s within Azure. Somehow the System Hybrid Worker gets corrupted and does not work anymore, so update deployments will fail with the following warning:<figure class="wp-block-image size-large">

<img loading="lazy" width="1024" height="16" src="/wp-content/uploads/2020/03/image-1-1024x16.png" alt="" class="wp-image-72" srcset="https://i2.wp.com/rbnmk.net/wp-content/uploads/2020/03/image-1.png?resize=1024%2C16 1024w, https://i2.wp.com/rbnmk.net/wp-content/uploads/2020/03/image-1.png?resize=300%2C5 300w, https://i2.wp.com/rbnmk.net/wp-content/uploads/2020/03/image-1.png?resize=768%2C12 768w, https://i2.wp.com/rbnmk.net/wp-content/uploads/2020/03/image-1.png?resize=1536%2C24 1536w, https://i2.wp.com/rbnmk.net/wp-content/uploads/2020/03/image-1.png?resize=2048%2C32 2048w, https://i2.wp.com/rbnmk.net/wp-content/uploads/2020/03/image-1.png?resize=676%2C11 676w, https://i2.wp.com/rbnmk.net/wp-content/uploads/2020/03/image-1.png?w=1160 1160w, https://i2.wp.com/rbnmk.net/wp-content/uploads/2020/03/image-1.png?w=1740 1740w" sizes="(max-width: 580px) 100vw, 580px" /> </figure> 

To fix this I created a script. After running the script you can re-create the schedule in Azure Update Management.

Some things to keep in mind before running the script:

  * You need to be Administrator on the VM that you are trying to run the script on.
  * If you are using SCOM for monitoring, running the script could cause an hiccup because the HealthService service will be restarted.
  * The script removes the System Hybrid Worker information from the registry and removes cache files from the C:\Program&nbsp;Files\Microsoft&nbsp;Monitoring&nbsp;Agent\Agent\Health&nbsp;Service&nbsp;State folder.

If you have any questions let me know in the comments!

The most recent script can be found in my <a href="https://github.com/rbnmk/PowerShell/blob/master/Clear-LocalHybridWorkerConfiguration.ps1" target="_blank" rel="noreferrer noopener">Github repo</a>.