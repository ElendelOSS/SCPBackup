import boto3
import botocore
import sys
import os
import datetime

def createClient():
    s3_client = boto3.client('s3', region_name="us-east-1")

    return s3_client

def createKey(server, filesource):
    timestamp = datetime.date.today()
    key = str(timestamp.year) + "/" + str(timestamp.month) + "/" + str(timestamp.day) + "/" + server + "/" + filesource
    
    return key

def write_s3object(data, bucket, key, logging=None):
    
    s3_client = createClient()
    
    try:
        response = s3_client.put_object(
            Body=bytes(data),
            Bucket=bucket,
            Key=key
        )
        if logging:
            print('Written object {} to bucket {}.'.format(key, bucket))

        return response
    
    except Exception as e:
        print(e)
        print('Error writing object {} to bucket {}.'.format(key, bucket))
        raise e
    
def grabConfig(server, filesource):

    fileobj = open('/tmp/' + filesource, "rb")
    data = fileobj.read()
    fileobj.close()

    return data

def backuptoS3(server, filesource, bucket, logging=None):
    
    data = grabConfig(server=server, filesource=filesource)
    key = createKey(server=server, filesource=filesource)
    write_s3object(
        data=data,
        bucket=bucket,
        key=key,
        logging=logging
    )