Title: Cloudblog
Summary: Yet-another blogging platform. Fully distributed, statically generated using WebPayments for access to articles
Category: Projects
Date: 2020-08-01
State: draft

Cloudblog is decentralized blogging service - meaning each part of the blog is provided by a service provider and everything
holds together by using standardized protocols such as WebDAV, OAuth2 and WebPayments. Of course it should
support microblogging and federated social platform together with webmentions.

The other thing is to how to store the data. Primarily, I am using WebDAV because it is a standard
technology fir writing files into a webserver. Unfortunately, followup actions are a problem. First,
we need to backup the data. This could be solved by a regular commit to a separate Git repository. Or
I could use IPFS. This project seems scary though. It would require teaming up with people and tackling
this together.