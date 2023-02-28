# AWS_ADMIN_API
aws admin api for various task

Step1:
Install into pc if you do not have them already.
python, vscode, aws Cli, Postman, boto3.


Step2:
Configure aws cli using aws configure commands. this might help for additional validations.


Step3:
On AWS console, Create a Lambda function, choose python3.7 when creating your Lambda function, attach the appropriate admin permission, increase the Lambda timeout to 15 minutes and deploy the lambda.
Copy and paste the code from this file, lambda.py to you deployed lambda.


Step4:
Create an API using API gateway, create a resource within the API, within the resource setup a method( in this case, the method is a GET method), link your API setup with the Lambda function created in step3
Create token, add the token to the usage plan for security.
Assign the usage plan and token to the api stage then deploy the API.
A URL is generated that can be used to trigger the API


How to use
==================
Open postman, create a new request with Get method and api endpoint url generated in step4.
Pass the body as json, add token in header and hit send button


![newuser-created](https://user-images.githubusercontent.com/126528702/221946239-5bf06b5c-5720-407a-b5d4-b58ffbb61380.PNG)
