import json
def create_media_convert_job(med_client,Dynamotb,mediaConvertRole,region,queue,Temp1,json_parameter_data):
    statusCode = 200
    body = {}
    Job = med_client.create_job(
            JobTemplate=Temp1,
            Role= mediaConvertRole,
            Queue = queue,
            UserMetadata=json_parameter_data['jobMetadata'],
            Settings={
                
             'Inputs':
             [
                 {
                'AudioSelectors': {
                    'Audio Selector 1': {
                        'Offset': 0,
                        'DefaultSelection': 'DEFAULT',
                        'ProgramSelection': 1
                    }
                },
                'VideoSelector': {
                    'ColorSpace': 'FOLLOW',
                    'Rotate': 'DEGREE_0'
                },
                 'FileInput': json_parameter_data['sourceS3']
                },
             ],
             'OutputGroups':
             [  
                 {
                    "OutputGroupSettings": {
                    "Type": "HLS_GROUP_SETTINGS",
                    "HlsGroupSettings": {
                    "Destination": json_parameter_data['dest1'],
                } } 
                },
                {
                    "OutputGroupSettings": {
                    "Type": "FILE_GROUP_SETTINGS",
                    "FileGroupSettings": {
                    "Destination": json_parameter_data['dest3'],
                 } }
                },
                {
                    "OutputGroupSettings": {
                    "Type": "FILE_GROUP_SETTINGS",
                    "FileGroupSettings": {
                    "Destination": json_parameter_data['dest2'],
                 } }
                }
             ]
            } 
        )
    print (json.dumps(Job, default=str))
    jsonin = json.dumps(Job, default=str)
    jsoncollection=json.loads(jsonin)
    jobid = jsoncollection['Job']['Id']
    jobinputfile = jsoncollection['Job']['Settings']['Inputs'][0]['FileInput']
    print('####################   Start JOB Collection ######################## ')
    print(json_parameter_data['S3KeyHLS'])
    print(jsoncollection)
    print('####################   End Job Collection ################')
    return jobid,jobinputfile