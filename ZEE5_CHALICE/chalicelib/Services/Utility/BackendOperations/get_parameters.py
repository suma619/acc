import os
import json
import glob
import json
import os
import uuid
import boto3
import datetime
import random
import urllib.parse
import functools
import datetime
import hashlib

from botocore.client import ClientError
from os.path import dirname


def get_parameters(sourceS3Key,sourceS3Bucket):
	assetID = str(uuid.uuid4())
	jobMetadata = {'assetID': assetID}

	sourceS3 = 's3://'+ sourceS3Bucket + '/' + sourceS3Key
	print(sourceS3)
	sourceS3Basename = os.path.splitext(os.path.basename(sourceS3))[0]
	print(sourceS3Basename)
	sourceS3dirpath=os.path.dirname(sourceS3Key)
	sourceS3dirpath2=os.path.dirname(sourceS3Key[9:])
	destinationS3 = 's3://' + os.environ['DestinationBucket']
	destinationS3basename = os.path.splitext(os.path.basename(destinationS3))[0]

	S3KeyHLS_path = '/News/' + 'Vod' + sourceS3dirpath2 + '/' + sourceS3Basename + '/' + 'index'
	S3KeyTCR_path = '/News/' + 'tcr' + sourceS3dirpath2 + '/' + sourceS3Basename  + '_' 
	S3thumb = '/News/' + 'thumbnails' + sourceS3dirpath2 + '/' + sourceS3Basename  + '/'
	S3KeyHLS = '/News/' + 'Vod' +  sourceS3dirpath2 + '/' + sourceS3Basename + '/' + 'index.m3u8'
	S3KeyTCR = '/News/' + 'tcr' +  sourceS3dirpath2 + '/' + sourceS3Basename + '_tcr/tcr.mp4'

	dest1 = destinationS3  + S3KeyHLS_path
	dest2 = destinationS3  + S3KeyTCR_path
	dest3 = destinationS3  + S3thumb

	parameter = {}
	parameter['sourceS3'] = sourceS3
	parameter['sourceS3Basename'] = sourceS3Basename
	parameter['sourceS3dirpath'] = sourceS3dirpath
	parameter['sourceS3dirpath2'] = sourceS3dirpath2
	parameter['destinationS3'] = destinationS3
	parameter['destinationS3basename'] = destinationS3basename
	parameter['dest1']=dest1
	parameter['dest2']=dest2
	parameter['dest3']=dest3
	parameter['jobMetadata']=jobMetadata
	parameter['S3KeyHLS']=S3KeyHLS
	parameter['S3KeyTCR']=S3KeyTCR
	parameter['assetID']=assetID




	json_parameter = json.dumps(parameter)
	return json_parameter
