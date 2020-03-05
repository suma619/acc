import json
from chalicelib.Services.Utility.BackendOperations import get_parameters
from chalicelib.Services.Utility import create_media_convert_job
from chalicelib.Services.Core import initialize_dynamo_db
import boto3
import os
def set_aws_services(region):  
	dynamo_client = boto3.client('dynamodb')
	mc_client = boto3.client('mediaconvert', region_name=region)
	endpoints = mc_client.describe_endpoints()
	med_client = boto3.client('mediaconvert', region_name=region, endpoint_url=endpoints['Endpoints'][0]['Url'], verify=False)
	return med_client,dynamo_client

def set_environment_variables():
	Dynamotb = os.environ['DynamoTB']
	mediaConvertRole = os.environ['MediaConvertRole']
	region = os.environ['Region']
	queue = os.environ['Queue']
	Temp1 = os.environ['JobTemplate']
	return Dynamotb,mediaConvertRole,region,queue,Temp1







def transcode(sourceS3Key,sourceS3Bucket):
	json_parameter=get_parameters.get_parameters(sourceS3Key,sourceS3Bucket)
	json_parameter_data=json.loads(json_parameter)
	#print("des source s3 is",json_parameter_data['sourceS3'])
	
	Dynamotb,mediaConvertRole,region,queue,Temp1=set_environment_variables()

	med_client,dynamo_client=set_aws_services(region)
	jobid,jobinputfile=create_media_convert_job.create_media_convert_job(med_client,Dynamotb,mediaConvertRole,region,queue,Temp1,json_parameter_data)
	initialize_dynamo_db.initialize_dynamo_db(Dynamotb,dynamo_client,json_parameter_data,jobid,jobinputfile)
	




