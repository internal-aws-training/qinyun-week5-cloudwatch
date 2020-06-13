import boto3

cloudwatch = boto3.client('cloudwatch')

def lambda_handler(event, handler):
  print("Start to put !")
  cloudwatch.put_metric_data(
    MetricData=[
        {
            'MetricName': 'InvocationTimes',
            'Dimensions': [
                {
                    'Name': 'Invocation',
                    'Value': 'Times'
                },
            ],
            'StatisticValues': {
                'Maximum': 1,
                'Minimum': 1,
                'SampleCount': 1,
                'Sum': 1
            },
            'Unit': 'None',
            'Value': 1
        },
    ],
    Namespace='QinyunNameSpace'
  )
  print("End to put !")
