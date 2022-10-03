# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

I choose an App Service for this particular project because while it isn't as scalable as a VM, it feels like a better fit for this kind of project which at the moment feels like a blog.
It is more cost effective than a VM because it is cheaper, it doesn't need downtime to manage the OS, it should be highly available for consumption, and we seemingly don't need access to any OS level functions to run this application.


### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

If the CMS were to grow into something more than just a blog like into something much more resource heavy like a CMS used at an enterprise to manage any kind of document or file needed to be stored and available on demand then running on a VM might make more sense. That could become more resource intensive and could need more than a web service to handle with extra applications running to help with things such as anti-virus, larger workloads, security, etc.
It could also become an extremely popular blog with hundreds of millions of people going to it and require more processing power and memory to keep up with the hardware demand.