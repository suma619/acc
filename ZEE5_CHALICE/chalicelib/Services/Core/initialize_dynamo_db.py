def initialize_dynamo_db(Dynamotb,dynamo_client,json_parameter_data,jobid,jobinputfile):
	jobstatus = 'NotCompleted'
	mpdstatus = 'False'
	syncstatus = 'False'
	HLSsync = 'False'
	FinTime = '00:00:00'
	dynamo_client.put_item(TableName=Dynamotb, 
    	Item={'InputFileName':{'S':jobinputfile},
    	'JobId':{'S':jobid},'HlsUrl':{'S':json_parameter_data['S3KeyHLS']},
    	'ResourceID':{'S':json_parameter_data['assetID']},
    	'TCRURL':{'S':json_parameter_data['S3KeyTCR']},
    	'ThumbnailPath':{'S':json_parameter_data['dest3']},
    	'JobStatus':{'S':jobstatus},
    	'SyncStatus':{'S':syncstatus},
    	'HLSsync':{'S':HLSsync},
    	'Finish time':{'S':FinTime}
    	}
    	)
        