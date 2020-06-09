import boto3

cloudwatch = boto3.client('cloudwatch')

def lambda_handler(event, handler):
  bucket = event['Records'][0]['s3']['bucket']['name']
  key = event['Records'][0]['s3']['object']['key']
        
  copy_source = {
      'Bucket': bucket,
      'Key': key
  }
  copy_target = s3.Bucket('aws-training-qinyun-copy')
  copy_target.copy(copy_source, key)
    
