# Week 5 — DynamoDB and Serverless Caching

Branch link https://github.com/aravindvcyber/aws-bootcamp-cruddur-2023/tree/week-5

Readme for better view with images https://github.com/aravindvcyber/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md

### Integrated with dynamodb

![messages screen](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/o97w0qgwl0w7z1c40uw6.png)


![table created](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/kptjnmx6ix0cjcf87eoj.png)


![message group](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/3quv3e2jzipe6nb6eowd.png)
![cruddur home from ddb](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zdh703gq3857g4hkpf45.png)


### Data Modelling a Direct Messaging System using Single Table Design 


I have also tried this in NoSQL workbench to query the data and use indexs and GSI


![workbench ops 1](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/x0w0l4f7jlplg7016gy9.png)
![workbench ops 2](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/af9ubk5s66kj0idqc810.png)

### Implemented DynamoDB query using Single Table Design

![query using modeller](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/wbcrppd2mf8steliliv2.png)

![backend connecting to prod](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/43sv115savc1slvwtmrf.png)

![scan or query console](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/z4jdwh23gazcmb9qmvtg.png)


### Provisioning DynamoDB tables with Provisioned Capacity

![table with rcus wcus](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/kptjnmx6ix0cjcf87eoj.png)

### Utilizing a Global Secondary Index (GSI) with DynamoDB

![gsi ddb](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ch1ilhazergx3fwhzhou.png)
### Rapid data modelling and implementation of DynamoDB with DynamoDB Local

![dockers](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/85u44a4krhickylo8zin.png)

![ddb schema load](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/k6pv2cnsj5q7rtl3m9bx.png)

![seed and list tables](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/125fbv3a4aoe40m74gag.png)

### Writing utility scripts to easily setup and teardown and debug DynamoDB data

![utility scripts](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ktndul3wjpncvgog7gns.png)

### Implemented dynamodb steams with VPC endpoint

![stream created](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/sxlb95r8stm9ru08gt1r.png)
![trigger connect with lambda](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/g5hgaqp7meznw3k91sr9.png)

![vpc endpoint for dynamodb](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/lxoyfl1oatex6x4hu6q0.png)

### Implemented the lambda to use VPC endpoint

lambda code

https://github.com/aravindvcyber/aws-bootcamp-cruddur-2023/blob/main/aws/lambda/cruddur-messaging-stream.py

![lambda](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/mondgdy6gwigox9cqcf2.png)
![lambda vpc](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1fstszlquo4vfzstxgx2.png)




customised permission policy for the lambda execution role 

```json 
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "dynamodb:PutItem",
                "dynamodb:DeleteItem",
                "dynamodb:Query"
            ],
            "Resource": [
                "arn:aws:dynamodb:ap-south-1:*******:table/cruddur-messages/index/message-group-sk-index",
                "arn:aws:dynamodb:ap-south-1:*******:table/cruddur-messages"
            ]
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": [
                "lambda:InvokeFunction",
                "dynamodb:GetShardIterator",
                "dynamodb:DescribeStream",
                "dynamodb:GetRecords"
            ],
            "Resource": [
                "arn:aws:dynamodb:ap-south-1:*******:table/cruddur-messages/stream/2023-03-25T18:11:15.897",
                "arn:aws:lambda:ap-south-1:*******:function:cruddur-messaging-stream"
            ]
        },
        {
            "Sid": "VisualEditor2",
            "Effect": "Allow",
            "Action": "dynamodb:ListStreams",
            "Resource": "arn:aws:dynamodb:ap-south-1:*******:table/cruddur-messages"
        }
    ]
}
```

![dynamodb permissions](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/kr4bg28xqn39jk2ejggb.png)
![ec2 permissions](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/e48ok5krr2n7kzijc7ui.png)


### Dynamodb stream is used to trigger lambda

This is used to delete existing messages in a group and recreate them when new messages are posted

![lambda cloudwatch logs seen](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ghhf6lw30ult3uxzlfre.png)

![added some pretty log](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/sma1h77tvcba37m6n34i.png)


# Other notes:

## DynamoDB Bash Scripts

```sh
./bin/ddb/schem-load
```


## The Boundaries of DynamoDB

- When you write a query you have provide a Primary Key (equality) eg. pk = 'andrew'
- Are you allowed to "update" the Hash and Range?
  - No, whenever you change a key (simple or composite) eg. pk or sk you have to create a new item.
    - you have to delete the old one
- Key condition expressions for query only for RANGE, HASH is only equality 
- Don't create UUID for entity if you don't have an access pattern for it


3 Access Patterns

## Pattern A  (showing a single conversation)

A user wants to see a list of messages that belong to a message group
The messages must be ordered by the created_at timestamp from newest to oldest (DESC)

```sql
SELECT
  messages.uuid,
  messages.display_name,
  messages.message,
  messages.handle,
  messages.created_at -- sk
FROM messages
WHERE
  messages.message_group_uuid = {{message_group_uuid}} -- pk
ORDER BY messages.created_at DESC
```

> message_group_uuid comes from Pattern B
## Pattern B (list of conversation)

A user wants to see a list of previous conversations.
These conversations are listed from newest to oldest (DESC)
We want to see the other person we are talking to.
We want to see the last message (from whomever) in summary.

```sql
SELECT
  message_groups.uuid,
  message_groups.other_user_uuid,
  message_groups.other_user_display_name,
  message_groups.other_user_handle,
  message_groups.last_message,
  message_groups.last_message_at
FROM message_groups
WHERE
  message_groups.user_uuid = {{user_uuid}} --pk
ORDER BY message_groups.last_message_at DESC
```

> We need a Global Secondary Index (GSI)
## Pattern C (create a message)

```sql
INSERT INTO messages (
  user_uuid,
  display_name,
  handle,
  creaed_at
)
VALUES (
  {{user_uuid}},
  {{display_name}},
  {{handle}},
  {{created_at}}
);
```

## Pattern D (update a message_group for the last message)

When a user creates a message we need to update the conversation
to display the last message information for the conversation

```sql
UPDATE message_groups
SET 
  other_user_uuid = {{other_user_uuid}}
  other_user_display_name = {{other_user_display_name}}
  other_user_handle = {{other_user_handle}}
  last_message = {{last_message}}
  last_message_at = {{last_message_at}}
WHERE 
  message_groups.uuid = {{message_group_uuid}}
  AND message_groups.user_uuid = {{user_uuid}}
```


## Serverless Caching

### Install Momento CLI tool

In your gitpod.yml file add:

```yml
  - name: momento
    before: |
      brew tap momentohq/tap
      brew install momento-cli
```

### Login to Momento

There is no `login` you just have to generate an access token and not lose it. 
 
You cannot rotate out your access token on an existing cache.

If you lost your cache or your cache was comprised you just have to wait for the TTL to expire.

> It might be possible to rotate out the key by specifcing the same cache name and email.
 ```sh
 momento account signup aws --email aravindv******@gmail.com --region ap-south-1
 ```

### Create Cache

```sh
export MOMENTO_AUTH_TOKEN=""
export MOMENTO_TTL_SECONDS="600"
export MOMENTO_CACHE_NAME="cruddur"
gp env MOMENTO_AUTH_TOKEN=""
gp env MOMENTO_TTL_SECONDS="600"
gp env MOMENTO_CACHE_NAME="cruddur"
```

> you might need to do `momento configure` since it might not pick up the env var in the CLI.
Create the cache:

```sh
momento cache create --name cruddur
```


### DynamoDB Stream trigger to update message groups

- create a VPC endpoint for dynamoDB service on your VPC
- create a Python lambda function in your vpc
- enable streams on the table with 'new image' attributes included
- add your function as a trigger on the stream
- grant the lambda IAM role permission to read the DynamoDB stream events

`AWSLambdaInvocation-DynamoDB`

- grant the lambda IAM role permission to update table items


**The Function**

```.py
import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.resource(
 'dynamodb',
 region_name='ap-south-1',
 endpoint_url="http://dynamodb.ap-south-1.amazonaws.com"
)
def lambda_handler(event, context):
  pk = event['Records'][0]['dynamodb']['Keys']['pk']['S']
  sk = event['Records'][0]['dynamodb']['Keys']['sk']['S']
  if pk.startswith('MSG#'):
    group_uuid = pk.replace("MSG#","")
    message = event['Records'][0]['dynamodb']['NewImage']['message']['S']
    print("GRUP ===>",group_uuid,message)
    
    table_name = 'cruddur-messages'
    index_name = 'message-group-sk-index'
    table = dynamodb.Table(table_name)
    data = table.query(
      IndexName=index_name,
      KeyConditionExpression=Key('message_group_uuid').eq(group_uuid)
    )
    print("RESP ===>",data['Items'])
    
    # recreate the message group rows with new SK value
    for i in data['Items']:
      delete_item = table.delete_item(Key={'pk': i['pk'], 'sk': i['sk']})
      print("DELETE ===>",delete_item)
      
      response = table.put_item(
        Item={
          'pk': i['pk'],
          'sk': sk,
          'message_group_uuid':i['message_group_uuid'],
          'message':message,
          'user_display_name': i['user_display_name'],
          'user_handle': i['user_handle'],
          'user_uuid': i['user_uuid']
        }
      )
      print("CREATE ===>",response)
```

