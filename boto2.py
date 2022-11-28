# This code meets Jira Tix: HIVE-149; https://ecstech.jira.com/jira/software/projects/HIVE/boards/316
# and shares it in github repo: https://github.com/blackstonetech/ecs-capability-repo
# First, Install from command line
# pip install boto3
# (you could try for local install) !pip install boto3
import os
import boto3
# This brings your AWS access key and secret access key from your credentials.py file
import credentials
# to test that you are connected to your credentials.py file:
# print(credentials.my_aws_access_key_id) [you probably will need to copy and paste your credentials into a local copy of credentials.py]
s3obj = boto3.client(
    service_name='s3',
    region_name='us-east-1',
    aws_access_key_id=credentials.my_aws_access_key_id,
    aws_secret_access_key=credentials.my_aws_secret_access_key
)
#
# Reference: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-creating-buckets.html
response = s3obj.list_buckets()
# Output the bucket names
# print('Existing buckets:')
# Print a list of the files in the specified bucket
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')
mybucket = s3obj.list_objects_v2(Bucket='atlas-ppr')
for content in mybucket.get('Contents', []):
    print(content['Key'])
    # optional if you have more filefolders to got through.
    response.append(files)
    return response

get_filenames(my_bucketfolder)
