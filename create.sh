!/bin/bash

echo 'START OF SCRIPT!!!'

aws configure set aws_access_key_id xxx
aws configure set aws_secret_access_key xxx
aws --endpoint-url=http://localhost:4566  s3api create-bucket --bucket my-bucket --region us-east-1

echo 'END OF SCRIPT!!!'