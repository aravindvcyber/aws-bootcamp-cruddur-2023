# Week 6 & 7  — Deploying Containers with Fargate

Branch https://github.com/aravindvcyber/aws-bootcamp-cruddur-2023/tree/week-6

Readme since I could not add every commits more detail customised here

https://github.com/aravindvcyber/aws-bootcamp-cruddur-2023/blob/week-6/journal/week6.md

https://cruddur.sandbox.exploringserverless.com/

Here is the site: Do checkout, let me know some comments



## Summary with inline notes

* Deployed ECS Cluster using ECS Service Connect
* Deployed serverless containers using Fargate for the Backend and Frontend Application

* Routed traffic to the frontend and backend on different subdomains using Application Load Balancer
* Secured our flask container
* Created several personal bash utility scripts to easily work with serverless containers.

### Both a domain and setup the app

Setup the ELB to use only 80 and 443
with necessary auto forwarding for my site

![certificate generated](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/kuo5x1pheo4m3l8orv09.png)

![alb listeners](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/blzenbbrv631mfu78ayz.png)

![alb ssl port rules](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8sdac54znqm5f8l9sb09.png)
![alb ssl port rules explained](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/oqfoobuofjcr1q9a3e5u.png)


![domain with ssl](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/dwndcc6751daf961egqk.png)

![domain with ssl 2](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/c2wzr3wubql9zjx4siyc.png)





### 3 Services Attempt

Also I tried to setup three sevices moving out xray demon for some time to see how it behaves

![3 services attempt](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/3wnlsfb480fih6yuwgns.png)

### Container Insights

![container insights 3](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ubgf2f8t5vh28cu0jau4.png)

![container insights 2](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/nkiq86qnabqqunj4ydyl.png)


![container insights](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/13q2j61c0k7ok0zaad4p.png)


Create CloudWatch Log Group

```sh
aws logs create-log-group --log-group-name "/cruddur/cluster"
aws logs put-retention-policy --log-group-name "/cruddur/cluster" --retention-in-days 1
```


![cloudwatch](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/vkr6vctqat0novhtb2jw.png)

Create ECS Cluster

```sh
aws ecs create-cluster \
--cluster-name cruddur \
--service-connect-defaults namespace=cruddur
```

![create cluster](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4no3yhehfnfw7y92s3jz.png)

Get ECS Opitmized EC2 AMI

Get the ECS-optimized AMI for my default region

```sh
aws ssm get-parameters --names /aws/service/ecs/optimized-ami/amazon-linux-2/recommended | jq -r '.Parameters[0].Value' | jq .
```

```sh
aws ssm get-parameters --names /aws/service/ecs/optimized-ami/amazon-linux-2/arm64/recommended --region ap-south-1 | jq -r '.Parameters[0].Value' | jq .
```

```sh
aws ec2 describe-images --owner amazon --filters "Name=description,Values=\"*Amazon Linux AMI 2.0.20230321 x86_64 ECS HVM GP2*\"" --query "Images[?ImageLocation=='amazon/amzn2-ami-minimal-hvm-2.0.20230320.0-arm64-ebs'].ImageId" --output text

ami-0352888a5fa748216
```

```sh
aws ec2 describe-images --owner amazon --filters "Name=description,Values=\"*Amazon Linux AMI 2.0.20230321 arm64 ECS HVM GP2*\"" --query "Images[?ImageLocation=='amazon/amzn2-ami-ecs-hvm-2.0.20230321-arm64-ebs'].ImageId" --region ap-south-1 --output text

ami-02e3648333752dfc5
```

```sh
export ECS_OPTIMIZED_AMI=$(aws ec2 describe-images --owner amazon --filters "Name=description,Values=\"*Amazon Linux AMI 2.0.20230321 x86_64 ECS HVM GP2*\"" --query "Images[?ImageLocation=='amazon/amzn2-ami-ecs-hvm-2.0.20230321-x86_64-ebs'].ImageId" --output text)

```

```sh
export ECS_OPTIMIZED_AMI_ARM=$(aws ec2 describe-images --owner amazon --filters "Name=description,Values=\"*Amazon Linux AMI 2.0.20230321 arm64 ECS HVM GP2*\"" --query "Images[?ImageLocation=='amazon/amzn2-ami-ecs-hvm-2.0.20230321-arm64-ebs'].ImageId" --region ap-south-1 --output text)

```

### Create UserData script that will configure ECS
Base64 encode launching the cluster

```sh
echo '#!/bin/bash\necho "ECS_CLUSTER=cruddur" >> /etc/ecs/ecs.config' | base64 -w 0
```





![describe ecs ami](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/9pkbqc2ggn7kidj2bec4.png)
![create launch template](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/3brpwqhj6d5twgre6wws.png)

![launch template](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/dl4m5vbmom60jqi6d9f1.png)



### Installing sessions manager


![session manager](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/h174rlhwstaenss8qcrj.png)

### Create Instance Profile

We want to be able to shell into the EC2 instance incase for debugging
so we'll want to do this via Sessions Manager.

We'll create an Instance Profile with the needed permissions.

```sh
aws iam create-role --role-name session-manager-role --assume-role-policy-document "{
    \"Version\": \"2012-10-17\",
    \"Statement\": [
        {
            \"Effect\": \"Allow\",
            \"Principal\": {
                \"Service\": \"ec2.amazonaws.com\"
            },
            \"Action\": \"sts:AssumeRole\"
        }
    ]
}"
```

```sh
aws iam create-role --role-name session-manager-role --assume-role-policy-document file://aws/policies/service-assume-role-execution-policy.json
```

```sh
aws iam attach-role-policy --policy-arn arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role --role-name session-manager-role
aws iam attach-role-policy --policy-arn arn:aws:iam::aws:policy/AmazonEC2ContainerServiceforEC2Role --role-name session-manager-role


```


arn:aws:iam::197942459570:instance-profile/cruddur-instance-profile

gp env ECS_INSTANCE_PROFILE_ARN=arn:aws:iam::197942459570:instance-profile/cruddur-instance-profile

Get instance profile arn after creation
```sh
export ECS_INSTANCE_PROFILE_ARN=$(aws iam get-instance-profile \
--instance-profile-name cruddur-instance-profile \
--query 'InstanceProfile.Arn' \
--output text)
```

```sh
aws iam add-role-to-instance-profile --instance-profile-name cruddur-instance-profile --role-name session-manager-role
```
### Create Launch Template Security Group

We need the default VPC ID
```sh
export DEFAULT_VPC_ID=$(aws ec2 describe-vpcs \
--filters "Name=isDefault, Values=true" \
--query "Vpcs[0].VpcId" \
--output text)
echo $DEFAULT_VPC_ID
```



Create Cluster Security Group
```sh
export CRUD_CLUSTER_SG=$(aws ec2 create-security-group \
  --group-name cruddur-ecs-cluster-sg \
  --description "Security group for Cruddur ECS ECS cluster" \
  --vpc-id $DEFAULT_VPC_ID \
  --query "GroupId" --output text)
echo $CRUD_CLUSTER_SG
```

Get the Group ID (after its created)

```sh
export CRUD_CLUSTER_SG=$(aws ec2 describe-security-groups \
--group-names cruddur-ecs-cluster-sg \
--query 'SecurityGroups[0].GroupId' \
--output text)
```


![alb security group changes making only 80 and 443 public](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/07b3crrp7o1eakh053g2.png)


### Create Launch Template

WE NEED TO HAVE A KEY PAIR SET.
We can using Sessions Manager without incurring cost when we use the NAT instance.

```sh
aws ec2 create-launch-template \
--launch-template-name cruddur-lt \
--version-description "Launch Template for Cruddur ECS EC2 Cluster" \
--launch-template-data "{
    \"ImageId\": \"$ECS_OPTIMIZED_AMI\",
    \"InstanceType\": \"t3.micro\",
    \"SecurityGroupIds\": [\"$CRUD_CLUSTER_SG\"],
    \"IamInstanceProfile\": {
        \"Arn\": \"$ECS_INSTANCE_PROFILE_ARN\"
    },
    \"UserData\": \"$(printf '#!/bin/bash\necho "ECS_CLUSTER=cruddur" >> /etc/ecs/ecs.config' | base64 -w 0)\"
}"
```

```sh
aws ec2 create-launch-template \
--launch-template-name cruddur-lt-arm \
--version-description "Launch Template for Cruddur ECS EC2 ARM64 Cluster" \
--launch-template-data "{
    \"ImageId\": \"$ECS_OPTIMIZED_AMI_ARM\",
    \"InstanceType\": \"t4g.micro\",
    \"SecurityGroupIds\": [\"$CRUD_CLUSTER_SG\"],
    \"IamInstanceProfile\": {
        \"Arn\": \"$ECS_INSTANCE_PROFILE_ARN\"
    },
    \"UserData\": \"$(printf '#!/bin/bash\necho "ECS_CLUSTER=cruddur" >> /etc/ecs/ecs.config' | base64 -w 0)\"
}"
```

![both launch types](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7g40layhja50i8q7fuyt.png)
## Create ASG

We need an Auto Scaling Group so that if we need to add more EC2 instance we have the capacity to run them.


### Get Subnet Ids as commans

We need the subnet ids for both when we launch the container service but for the ASG

```sh
export DEFAULT_SUBNET_IDS=$(aws ec2 describe-subnets  \
 --filters Name=vpc-id,Values=$DEFAULT_VPC_ID \
 --query 'Subnets[*].SubnetId' \
 --output json | jq -r 'join(",")')
echo $DEFAULT_SUBNET_IDS
```

subnet-09027c709eff3144b,subnet-0359ee57f38e3aca6,subnet-074c1e21ea860b6d4

### Create the ASG
```sh
aws autoscaling create-auto-scaling-group \
--auto-scaling-group-name cruddur-asg \
--launch-template "LaunchTemplateName=cruddur-lt,Version=\$Latest" \
--min-size 1 \
--max-size 1 \
--desired-capacity 1 \
--vpc-zone-identifier $DEFAULT_SUBNET_IDS
```

```sh
aws autoscaling create-auto-scaling-group \
--auto-scaling-group-name cruddur-asg-arm \
--launch-template "LaunchTemplateName=cruddur-lt-arm,Version=\$Latest" \
--min-size 1 \
--max-size 1 \
--desired-capacity 1 \
--vpc-zone-identifier $DEFAULT_SUBNET_IDS
```

![cruddur asg](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/x8zbnhjayjrfy724n7we.png)




![both asg](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/mfx2ktnsxzhm1i3pxi4w.png)

![asg instances both types](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/cqcrydffo1kjp0jwk9px.png)

## Debugging association of EC2 Instance with Cluster (optional)

If we don't see out EC2 instance associated with our cluster.
We can use sessions manger to login.

```sh
sudo su - ec2-user
/etc/ecs/ecs.config
cat /etc/ecs/ecs.config
systemctl status ecs
```

Consider that we have access to docker and we can see any running containers or shell into them eg:

```sh
docker ps
docker exec -it <container name> /bin/bash
```

## Create ECR repo and push image

### Login to ECR

```sh
aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin "$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com"

or 

AWS_ECR_PASSWORD=$(aws ecr get-login-password --region $AWS_DEFAULT_REGION)
echo $AWS_ECR_PASSWORD | docker login --username AWS --password-stdin $IMAGE_URL

```

![ecr login](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/mk8wwswxnhjjh5bu9lto.png)


### For Base-image python

```sh
aws ecr create-repository \
  --repository-name cruddur-python \
  --image-tag-mutability MUTABLE
```

![ecr repo 1](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zgwj1ixt8euh6h7pkzk4.png)

#### Set URL

```sh
export ECR_PYTHON_URL="$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/cruddur-python"
echo $ECR_PYTHON_URL
```
![ecr repo 2](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/rrora6zutt4upgc9d462.png)
#### Pull Image

```sh
docker pull python:3.10-slim-buster
```

#### Tag Image

```sh
docker tag python:3.10-slim-buster $ECR_PYTHON_URL:3.10-slim-buster
```

#### Push Image

```sh
docker push $ECR_PYTHON_URL:3.10-slim-buster
```

### For Flask

In your flask dockerfile update the from to instead of using DockerHub's python image
you use your own eg.

> remember to put the :latest tag on the end

#### Create Repo
```sh
aws ecr create-repository \
  --repository-name backend-flask \
  --image-tag-mutability MUTABLE
```

#### Set URL

```sh
export ECR_BACKEND_FLASK_URL="$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/backend-flask"
echo $ECR_BACKEND_FLASK_URL
```

#### Build Image
```sh
docker build -t backend-flask .
```

#### Tag Image

```sh
docker tag backend-flask:latest $ECR_BACKEND_FLASK_URL:latest
```

#### Push Image

```sh
docker push $ECR_BACKEND_FLASK_URL:latest
```

### For Frontend React

#### Create Repo
```sh
aws ecr create-repository \
  --repository-name frontend-react-js \
  --image-tag-mutability MUTABLE
```

#### Set URL

```sh
export ECR_FRONTEND_REACT_URL="$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/frontend-react-js"
echo $ECR_FRONTEND_REACT_URL
```

#### Build Image

```sh
docker build \
--build-arg REACT_APP_BACKEND_URL="http://${AWS_ELB}:4567" \
--build-arg REACT_APP_AWS_PROJECT_REGION="$AWS_DEFAULT_REGION" \
--build-arg REACT_APP_AWS_COGNITO_REGION="$AWS_DEFAULT_REGION" \
--build-arg REACT_APP_AWS_USER_POOLS_ID="$AWS_USER_POOLS_ID" \
--build-arg REACT_APP_CLIENT_ID="$AWS_COGNITO_USER_POOL_CLIENT_ID" \
-t frontend-react-js \
-f Dockerfile.prod \
.
```

#### Tag Image

```sh
docker tag frontend-react-js:latest $ECR_FRONTEND_REACT_URL:latest
```

#### Push Image

```sh
docker push $ECR_FRONTEND_REACT_URL:latest
```


If you want to run and test it

```sh
docker run --rm -p 3000:3000 -it frontend-react-js 
```

## Register Task Defintions

### Passing Senstive Data to Task Defintion

https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data.html
https://docs.aws.amazon.com/AmazonECS/latest/developerguide/secrets-envvar-ssm-paramstore.html

```sh
aws ssm put-parameter --type "SecureString" --name "/cruddur/backend-flask/AWS_ACCESS_KEY_ID" --value $AWS_ACCESS_KEY_ID
aws ssm put-parameter --type "SecureString" --name "/cruddur/backend-flask/AWS_SECRET_ACCESS_KEY" --value $AWS_SECRET_ACCESS_KEY
aws ssm put-parameter --type "SecureString" --name "/cruddur/backend-flask/CONNECTION_URL" --value $PROD_CONNECTION_URL
aws ssm put-parameter --type "SecureString" --name "/cruddur/backend-flask/ROLLBAR_ACCESS_TOKEN" --value $ROLLBAR_ACCESS_TOKEN
aws ssm put-parameter --type "SecureString" --name "/cruddur/backend-flask/OTEL_EXPORTER_OTLP_HEADERS" --value "x-honeycomb-team=$HONEYCOMB_API_KEY"
```

### Create Task and Exection Roles for Task Defintion


#### Create ExecutionRole

```sh
aws iam create-role \
    --role-name CruddurServiceExecutionRole \
    --assume-role-policy-document "{
  \"Version\":\"2012-10-17\",
  \"Statement\":[{
    \"Action\":[\"sts:AssumeRole\"],
    \"Effect\":\"Allow\",
    \"Principal\":{
      \"Service\":[\"ecs-tasks.amazonaws.com\"]
    }
  }]
}"
```

```json

       {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "ssm:GetParameter",
            "Resource": "arn:aws:ssm:ap-south-1:197942459570:parameter/cruddur/backend-flask/*"
        }

```sh
aws iam attach-role-policy \
    --policy-arn arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy \
    --role-name CruddurServiceExecutionRole
```

```json
{
  "Sid": "VisualEditor0",
  "Effect": "Allow",
  "Action": [
    "ssm:GetParameters",
    "ssm:GetParameter"
  ],
  "Resource": "arn:aws:ssm:ap-south-1:197942459570:parameter/cruddur/backend-flask/*"
}
```

```sh
aws iam put-role-policy \
  --policy-name SSMAccessPolicyParams \
  --role-name CruddurServiceExecutionRole \
  --policy-document file:///aws/policies/service-execution-policy.json
```

#### Create TaskRole

```sh
aws iam create-role \
    --role-name CruddurTaskRole \
    --assume-role-policy-document "{
  \"Version\":\"2012-10-17\",
  \"Statement\":[{
    \"Action\":[\"sts:AssumeRole\"],
    \"Effect\":\"Allow\",
    \"Principal\":{
      \"Service\":[\"ecs-tasks.amazonaws.com\"]
    }
  }]
}"

aws iam put-role-policy \
  --policy-name SSMAccessPolicy \
  --role-name CruddurTaskRole \
  --policy-document "{
  \"Version\":\"2012-10-17\",
  \"Statement\":[{
    \"Action\":[
      \"ssmmessages:CreateControlChannel\",
      \"ssmmessages:CreateDataChannel\",
      \"ssmmessages:OpenControlChannel\",
      \"ssmmessages:OpenDataChannel\"
    ],
    \"Effect\":\"Allow\",
    \"Resource\":\"*\"
  }]
}
"

aws iam attach-role-policy --policy-arn arn:aws:iam::aws:policy/CloudWatchFullAccess --role-name CruddurTaskRole
aws iam attach-role-policy --policy-arn arn:aws:iam::aws:policy/AWSXRayDaemonWriteAccess --role-name CruddurTaskRole
```

### Create Json file
Create a new folder called `aws/task-defintions` and place the following files in there:

`backend-flask.json`

```json
{
  "family": "backend-flask",
  "executionRoleArn": "arn:aws:iam::AWS_ACCOUNT_ID:role/CruddurServiceExecutionRole",
  "taskRoleArn": "arn:aws:iam::AWS_ACCOUNT_ID:role/CruddurTaskRole",
  "networkMode": "awsvpc",
  "containerDefinitions": [
    {
      "name": "backend-flask",
      "image": "BACKEND_FLASK_IMAGE_URL",
      "cpu": 256,
      "memory": 512,
      "essential": true,
      "portMappings": [
        {
          "name": "backend-flask",
          "containerPort": 4567,
          "protocol": "tcp", 
          "appProtocol": "http"
        }
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
            "awslogs-group": "cruddur",
            "awslogs-region": "ca-central-1",
            "awslogs-stream-prefix": "backend-flask"
        }
      },
      "environment": [
        {"name": "OTEL_SERVICE_NAME", "value": "backend-flask"},
        {"name": "OTEL_EXPORTER_OTLP_ENDPOINT", "value": "https://api.honeycomb.io"},
        {"name": "AWS_COGNITO_USER_POOL_ID", "value": ""},
        {"name": "AWS_COGNITO_USER_POOL_CLIENT_ID", "value": ""},
        {"name": "FRONTEND_URL", "value": ""},
        {"name": "BACKEND_URL", "value": ""},
        {"name": "AWS_DEFAULT_REGION", "value": ""}
      ],
      "secrets": [
        {"name": "AWS_ACCESS_KEY_ID"    , "valueFrom": "arn:aws:ssm:AWS_REGION:AWS_ACCOUNT_ID:parameter/cruddur/backend-flask/AWS_ACCESS_KEY_ID"},
        {"name": "AWS_SECRET_ACCESS_KEY", "valueFrom": "arn:aws:ssm:AWS_REGION:AWS_ACCOUNT_ID:parameter/cruddur/backend-flask/AWS_SECRET_ACCESS_KEY"},
        {"name": "CONNECTION_URL"       , "valueFrom": "arn:aws:ssm:AWS_REGION:AWS_ACCOUNT_ID:parameter/cruddur/backend-flask/CONNECTION_URL" },
        {"name": "ROLLBAR_ACCESS_TOKEN" , "valueFrom": "arn:aws:ssm:AWS_REGION:AWS_ACCOUNT_ID:parameter/cruddur/backend-flask/ROLLBAR_ACCESS_TOKEN" },
        {"name": "OTEL_EXPORTER_OTLP_HEADERS" , "valueFrom": "arn:aws:ssm:AWS_REGION:AWS_ACCOUNT_ID:parameter/cruddur/backend-flask/OTEL_EXPORTER_OTLP_HEADERS" }
        
      ]
    }
  ]
}
```

`frontend-react.json`

```json
{
  "family": "frontend-react-js",
  "executionRoleArn": "arn:aws:iam::AWS_ACCOUNT_ID:role/CruddurServiceExecutionRole",
  "taskRoleArn": "arn:aws:iam::AWS_ACCOUNT_ID:role/CruddurTaskRole",
  "networkMode": "awsvpc",
  "containerDefinitions": [
    {
      "name": "frontend-react-js",
      "image": "BACKEND_FLASK_IMAGE_URL",
      "cpu": 256,
      "memory": 256,
      "essential": true,
      "portMappings": [
        {
          "name": "frontend-react-js",
          "containerPort": 3000,
          "protocol": "tcp", 
          "appProtocol": "http"
        }
      ],

      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
            "awslogs-group": "cruddur",
            "awslogs-region": "ca-central-1",
            "awslogs-stream-prefix": "frontend-react"
        }
      }
    }
  ]
}
```

### Register Task Defintion

```sh
aws ecs register-task-definition --cli-input-json file://aws/task-definitions/backend-flask.json
```


```sh
aws ecs register-task-definition --cli-input-json file://aws/task-definitions/frontend-react-js.json
```
![task def](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/2lof8um6k0t9r95u48ky.png)

![tasks](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/a3rp1czx0qepcgvas9is.png)
### Create Security Group


```sh
export CRUD_SERVICE_SG=$(aws ec2 create-security-group \
  --group-name "crud-srv-sg" \
  --description "Security group for Cruddur services on ECS" \
  --vpc-id $DEFAULT_VPC_ID \
  --query "GroupId" --output text)
echo $CRUD_SERVICE_SG
```


```sh
aws ec2 authorize-security-group-ingress \
  --group-id $CRUD_SERVICE_SG \
  --protocol tcp \
  --port 80 \
  --cidr 0.0.0.0/0
```


> if we need to get the sg group id  again
```sh
export CRUD_SERVICE_SG=$(aws ec2 describe-security-groups \
  --filters Name=group-name,Values=crud-srv-sg \
  --query 'SecurityGroups[*].GroupId' \
  --output text)
```

#### Update RDS SG to allow access for the last security group

```sh
aws ec2 authorize-security-group-ingress \
  --group-id $DB_SG_ID \
  --protocol tcp \
  --port 5432 \
  --source-group $CRUD_SERVICE_SG'


  # --tag-specifications 'ResourceType=security-group,Tags=[{Key=Name,Value=BACKENDFLASK}]
```

### Create Services

```sh
aws ecs create-service --cli-input-json file://aws/json/service-backend-flask.json
```

```sh
aws ecs create-service --cli-input-json file://aws/json/service-frontend-react-js.json
```


![services](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/og1m1b28nllrnb9aiqjc.png)
![services 1](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/w53wxoc4tkr97lpxq7hw.png)


> Auto Assign is not supported by EC2 launch type for services

This is for when we are uing a NetworkMode of awsvpc
> --network-configuration "awsvpcConfiguration={subnets=[$DEFAULT_SUBNET_IDS],securityGroups=[$SERVICE_CRUD_SG],assignPublicIp=ENABLED}"

https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html


### Elastic load balancer from console


![elb listioners](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/3t0gsxd9xcbdsfz7dp2g.png)
![elb access logs](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/eglh0t1ft6usjc67r64m.png)
![target groups](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/kpmm6ctz2lc2ige5tlsg.png)

### Access logs for ELB

Create a bucket and configure policy like this with principal `arn:aws:iam::718504428378:root` for ap-south-1 elb

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Allow-ELB-to-write-logs",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::718504428378:root"
            },
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::access-logs-4-cruddur-alb/AWSLogs/99999999999/*"
        }
    ]
}
```

![s3 log 1](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/d17obnm0hwqiddt9pu0b.png)
![s3 log 2](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/g4nleuzjjdijgvgwl46u.png)




![docker build with args frontend](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/kw7lsbkxbrjnw3hwli2e.png)
![sample authorise ingress for service](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/fif8tue55mfq0yxk5tg3.png)
![authorise db sg 5432](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/peq9ajb054hml5if55jr.png)
![sample access log](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4mmjhsdrh9dci9iapebb.png)



### Test Service

Use sessions manager to connect to the EC2 instance.

#### Test RDS Connection

Shell into the backend flask container and run the `./bin/db/test` script to ensure we have a database connection


#### Test Flask App is running

`./bin/flask/health-check`

Check our forwarding ports for the container

```sh
docker port <CONTAINER_ID>
```

> docker run --rm --link <container_name_or_id>:<alias> curlimages/curl curl <alias>:<port>/<endpoint>

```sh
docker run --rm --link d71eea0b8e93:flask -it curlimages/curl --get -H "Accept: application/json" -H "Content-Type: application/json" http://flask:4567/api/activities/home
```

#### Check endpoiint against Public IP 

```sh
docker run --rm -it curlimages/curl --get -H "Accept: application/json" -H "Content-Type: application/json" http://3.97.113.133/api/activities/home
```


## Not able to use Sessions Manager to get into cluster EC2 sintance

The instance can hang up for various reasons.
You need to reboot and it will force a restart after 5 minutes
So you will have to wait 5 minutes or after a timeout.

You have to use the AWS CLI. 
You can't use the AWS Console. it will not work as expected.

The console will only do a graceful shutdodwn
The CLI will do a forceful shutdown after a period of time if graceful shutdown fails.

```sh
aws ec2 reboot-instances --instance-ids i-0d15aef0618733b6d
```


## Route 53


![route 53](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/0738dw9adgvowue0a7a7.png)


