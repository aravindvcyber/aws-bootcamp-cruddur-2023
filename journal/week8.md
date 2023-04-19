# Week 8 — Serverless Image Processing

Weekly branch 
https://github.com/aravindvcyber/aws-bootcamp-cruddur-2023/tree/week-8

README for better readability

https://github.com/aravindvcyber/aws-bootcamp-cruddur-2023/blob/main/journal/week8.md


* created CDK stack with typescript template
* created s3 bucket to store processed assets
* created s3 bucket to store uploaded assets
* served assets behind Cloudfront also added route 53 for dns
* processed images using a javascript lambda running sharpjs
* implemented lambda layers using ruby
* used s3 event notifications to trigger processing images
* implemented HTTP API Gateway using a lambda authorizer
* generated openapi3 spec file to review and add it to the repo
* implemented a ruby function to generate a presigned URL and integrated to the path /avatars/key_upload
* upload assets to a bucket client side using a presigned URL which has life cycle rules to cleanup after a certain period
* Had good amount of exposure in resolving the CORS in this week
* Cloudfront integration is awesome to serve static content
* sharpjs library got some handson in using this image processing with node, earlier i had some exposure to using rust for image resizing
* Glad to see ruby since it is a first time experience for me in projects
* authorization verification and jwt parsing is interesting to understand here
* CSS changes for the profile page in UI looks cool and able to try handson
* Also new bunch of scripts for this week, especially for me I setup a few more of them for interoperability with git pod and code space.
* Undoubtably resolving the CORS issues across the stuff and along the gitpod, codespace and aws is the highlight for delay this week


## Final Views


![aravind profile](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4j7h22491nwdnyce7ckd.png)

![bayko profile](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7au4qnqm9z70zz1z2dq4.png)

## Serverless stack

![cdk deploy stack](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/nyldfpu5xv6vythxzlpt.png)

![upload bucket cors setup](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/g5rdslxiad5diptvln35.png)

![s3 lifecycle rule for uploads](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/fwjjxc4l0ti8pdwnt9m5.png)

![lambda trigger](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/k8hilv3bepfzwg5e12la.png)

![resizer lambda](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/k1hfyw8sxb5uwtj7jtra.png)

![s3 permission for resizer](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/iuxn2iuuv398dli41399.png)

![sns topic event notification](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/2clql6ag1dvmirxhu3g3.png)

### Ruby Function for presigned url

![creating ruby lambda function](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/3v4q36bjlgjswb1zrily.png)

![ruby lambda layer](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/xy9ta1v7ce5b79zwvp7m.png)

![ruby layer generation](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zzsermqrzda87i1j9m64.png)

![generated open api 3 spec file for documentation and inspection with swagger](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/0tut3gq68s8zugek35tu.png)


![new api](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/bosccdpnh74g5lv57gxh.png)

![routes](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ez84j8on8qk2dldn89y1.png)

![authorization for routes](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1rlypnykdbzxrpshr1x4.png)

![authorization with custom lambda integration](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/3mg6960hfuz7mckvqj3k.png)

### Authorizer 

![authorizer lambda](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1x7c9cxrm6ogvmt3wlw0.png)

![lambda authorizer logs](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1xa5to7ofp8zralltnar.png)

![routes and integration](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/rdt47bnroje9kks5hm28.png)


![route integration to avatar presigned url generator](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/k84ka550hch0ey3fq8af.png)

### presigned url generator

![Avatar upload pre signed url generator](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zewiurzbya5zdb1hx7hn.png)

![uploader s3 access](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/46itvjyz8edxp8ak0upn.png)

![lambda ruby integrated](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/e0ka41v6fatz0le4490h.png)

![cruddur avatar uploader logs](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/p8v7k0ywe762ieoolcnc.png)


![api gateway custom domain](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/f3n6i03130qvjo3por04.png)

![api gateway custom domain api mappings](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/c0w0twa47n017toaqhya.png)


![route53 for api](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/t5wxuawy4abgjbac2gaq.png)

![Api access cloudwatch](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/koico4ebat3wj3lwn806.png)

## Cloudfront 

![new cloudfront setup](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/v7dygfetcf63r0jhi3qg.png)

![cloudfront origins](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/fcxp98vps2njycf4wpew.png)

![assets bucket origin bucket policy](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zuwhr5yz2z0xwm6vkasb.png)

![cloudfront behaviours](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/xcu06m5up3wpledrc2oq.png)

![cloudfront invalidations history](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4ioztnsmj2jll3u6sf3e.png)

![cloudfront invalidation sample](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/tlhqpfc6zdn5z6alopjo.png)


![route53 for cloudfront](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/w3wn5yzrxied1c5x8lr6.png)


## Other Notes


## New Directory

Lets contain our cdk pipeline in a new top level directory called:

```sh
cd /workspace/aws-bootcamp-cruddur-2023
mkdir thumbing-serverless-cdk
```

## Install CDK globally

This is so we can use the AWS CDK CLI for anywhere.

```sh
npm install aws-cdk -g
```

We'll add the the install to our gitpod task file
```sh
  - name: cdk
    before: |
      npm install aws-cdk -g
```


## Initialize a new project

We'll initialize a new cdk project within the folder we created:

```sh
cdk init app --language typescript
```

## Add an S3 Bucket

Add the following code to your `thumbing-serverless-cdk-stack.ts`

```ts
import * as s3 from 'aws-cdk-lib/aws-s3';

const bucketName: string = process.env.THUMBING_BUCKET_NAME as string;

const bucket = new s3.Bucket(this, 'ThumbingBucket', {
  bucketName: bucketName,
  removalPolicy: cdk.RemovalPolicy.DESTROY,
});
```

```sh
export THUMBING_BUCKET_NAME="cruddur-thumbs"
gp env THUMBING_BUCKET_NAME="cruddur-thumbs"
```

- [Bucket Construct](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)
- [Removal Policy](https://docs.aws.amazon.com/cdk/api/v1/docs/@aws-cdk_core.RemovalPolicy.html)

## Bootstrapping

> Deploying stacks with the AWS CDK requires dedicated Amazon S3 buckets and other containers to be available to AWS CloudFormation during deployment. 

```sh
cdk bootstrap "aws://$AWS_ACCOUNT_ID/$AWS_DEFAULT_REGION"
```

## Build

We can use build to catch errors prematurely.
This jsut builds tyescript

```sh
npm run build
```


## Synth

> the synth command is used to synthesize the AWS CloudFormation stack(s) that represent your infrastructure as code.

```sh
cdk synth
```


## Deploy

```sh
cdk deploy
```

## List Stacks

```sh
cdk ls
```

## Load Env Vars
  ```ts
const dotenv = require('dotenv');
dotenv.config();

const bucketName: string = process.env.THUMBING_BUCKET_NAME as string;
const folderInput: string = process.env.THUMBING_S3_FOLDER_INPUT as string;
const folderOutput: string = process.env.THUMBING_S3_FOLDER_OUTPUT as string;
const webhookUrl: string = process.env.THUMBING_WEBHOOK_URL as string;
const topicName: string = process.env.THUMBING_TOPIC_NAME as string;
const functionPath: string = process.env.THUMBING_FUNCTION_PATH as string;
console.log('bucketName',bucketName)
console.log('folderInput',folderInput)
console.log('folderOutput',folderOutput)
console.log('webhookUrl',webhookUrl)
console.log('topicName',topicName)
console.log('functionPath',functionPath)
```

## Create Bucket

```ts
import * as s3 from 'aws-cdk-lib/aws-s3';

const bucket = this.createBucket(bucketName)

createBucket(bucketName: string): s3.IBucket {
  const logicalName: string = 'ThumbingBucket';
  const bucket = new s3.Bucket(this, logicalName , {
    bucketName: bucketName,
    removalPolicy: cdk.RemovalPolicy.DESTROY,
  });
  return bucket;
}
```

## Create Lambda

```ts
import * as lambda from 'aws-cdk-lib/aws-lambda';

const lambda = this.createLambda(folderInput,folderOutput,functionPath,bucketName)

createLambda(folderIntput: string, folderOutput: string, functionPath: string, bucketName: string): lambda.IFunction {
  const logicalName = 'ThumbLambda';
  const code = lambda.Code.fromAsset(functionPath)
  const lambdaFunction = new lambda.Function(this, logicalName, {
    runtime: lambda.Runtime.NODEJS_18_X,
    handler: 'index.handler',
    code: code,
    environment: {
      DEST_BUCKET_NAME: bucketName,
      FOLDER_INPUT: folderIntput,
      FOLDER_OUTPUT: folderOutput,
      PROCESS_WIDTH: '512',
      PROCESS_HEIGHT: '512'
    }
  });
  return lambdaFunction;
}
```

## Create SNS Topic

```ts
import * as sns from 'aws-cdk-lib/aws-sns';

const snsTopic = this.createSnsTopic(topicName)

createSnsTopic(topicName: string): sns.ITopic{
  const logicalName = "Topic";
  const snsTopic = new sns.Topic(this, logicalName, {
    topicName: topicName
  });
  return snsTopic;
}
```

## Create an SNS Subscription

```ts
import * as s3n from 'aws-cdk-lib/aws-s3-notifications';

this.createSnsSubscription(snsTopic,webhookUrl)

createSnsSubscription(snsTopic: sns.ITopic, webhookUrl: string): sns.Subscription {
  const snsSubscription = snsTopic.addSubscription(
    new subscriptions.UrlSubscription(webhookUrl)
  )
  return snsSubscription;
}
```

## Create S3 Event Notification to SNS

```ts
this.createS3NotifyToSns(folderOutput,snsTopic,bucket)

createS3NotifyToSns(prefix: string, snsTopic: sns.ITopic, bucket: s3.IBucket): void {
  const destination = new s3n.SnsDestination(snsTopic)
  bucket.addEventNotification(
    s3.EventType.OBJECT_CREATED_PUT, 
    destination,
    {prefix: prefix}
  );
}
```

## Create S3 Event Notification to Lambda

```ts
this.createS3NotifyToLambda(folderInput,laombda,bucket)

createS3NotifyToLambda(prefix: string, lambda: lambda.IFunction, bucket: s3.IBucket): void {
  const destination = new s3n.LambdaDestination(lambda);
    bucket.addEventNotification(s3.EventType.OBJECT_CREATED_PUT,
    destination,
    {prefix: prefix}
  )
}
```

## Create Policy for Bucket Access

```ts
const s3ReadWritePolicy = this.createPolicyBucketAccess(bucket.bucketArn)
```

## Create Policy for SNS Publishing

```ts
const snsPublishPolicy = this.createPolicySnSPublish(snsTopic.topicArn)
```

## Attach the Policies to the Lambda Role

```ts
lambda.addToRolePolicy(s3ReadWritePolicy);
lambda.addToRolePolicy(snsPublishPolicy);
```