# Week 9 — CI/CD with CodePipeline, CodeBuild and CodeDeploy

Weekly branch 
https://github.com/aravindvcyber/aws-bootcamp-cruddur-2023/tree/week-9

README for better readability

https://github.com/aravindvcyber/aws-bootcamp-cruddur-2023/blob/main/journal/week9.md

* Configured CodeBuild Project for backend flask
* created a build progress badge for backend
* Configured CodePipeline for backend flask
* Created a buildspec.yml file for backend flask
* Configured codedeploy to ECS fargate for backend
* Configured CodeBuild Project for frontend react
* created a build progress badge for frontend
* Configured CodePipeline for frontend flask
* Created a buildspec.yml file for frontend flask
* Configured codedeploy to ECS fargate for frontend
* The setup process for these pipelines help me to solidify my understanding of how the current e2e deployment to ECS
* Also I believe this will bring a lot of consistency in prod readiness when I switch context across various stack elements


#### Build Badges Github Actions


[![CodeQL](https://github.com/aravindvcyber/aws-bootcamp-cruddur-2023/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/aravindvcyber/aws-bootcamp-cruddur-2023/actions/workflows/github-code-scanning/codeql)

[![Node.js CI](https://github.com/aravindvcyber/aws-bootcamp-cruddur-2023/actions/workflows/node.js.yml/badge.svg)](https://github.com/aravindvcyber/aws-bootcamp-cruddur-2023/actions/workflows/node.js.yml)

[![Python application](https://github.com/aravindvcyber/aws-bootcamp-cruddur-2023/actions/workflows/python-app.yml/badge.svg)](https://github.com/aravindvcyber/aws-bootcamp-cruddur-2023/actions/workflows/python-app.yml)

#### Build Badges CodeBuild


![Cruddur Frontend CodeBuild Status](https://codebuild.ap-south-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiRDlRRXorTjl6anpBZmpEYkJPSERCdSt1OEE2QUFyY253UXpSR20yTkhIM3FmZ1hodVNKYVNmNjRJMmVabFI5dHhEZGcrNXlMMmNPNFVTMk5TOC9XelBVPSIsIml2UGFyYW1ldGVyU3BlYyI6InVNMXZOTld4NFF4bys4UlciLCJtYXRlcmlhbFNldFNlcmlhbCI6Mn0%3D&branch=main)

![Cruddur Backend CodeBuild Status](https://codebuild.ap-south-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiNXcrRDZ3akxYTFo3c2pjdHQ2NVFSWGNoSFB2REJFcXBlV1pPSEsyRE9xSXZWYVVXY3ZRdS9TVWZFS0lVWnQ1eEVMQjNSeW9nbFluRCt5aEI4N3JQWlU0PSIsIml2UGFyYW1ldGVyU3BlYyI6IlpLODdnSWJLMkZpUWtqdnAiLCJtYXRlcmlhbFNldFNlcmlhbCI6Mn0%3D&branch=main)


## ECS fargate map

![ecs services](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/rillmmdddfyvqfse7r6k.png)
![ecs tasks](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5q3bn5p1brzsei4a4mdo.png)

![ecs cpu](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/fpqt631pk9i73k8xqm4m.png)
![ecs memory](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6zl1cajmyekhn6e1j255.png)

## Pipelines

![pipelines](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/16jk9cj532zjdsae7ejd.png)

### Backend Pipeline

![edit backend pipeline](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/plyjkrasrqpap6m5vjw3.png)
![edit backend build](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/spc0frx5va0ff85bouus.png)
![edit backend deploy](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/9f7natm82wey6qldprmh.png)

### Frontend Pipeline

![frontend edit code pipeline](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ttkph794af2ptr6ipvvq.png)
![edit frontend build](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/rkrrqgzo3ck0m14g7je8.png)
![edit frontend deploy](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/41s93zwtcdsurrrwctm5.png)


## Build Projects

![build projects](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/mlmg1i61e29e9fxnkfw1.png)

![build history](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/b5wevvjqwuhz3kbdfc1a.png)

![frontend pipeline in action](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qw03basm0n0eu9ikgwe3.png)

![backend pipeline in action](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/bdpqt4qzt97d3e6enejp.png)


### Codebuild logs

![backend logs](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/xhiakq8n7e5zjwnbcecc.png)
![frontend logs](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/xl11kwv00oqqskynu2df.png)














