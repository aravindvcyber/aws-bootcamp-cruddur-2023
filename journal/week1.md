# Week 1 — App Containerization



![budget created](/journal/week1/containers-up.png "budget created").

![budget created](/journal/week1/docker-compose-started.png "budget created").






![budget created](/journal/week1/ports-active.png "docker ports up").

![budget created](/journal/week1/front-end-first-strt.png "front end first look").


![budget created](/journal/week1/dynamodb-scan.png "dynamodb scan").



```aws dynamodb create-table \
    --endpoint-url http://localhost:8000 \
    --table-name Music \
    --attribute-definitions \
        AttributeName=Artist,AttributeType=S \
        AttributeName=SongTitle,AttributeType=S \
    --key-schema AttributeName=Artist,KeyType=HASH AttributeName=SongTitle,KeyType=RANGE \
    --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 \
    --table-class STANDARD```


```aws dynamodb put-item \
    --endpoint-url http://localhost:8000 \
    --table-name Music \
    --item \
        '{"Artist": {"S": "No One You Know"}, "SongTitle": {"S": "Call Me Today"}, "AlbumTitle": {"S": "Somewhat Famous"}}' \
    --return-consumed-capacity TOTAL```  


```aws dynamodb list-tables --endpoint-url http://localhost:8000```


```aws dynamodb scan --table-name Music --query "Items" --endpoint-url http://localhost:8000```

![budget created](/journal/week1/psql-client-cli.png "psql client cli instalal").

![budget created](/journal/week1/psql-connection-issue.png "psql localhost connection issue").

![budget created](/journal/week1/psql-connected.png "psql cli connected").

![budget created](/journal/week1/psql-client-extension.png "psql client extension").

## Github Actions pipelines

I have additionally setup workflows to build and test python and react projects to validate push and pull to main branch

![budget created](/journal/week1/github-actions.png "github actions workflow").

Sample pipeline executions

![budget created](/journal/week1/push-pull-pipelines.png "push and 
 pull pipelines for main branch 1").

![budget created](/journal/week1/push-pull-pipelines2.png "push and pull pipelines for main branch 2").