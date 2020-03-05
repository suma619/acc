from chalicelib.Services import transcode


def controller(event):

	print("invoked controller")
	sourceS3Key=event.key
	sourceS3Bucket = event.bucket
	print(sourceS3Key,sourceS3Bucket)
	transcode.transcode(sourceS3Key,sourceS3Bucket)

