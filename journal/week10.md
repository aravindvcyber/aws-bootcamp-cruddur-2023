# Week 10 — CloudFormation Part 1 & 2


Before you run any templates, be sure to create an S3 bucket to contain
all of our artifacts for CloudFormation.

```sh
aws s3 mk s3://cfn-sandbox-artifacts
export CFN_BUCKET="cfn-sandbox-artifacts"
gp env CFN_BUCKET="cfn-sandbox-artifacts"
```

> remember bucket names are unique to the provide code example you may need to adjust