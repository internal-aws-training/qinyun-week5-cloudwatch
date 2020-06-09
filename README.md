## What is CloudWatch
Amazon CloudWatch monitors your Amazon Web Services (AWS) resources and the applications you run on AWS in real time. You can use CloudWatch to collect and track metrics, which are variables you can measure for your resources and applications.

## What is metrics

Metrics are the fundamental concept in CloudWatch. A metric represents a time-ordered set of data points that are published to CloudWatch. Think of a metric as a variable to monitor, and the data points as representing the values of that variable over time.

## 有哪些指标

![Imgur](https://imgur.com/43OryHg.png)

## 我们可以如何使用metrics

- 获取特定资源统计数据
- 跨资源聚合统计数据
- 绘制指标的图表
- 使用动态标签
- 从图表上的指标创建警报
- 发布自定义指标
- 使用指标数学

## What is event
Amazon CloudWatch Events delivers a near real-time stream of system events that describe changes in Amazon Web Services (AWS) resources.

应用场景:
- Amazon EC2 instances

- AWS Lambda functions

- Streams in Amazon Kinesis Data Streams

- Delivery streams in Amazon Kinesis Data Firehose

- Log groups in Amazon CloudWatch Logs

- Amazon ECS tasks

- Systems Manager Run Command

- systems Manager Automation

- AWS Batch jobs

- Step Functions state machines

- Pipelines in CodePipeline

- CodeBuild projects

- Amazon Inspector assessment templates

- Amazon SNS topics

- Amazon SQS queues

- Built-in targets: EC2 CreateSnapshot API call, EC2 RebootInstances API call, EC2 StopInstances API call, and EC2 TerminateInstances API call.

- The default event bus of another AWS account

### Namespaces
A namespace is a container for CloudWatch metrics. Metrics in different namespaces are isolated from each other, so that metrics from different applications are not mistakenly aggregated into the same statistics.

### Dimensions
A dimension is a name/value pair that is part of the identity of a metric. You can assign up to 10 dimensions to a metric.

### Statistics
Statistics are metric data aggregations over specified periods of time. CloudWatch provides statistics based on the metric data points provided by your custom data or provided by other AWS services to CloudWatch. Aggregations are made using the namespace, metric name, dimensions, and the data point unit of measure, within the time period you specify. The following table describes the available statistics.

### Periods
A period is the length of time associated with a specific Amazon CloudWatch statistic. Each statistic represents an aggregation of the metrics data collected for a specified period of time. Periods are defined in numbers of seconds, and valid values for period are 1, 5, 10, 30, or any multiple of 60.