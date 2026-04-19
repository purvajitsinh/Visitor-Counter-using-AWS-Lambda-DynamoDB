# Visitor Counter using AWS Lambda + DynamoDB

A serverless visitor counter web application built using AWS services.  
This project increases the visitor count each time the website is opened and displays the count in real time.

## Technologies Used
- AWS Lambda
- Amazon DynamoDB
- API Gateway
- Amazon S3
- HTML
- CSS
- JavaScript

## Features
- Real-time visitor count
- Serverless architecture
- Static website hosting on S3
- API integration with Lambda
- Data storage using DynamoDB

## Project Architecture
S3 Website → API Gateway → Lambda → DynamoDB

## How It Works
1. User opens website
2. JavaScript calls API Gateway
3. API triggers Lambda function
4. Lambda updates count in DynamoDB
5. Latest visitor count shown on website
