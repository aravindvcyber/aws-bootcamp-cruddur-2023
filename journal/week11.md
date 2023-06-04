# Week 11 — CloudFormation

Created the necessary cloudformation stacks as shown below

* Networking
* Cluster
* Service
* Frontend
* RDS
* Dynamodb
* ALB
* Sync role
* Machine User

And also integrated the existing application with the new stacks

Have also done the new refactorings for the frontend

Implemented the aws_s3_sync tool to build and push the static site to s3

Also added OAC settings in Cloudformation for the new cloudfront

Refactored the backend for the file level reorganistion as well the jwt authorization

Readme link : https://github.com/aravindvcyber/aws-bootcamp-cruddur-2023/blob/main/journal/week11.md


## Stacks

![CrdNet](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/fddgknsmted4hklj3uvk.png)

![CrdCluster](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/np0ltaz5bgv8v86zo3q9.png)

![CrdSrvBackendFlask](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7rbtpdo2dsug68o37gcj.png)


![CrdFrontend](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/vaxxy795ec4tkmx4wwjd.png)
![CrdMachineUser](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ior34h9igevh6r1i5doa.png)
![CrdCicd](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/dolsmml5w488fh0lwloz.png)

![CrdCicd codebuild](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5a149wr0z70mfjfr91k3.png)
![sync role](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/tt1kce0pykvl93ideamh.png)
![crd db](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5k4rmfpvlz3t7ujyeo2h.png)
![crd ddb](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8ds22vejwiantih74j09.png)
![crd alb](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/itk2j1fngcfngxt9btqa.png)

## Resources

![crd alb def 2](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/3aaiu019y1wtjxvn7h3e.png)

![distributions](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/pfu0nz8e0xdc0bfzun56.png) 


![s3 oac bucket policy](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/sk47vfa9lvq4gm7r54v3.png)
![root bucket cloudfront](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1cbt7s5eroi1xw076usl.png)

![assets cloudfront](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/jyruqb887rzgisis4s9c.png)
![post confirmation vpc](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/cq6dxycjuc3cjsoriegi.png)
## Frontend Sync to S3

![static build](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/mm37rjk83x03z02a5ku8.png)
![sync status](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/b6am2ca5852hs7xjpt17.png)

## App screenshots

![user profile](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zbvcoiepdorlh3o1e84v.png)

![message group id](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ixzu011wdda9r4cxmrvy.png)

![home page](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/cwurlumed6x9rnoogybq.png)

![notifications](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/106242okizox1ttz5hfn.png)


## Build pipelines


![pipelines](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5i0sv3h88f311wypm7xv.png)

![codebuild](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8rx0p6fvrkh5m3k4r65j.png)

![cfn backend build project](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/u16e7ios6jtkq0x0l2mo.png)

![backend pipeline execution](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ele3m36clhmx97xkdh5s.png)

![backend pipeline execution 2](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/etw0nv1z3s2ncl1p554d.png)









