# Week 1 — App Containerization

## Starting the docker compose after updating the docker compose file


![containers-up](/journal/week1/containers-up.png "containers-up").

![docker-compose-started](/journal/week1/docker-compose-started.png "docker-compose-started").



## Validating the port and making frontend and backend public to test


![docker ports up](/journal/week1/ports-active.png "docker ports up").

![front end first look](/journal/week1/front-end-first-strt.png "front end first look").


## creating dynamodb schema




```sh
aws dynamodb create-table \
    --endpoint-url http://localhost:8000 \
    --table-name Music \
    --attribute-definitions \
        AttributeName=Artist,AttributeType=S \
        AttributeName=SongTitle,AttributeType=S \
    --key-schema AttributeName=Artist,KeyType=HASH AttributeName=SongTitle,KeyType=RANGE \
    --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 \
    --table-class STANDARD
```


```sh
aws dynamodb put-item \
    --endpoint-url http://localhost:8000 \
    --table-name Music \
    --item \
        '{"Artist": {"S": "No One You Know"}, "SongTitle": {"S": "Call Me Today"}, "AlbumTitle": {"S": "Somewhat Famous"}}' \
    --return-consumed-capacity TOTAL
```  


```sh
aws dynamodb list-tables --endpoint-url http://localhost:8000
```


```sh
aws dynamodb scan --table-name Music --query "Items" --endpoint-url http://localhost:8000
```

![dynamodb scan](/journal/week1/dynamodb-scan.png "dynamodb scan").


## set up local psl client and connection

![psql client cli instal](/journal/week1/psql-client-cli.png "psql client cli instal").

![psql localhost connection issue](/journal/week1/psql-connection-issue.png "psql localhost connection issue").

![psql cli connected](/journal/week1/psql-connected.png "psql cli connected").

![psql client extension](/journal/week1/psql-client-extension.png "psql client extension").


## Github Actions pipelines

I have additionally setup workflows to build and test python and react projects to validate push and pull to main branch

![github actions workflow](/journal/week1/github-actions.png "github actions workflow").

### Sample pipeline executions


![push-pull-pipelines](/journal/week1/push-pull-pipelines.png "push-pull-pipelines").

![push and pull pipelines for main branch 2](/journal/week1/push-pull-pipelines2.png "push and pull pipelines for main branch 2").


## Setup vulnerability scanning synk

also fixed with a vulnerability based on security lessons learned

https://github.com/aravindvcyber/aws-bootcamp-cruddur-2023/pull/6

![synk pr](/journal/week1/synk-pr.png "synk pr").

![synk pr pass](/journal/week1/synk-pr-pass.png "synk pr pass").


![budget created](/journal/week1/readme-api-full.png "readme-api-full").
![budget created](/journal/week1/readme-api.png "readme-api").

## Creating new backend api

`/api/activities/notifications`

![budget created](/journal/week1/home2.png "crudder home").

![budget created](/journal/week1/notifications.png "crudder notifications").