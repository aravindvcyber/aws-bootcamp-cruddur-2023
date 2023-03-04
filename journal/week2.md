# Week 2 — Distributed Tracing



## Branch

https://github.com/aravindvcyber/aws-bootcamp-cruddur-2023/blob/week-2/journal/week2.md


## Codespaces successfully explored

![Codespaces](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/0gqigivmipwt6nc4th6k.png)

## Open Telemetry (OTEL)

OpenTelemetry is a collection of tools, APIs, and SDKs. Use it to instrument, generate, collect, and export telemetry data (metrics, logs, and traces) to help you analyze your software’s performance and behavior.

I further explored on this using python and JS specificlly  as discussed in this week.

## Honey Comb

Instrument our backend flask application to use Open Telemetry (OTEL) with
Honeycomb.io as the provider

Both JS and flash projects are integrated with honeyecomebe

Ran queries to explore traces within Honeycomb.io

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/xtbcvzhla1r8rmn1ud0y.png)

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/08gs1jj8d8q2rwbzgf4p.png)

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/if33jc0u80bs4laycz8a.png)

## AWS console

Observe X-Ray traces within the AWS Console

## Rollbar

Integrate Rollbar for Error Logging

Both JS and flash projects are integrated with rollbar

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/m1a14p5fxxqn3w2rm60n.png)

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/hqj9loit78wyqu5lo46s.png)



## Error logging
Trigger an error an observe an error with Rollbar

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/e0c87kelo6mfparuxu9o.png)


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/2vumiaqrolaklf3evh7u.png)



![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/2ouwlydevvidwgsfy02i.png)

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/tl7gp1cx047jui1vaok3.png)

## Cloudwatch


Install WatchTower and write a custom logger to send application log data to - CloudWatch Log group


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/vuat4yqzcleveg815c3h.png)




![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/3v0spsu054w771u7xhem.png)

## X-ray

Instrument AWS X-Ray into backend flask application


![XRay Insights](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4w6qpegatjjmkct4dem1.png)


## X-ray daemon

Configure and provision X-Ray daemon within docker-compose and send data back to X-Ray API

![X-ray daemon](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/0gqigivmipwt6nc4th6k.png)

## Github  actions to be consistent

![CI/CD](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/2mc47mb4ugbnwbf8wt6x.png)


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1wjxqn5hy0cvdyfyjogl.png)

Posted to rollbar on version and deployment changes



![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/cv6oihrcj3fsm8j3g8qq.png)


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/rqkn3viwaa3zreb4wnj1.png)
















