# Week 3 — Decentralized Authentication

This week branch

https://github.com/aravindvcyber/aws-bootcamp-cruddur-2023/tree/week-3

https://github.com/aravindvcyber/aws-bootcamp-cruddur-2023/blob/main/journal/week3.md

## Provisioned via ClickOps a Amazon Cognito User Pool


![Provision via ClickOps](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/3tll9lh67dfoamqlnb2v.png)

To set password for a specific user

```sh
aws cognito-idp admin-set-user-password --user-pool-id $AWS_COGNITO_USER_POOL_ID --username test --password ***** --permanent
```


#### Install and configure Amplify client-side library for Amazon Congito

```sh
npm install --save aws-amplify
```

#### In backend python using th ebelow package and custom lib for jwt

`Flask-AWSCognito`



## Implemented API calls 

>to Amazon Coginto for custom login, signup, recovery and forgot password page



### Signup

![Signup link](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/mzhlpf4ggtg9rykqmek5.png)


![Signup page](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5hpzhpkeb01x7w979q3c.png)


### Forgot password

![forgot password email](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/vixoruc9kvj08mo4vte0.png)


### Recovery


![recovery confirmation](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/jb9fpem2ccqszyna717a.png)


### Login

![Sample login](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/gzcvzh479y21ztq3i3sy.png)

![login home page](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zjxl83y86grpwcmvrgyz.png)





Confirmation

![passcodes for confirmation](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/i4y17fbtsq29b7ssxs86.png)



## Show conditional elements and data based on logged in or logged out

> Besides this I learned customising the UI with css as demonstrated this week

![conditionals](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/efbi7k2j53ejpcejq3nz.png)


### Verify JWT Token server side to serve authenticated API endpoints in Flask Application

![Verify JWT Token](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/3x7k2931izvksj4xqrgh.png)

Here the helper library to verify JWT gave more insights why we need verify them in backend and extract claims, I could imagine lot of possibilities by decrypting using the jwk keys as a generic authorization handler
