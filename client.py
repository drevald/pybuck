import boto3

client = boto3.client('s3',
        aws_access_key_id='xxx',                    # same as in resource creation script create.sh  
        aws_secret_access_key= 'xxx',               # same as in resource creation script create.sh  
        endpoint_url='http://192.168.0.198:4566',   # my laptop address where docker engine is running
        region_name='us-east-1')                    # same as in resource creation script create.sh  

response = client.list_buckets()

assert (response['Buckets'][0]['Name']) == 'my-bucket'  # check that bucket exist

client.put_object(Bucket='my-bucket', Key='something', Body='three apples two lemons')  # put something to it

bucket_response = client.get_object(Bucket='my-bucket', Key='something') # get something from it

body = bucket_response['Body']

assert (body.read()).decode('utf-8') == 'three apples two lemons' # check stored content
