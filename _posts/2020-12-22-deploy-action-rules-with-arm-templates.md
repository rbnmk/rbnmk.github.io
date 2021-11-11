---
id: 169
title: Deploy Action Rules with ARM Templates
date: 2020-12-22T14:46:32+02:00
author: Robin Makkus
layout: post
guid: http://rbnmk.net/?p=169
permalink: /2020/12/22/deploy-action-rules-with-arm-templates/
image: http://rbnmk.net/wp-content/uploads/2020/12/logo.png
categories:
  - ARM Templates
  - Azure Monitor
  - DevOps
  - SysAdmin
---
We recently started using Azure Monitor as our solution for monitoring Azure resources. While <a rel="noreferrer noopener" href="https://docs.microsoft.com/en-us/azure/azure-monitor/platform/alerts-action-rules?tabs=portal" target="_blank">Action Rules</a> are still in preview we want to make sure that we do not receive alerts when maintenance is scheduled. For instance we do patching during the evening and don&#8217;t want to receive alerts for VM&#8217;s in our ITSM tooling and/or mailboxes. 

Because we deploy our alerts via pre-defined ARM templates I wanted to deploy Action rules in the same manner and created a somewhat complete <a rel="noreferrer noopener" href="https://github.com/rbnmk/ARM/blob/master/Azure%20Monitor/Action%20Rules/actionrule.json" target="_blank">ARM template</a> to deploy Action Rules to set up suppression (or additional actions) for alerts based on conditions that you can set in the parameters. If you want to know which conditions can be used please check out the <a rel="noreferrer noopener" href="https://docs.microsoft.com/en-us/azure/azure-monitor/platform/alerts-action-rules?tabs=portal#filter-criteria" data-type="URL" data-id="https://docs.microsoft.com/en-us/azure/azure-monitor/platform/alerts-action-rules?tabs=portal#filter-criteria" target="_blank">Microsoft docs</a>.

The template and additional information can be found in my <a rel="noreferrer noopener" href="https://github.com/rbnmk/ARM/tree/master/Azure%20Monitor/Action%20Rules" target="_blank">GitHub repository</a> along with some parameter examples that I find useful, but feel free to adjust them to your needs!

If you have questions, ideas or run into a problem please reach out. Happy to help.

Happy holidays, see you next year!