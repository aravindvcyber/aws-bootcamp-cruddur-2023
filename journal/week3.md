# Week 3 — Decentralized Authentication

This week branch

https://github.com/aravindvcyber/aws-bootcamp-cruddur-2023/tree/week-3

## Provision via ClickOps a Amazon Cognito User Pool


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/3tll9lh67dfoamqlnb2v.png)

To set password for a specific user

```sh
aws cognito-idp admin-set-user-password --user-pool-id $AWS_COGNITO_USER_POOL_ID --username test --password ***** --permanent
```


Install and configure Amplify client-side library for Amazon Congito

```sh
npm install --save aws-amplify
```

In backend python using th ebelow package and custom lib for jwt

`Flask-AWSCognito`



## Implemented API calls to Amazon Coginto for custom login, signup, 
recovery and forgot password page


### Signup

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/mzhlpf4ggtg9rykqmek5.png)


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5hpzhpkeb01x7w979q3c.png)


### Forgot password

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/vixoruc9kvj08mo4vte0.png)


### Recovery


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/jb9fpem2ccqszyna717a.png)






Login

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/gzcvzh479y21ztq3i3sy.png)

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zjxl83y86grpwcmvrgyz.png)








Confirmation

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/i4y17fbtsq29b7ssxs86.png)



## Show conditional elements and data based on logged in or logged out



![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/efbi7k2j53ejpcejq3nz.png)


### Verify JWT Token server side to serve authenticated API endpoints in Flask Application

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/3x7k2931izvksj4xqrgh.png)