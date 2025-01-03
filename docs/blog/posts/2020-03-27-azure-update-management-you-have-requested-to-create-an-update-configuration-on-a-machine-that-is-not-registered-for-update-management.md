---
date: 
  created: 2020-03-27T09:08:03+02:00
categories:
  - Azure
tags:
  - automation
  - azure
  - management
  - update
authors:
  - rbnmk
---
# Azure Update Management: You have requested to create an update configuration on a machine that is not registered for Update Management

We have several customers running with our Update Management solution via Azure Automation. We schedule the deployments via Powershell and Azure DevOps. I have ran into several issues after migrating VM&#8217;s to Azure or moving VM&#8217;s within Azure.

<!-- more -->

Somehow the System Hybrid Worker gets corrupted and does not work anymore, so update deployments will fail with the following warning:

-image was lost in migration-

To fix this I creaed a script. After running the script you can re-create the schedule in Azure Update Management.

Some things to keep in mind before running the script:

* You need to be Administrator on the VM that you are trying to run the script on.
* If you are using SCOM for monitoring, running the script could cause an hiccup because the HealthService service will be restarted.
* The script removes the System Hybrid Worker information from the registry and removes cache files from the C:\Program&nbsp;Files\Microsoft&nbsp;Monitoring&nbsp;Agent\Agent\Health&nbsp;Service&nbsp;State folder.

If you have any questions let me know in the comments!

The most recent script can be found in my <a href="https://github.com/rbnmk/PowerShell/blob/master/Clear-LocalHybridWorkerConfiguration.ps1" target="_blank" rel="noreferrer noopener">Github repo</a>.
