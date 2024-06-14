import boto3
from pprint import pprint


def tag_check(queue, tag_key):
    response = sqs.list_queue_tags(
        QueueUrl=queue
    )
    tags = response['Tags']
    return tag_key in tags


def tag_update(queue, tag_key, tag_value):
    print(f'update queue {queue}')
    response = sqs.tag_queue(
        QueueUrl=queue,
        Tags={
            tag_key: tag_value
        }
    )
    print(response)


"""
sqs 리소스에 대해 특정 태그가 있는지 찾고, 없다면 태그를 부여하는 코드
"""

sqs = boto3.client('sqs')
queue_list = sqs.list_queues()['QueueUrls']
databricks_queue = []

tag_key = 'tag_key'                       # Set 'Key' what you need
tag_value = 'tag_value'                   # Set 'Value' what you need


for queue in queue_list:
    if 'databricks' in queue:
        databricks_queue.append(queue)

for queue in databricks_queue:
    if tag_check(queue=queue, tag_key=tag_key):
        pass
    else:
        tag_update(
            queue=queue,
            tag_key=tag_key,
            tag_value=tag_value
        )
