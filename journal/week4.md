# Week 4 — Postgres and RDS

Branch: https://github.com/aravindvcyber/aws-bootcamp-cruddur-2023/tree/week-4

Page: https://github.com/aravindvcyber/aws-bootcamp-cruddur-2023/blob/week-4/journal/week4.md

### Provisioned an RDS instance
![rds available](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/e07eubr60olvvcfejf3w.png)

### Temporarily stopped an RDS instance
![rds stopped](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/td0gviit84504kkcfn56.png)


### Programmatically updated a security group rule

![gitpod task for saving gitpod id](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/sp4oz2l847ovs021v77t.png)

![gitpod ip allow in sg](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/cme3r4x789x933kwzwaw.png)

### Remotely connectted to RDS instance in gitpod and local

![connect to rds from gitpod](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/17a9kkke6rfne4o96ltf.png)

![connect to rds from local psql](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/95nbtie3shptwwgkmi61.png)

### Written necessary bash scripts for database operations

![bash scripts for database operations](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/56q2nb5p29r63ow4gu3o.png)

### Operate common SQL commands using psql client

![sample commands](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/hjfo7hi9rzdwt63j4dgx.png)


### Create a schema SQL file by hand


`backend-flask/db/schema.sql`

### Work with UUIDs and PSQL extensions

![list extensions](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ukt0quok5kumzggeo929.png)

![list extensions functions](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/g375wwpw1e2ze5mj6vye.png)

### Implemented a postgres client for python using a connection pool

`backend-flask/lib/db.py`

### Troubleshooted common SQL errors based on the error seen in the log

![rollbar backend error](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/l38wktztd5lekxllahm9.png)

#### sample example pgerror

![sample example pgerror](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/v95o9p8wymzcdawgbofa.png)

### Implemented a Lambda that runs in a VPC and commits code to RDS

![lambda runtime](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/lahn2ohdzx9sbsp6wfad.png)

![cognito post confirmation trigger](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/en93c7ymv8ajwy66o6av.png)


![lambda ec2 network permissions inside vpc](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qdxhye6xjgjq26wmoos8.png)


![lambda vpc security group](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5pglv82six3jzpul00dc.png)



![test event](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/nhswvi3bnwsjhgadw7l8.png)


![cloudwatch log](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/grllsd28bepx5luwl215.png)

#### Work with PSQL json functions to directly return json from the database


![wrapper functions json](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/h0jhvgwyn4tiqnojwyig.png)


### Correctly sanitize parameters passed to SQL to execute

![sanitize with parameters](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/dxdqli75di3i322jcjgu.png)






### To connect to psql via the psql client cli tool remember to use the host flag to specific localhost.




### Other notes taken based on the session in this bootcamp


```
psql -Upostgres --host localhost
```

Common PSQL commands:

```sql
\x on -- expanded display when looking at data
\q -- Quit PSQL
\l -- List all databases
\c database_name -- Connect to a specific database
\dt -- List all tables in the current database
\d table_name -- Describe a specific table
\du -- List all users and their roles
\dn -- List all schemas in the current database
CREATE DATABASE database_name; -- Create a new database
DROP DATABASE database_name; -- Delete a database
CREATE TABLE table_name (column1 datatype1, column2 datatype2, ...); -- Create a new table
DROP TABLE table_name; -- Delete a table
SELECT column1, column2, ... FROM table_name WHERE condition; -- Select data from a table
INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...); -- Insert data into a table
UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition; -- Update data in a table
DELETE FROM table_name WHERE condition; -- Delete data from a table
```

## Create (and dropping) our database

We can use the createdb command to create our database:

https://www.postgresql.org/docs/current/app-createdb.html

```
createdb cruddur -h localhost -U postgres
```

```sh
psql -U postgres -h localhost
```

```sql
\l
DROP database cruddur;
```

We can create the database within the PSQL client

```sql
CREATE database cruddur;
```

## Import Script

We'll create a new SQL file called `schema.sql`
and we'll place it in `backend-flask/db`

The command to import:
```
psql cruddur < db/schema.sql -h localhost -U postgres
```


## Add UUID Extension

We are going to have Postgres generate out UUIDs.
We'll need to use an extension called:

```sql
CREATE EXTENSION "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
```

## Create our tables

https://www.postgresql.org/docs/current/sql-createtable.html

```sql
CREATE TABLE public.users (
  uuid UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  display_name text,
  handle text
  cognito_user_id text,
  created_at TIMESTAMP default current_timestamp NOT NULL
);
```

```sql
CREATE TABLE public.activities (
  uuid UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  message text NOT NULL,
  replies_count integer DEFAULT 0,
  reposts_count integer DEFAULT 0,
  likes_count integer DEFAULT 0,
  reply_to_activity_uuid integer,
  expires_at TIMESTAMP,
  created_at TIMESTAMP default current_timestamp NOT NULL
);
```

```sql
DROP TABLE IF EXISTS public.users;
DROP TABLE IF EXISTS public.activities;
```

# https://aviyadav231.medium.com/automatically-updating-a-timestamp-column-in-postgresql-using-triggers-98766e3b47a0

```sql
DROP FUNCTION IF EXISTS func_updated_at();
CREATE FUNCTION func_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = now();
    RETURN NEW;
END;
$$ language 'plpgsql';
```

```sql
CREATE TRIGGER trig_users_updated_at 
BEFORE UPDATE ON users 
FOR EACH ROW EXECUTE PROCEDURE func_updated_at();
CREATE TRIGGER trig_activities_updated_at 
BEFORE UPDATE ON activities 
FOR EACH ROW EXECUTE PROCEDURE func_updated_at();
```

```sql
DROP TRIGGER IF EXISTS trig_users_updated_at ON users;
DROP TRIGGER IF EXISTS trig_activities_updated_at ON activities;
```

## Shell Script to Connect to DB

For things we commonly need to do we can create a new directory called `bin`

We'll create an new folder called `bin` to hold all our bash scripts.

```sh
mkdir /workspace/aws-bootcamp-cruddur-2023/backend-flask/bin
```

```sh
export CONNECTION_URL="postgresql://postgres:pssword@127.0.0.1:5433/cruddur"
gp env CONNECTION_URL="postgresql://postgres:pssword@127.0.0.1:5433/cruddur"
```

We'll create a new bash script `bin/db-connect`

```sh
#! /usr/bin/bash

psql $CONNECTION_URL
```

We'll make it executable:

```sh
chmod u+x bin/db-connect
```

To execute the script:
```sh
./bin/db-connect
```

## Shell script to drop the database

`bin/db-drop`

```sh
#! /usr/bin/bash

NO_DB_CONNECTION_URL=$(sed 's/\/cruddur//g' <<<"$CONNECTION_URL")
psql $NO_DB_CONNECTION_URL -c "DROP database cruddur;"
```

https://askubuntu.com/questions/595269/use-sed-on-a-string-variable-rather-than-a-file

## See what connections we are using

```sh
NO_DB_CONNECTION_URL=$(sed 's/\/cruddur//g' <<<"$CONNECTION_URL")
psql $NO_DB_CONNECTION_URL -c "select pid as process_id, \
       usename as user,  \
       datname as db, \
       client_addr, \
       application_name as app,\
       state \
from pg_stat_activity;"
```

> We could have idle connections left open by our Database Explorer extension, try disconnecting and checking again the sessions 

## Shell script to create the database

`bin/db-create`

```sh
#! /usr/bin/bash

NO_DB_CONNECTION_URL=$(sed 's/\/cruddur//g' <<<"$CONNECTION_URL")
createdb cruddur $NO_DB_CONNECTION_URL
```

## Shell script to load the schema

`bin/db-schema-load`

```sh
#! /usr/bin/bash

schema_path="$(realpath .)/db/schema.sql"

echo $schema_path

NO_DB_CONNECTION_URL=$(sed 's/\/cruddur//g' <<<"$CONNECTION_URL")
psql $NO_DB_CONNECTION_URL cruddur < $schema_path
```

## Shell script to load the seed data

```
#! /usr/bin/bash

#echo "== db-schema-load"


schema_path="$(realpath .)/db/schema.sql"

echo $schema_path

psql $CONNECTION_URL cruddur < $schema_path
```

## Easily setup (reset) everything for our database


```sh
#! /usr/bin/bash
-e # stop if it fails at any point

#echo "==== db-setup"

bin_path="$(realpath .)/bin"

source "$bin_path/db-drop"
source "$bin_path/db-create"
source "$bin_path/db-schema-load"
source "$bin_path/db-seed"
```

## Make prints nicer

We we can make prints for our shell scripts coloured so we can see what we're doing:

https://stackoverflow.com/questions/5947742/how-to-change-the-output-color-of-echo-in-linux


```sh
CYAN='\033[1;36m'
NO_COLOR='\033[0m'
LABEL="db-schema-load"
printf "${CYAN}== ${LABEL}${NO_COLOR}\n"
```

## Install Postgres Client

We need to set the env var for our backend-flask application:

```yml
  backend-flask:
    environment:
      CONNECTION_URL: "${CONNECTION_URL}"
```

https://www.psycopg.org/psycopg3/

We'll add the following to our `requirments.txt`

```
psycopg[binary]
psycopg[pool]
```

```
pip install -r requirements.txt
```

## DB Object and Connection Pool


`lib/db.py`

```py
from psycopg_pool import ConnectionPool
import os

def query_wrap_object(template):
  sql = '''
  (SELECT COALESCE(row_to_json(object_row),'{}'::json) FROM (
  {template}
  ) object_row);
  '''

def query_wrap_array(template):
  sql = '''
  (SELECT COALESCE(array_to_json(array_agg(row_to_json(array_row))),'[]'::json) FROM (
  {template}
  ) array_row);
  '''

connection_url = os.getenv("CONNECTION_URL")
pool = ConnectionPool(connection_url)
```

In our home activities we'll replace our mock endpoint with real api call:

```py
from lib.db import pool, query_wrap_array

      sql = query_wrap_array("""
      SELECT
        activities.uuid,
        users.display_name,
        users.handle,
        activities.message,
        activities.replies_count,
        activities.reposts_count,
        activities.likes_count,
        activities.reply_to_activity_uuid,
        activities.expires_at,
        activities.created_at
      FROM public.activities
      LEFT JOIN public.users ON users.uuid = activities.user_uuid
      ORDER BY activities.created_at DESC
      """)
      print(sql)
      with pool.connection() as conn:
        with conn.cursor() as cur:
          cur.execute(sql)
          # this will return a tuple
          # the first field being the data
          json = cur.fetchone()
      return json[0]
```

## Provision RDS Instance

```sh
aws rds create-db-instance \
  --db-instance-identifier cruddur-db-instance \
  --db-instance-class db.t3.micro \
  --engine postgres \
  --engine-version  14.6 \
  --master-username root \
  --master-user-password huEE33z2Qvl383 \
  --allocated-storage 20 \
  --availability-zone ca-central-1a \
  --backup-retention-period 0 \
  --port 5432 \
  --no-multi-az \
  --db-name cruddur \
  --storage-type gp2 \
  --publicly-accessible \
  --storage-encrypted \
  --enable-performance-insights \
  --performance-insights-retention-period 7 \
  --no-deletion-protection
```

> This will take about 10-15 mins

We can temporarily stop an RDS instance for 4 days when we aren't using it.

## Connect to RDS via Gitpod

In order to connect to the RDS instance we need to provide our Gitpod IP and whitelist for inbound traffic on port 5432.

```sh
GITPOD_IP=$(curl ifconfig.me)
```

We'll create an inbound rule for Postgres (5432) and provide the GITPOD ID.

We'll get the security group rule id so we can easily modify it in the future from the terminal here in Gitpod.

```sh
export DB_SG_ID="sg-0b725ebab7e25635e"
gp env DB_SG_ID="sg-0b725ebab7e25635e"
export DB_SG_RULE_ID="sgr-070061bba156cfa88"
gp env DB_SG_RULE_ID="sgr-070061bba156cfa88"
```

Whenever we need to update our security groups we can do this for access.
```sh
aws ec2 modify-security-group-rules \
    --group-id $DB_SG_ID \
    --security-group-rules "SecurityGroupRuleId=$DB_SG_RULE_ID,SecurityGroupRule={IpProtocol=tcp,FromPort=5432,ToPort=5432,CidrIpv4=$GITPOD_IP/32}"
```

https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-security-group-rules.html#examples

## Test remote access

We'll create a connection url:

```
postgresql://root:***********@cruddur-db-instance.***********.ap-south-1.rds.amazonaws.com:5433/cruddur
```

We'll test that it works in Gitpod:

```sh
psql postgresql://root:***********@cruddur-db-instance.***********.ap-south-1.rds.amazonaws.com:5432/cruddur
```

We'll update your URL for production use case

```sh
export PROD_CONNECTION_URL="postgresql://root:***********@cruddur-db-instance.***********.ap-south-1.rds.amazonaws.com:5432/cruddur"
gp env PROD_CONNECTION_URL="postgresql://root:***********@cruddur-db-instance.***********.ap-south-1.rds.amazonaws.com:5432/cruddur"
```

## Update Bash scripts for production

```sh
if [ "$1" = "prod" ]; then
  echo "Running in production mode"
else
  echo "Running in development mode"
fi
```

We'll update:
- db-connect
- db-schema-load

## Update Gitpod IP on new env var

We'll add a command step for postgres:

```sh
    command: |
      export GITPOD_IP=$(curl ifconfig.me)
      source "$THEIA_WORKSPACE_ROOT/backend-flask/db-update-sg-rule"
```


## Setup Cognito post confirmation lambda

### Create the handler function

- Create lambda in same vpc as rds instance Python 3.8
- Add a layer for psycopg2 with one of the below methods for development or production 

ENV variables needed for the lambda environment.
```
PG_HOSTNAME='cruddur-db-instance.***********.ap-south-1.rds.amazonaws.com'
PG_DATABASE='cruddur'
PG_USERNAME='root'
PG_PASSWORD='***********'
```

The function

```
import json
import psycopg2

def lambda_handler(event, context):
    user = event['request']['userAttributes']
    try:
        conn = psycopg2.connect(
            host=(os.getenv('PG_HOSTNAME')),
            database=(os.getenv('PG_DATABASE')),
            user=(os.getenv('PG_USERNAME')),
            password=(os.getenv('PG_SECRET'))
        )
        cur = conn.cursor()
        cur.execute("INSERT INTO users (display_name, handle, cognito_user_id) VALUES(%s, %s, %s)", (user['name'], user['email'], user['sub']))
        conn.commit() 

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            cur.close()
            conn.close()
            print('Database connection closed.')

    return event
```

### Development
https://github.com/AbhimanyuHK/aws-psycopg2

`
This is a custom compiled psycopg2 C library for Python. Due to AWS Lambda missing the required PostgreSQL libraries in the AMI image, we needed to compile psycopg2 with the PostgreSQL libpq.so library statically linked libpq library instead of the default dynamic link.
`

`EASIEST METHOD`

Some precompiled versions of this layer are available publicly on AWS freely to add to your function by ARN reference.

https://github.com/jetbridge/psycopg2-lambda-layer

- Just go to Layers + in the function console and add a reference for your region

`arn:aws:lambda:ca-central-1:898466741470:layer:psycopg2-py38:1`


Alternatively you can create your own development layer by downloading the psycopg2-binary source files from https://pypi.org/project/psycopg2-binary/#files

- Download the package for the lambda runtime environment: [psycopg2_binary-2.9.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl](https://files.pythonhosted.org/packages/36/af/a9f06e2469e943364b2383b45b3209b40350c105281948df62153394b4a9/psycopg2_binary-2.9.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl)

- Extract to a folder, then zip up that folder and upload as a new lambda layer to your AWS account

### Production

Follow the instructions on https://github.com/AbhimanyuHK/aws-psycopg2 to compile your own layer from postgres source libraries for the desired version.


## Add the function to Cognito 

Under the user pool properties add the function as a `Post Confirmation` lambda trigger.