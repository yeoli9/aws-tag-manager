import boto3
from pprint import pprint


def tag_check(topic_arn, tag_key):
    response = sns.list_tags_for_resource(
        ResourceArn=topic_arn
    )
    tags = response['Tags']
    return any(tag['Key'] == tag_key for tag in tags)


def tag_update(topic_arn, tag_key, tag_value):
    print(f'update topic {topic_arn}')
    response = sns.tag_resource(
        ResourceArn=topic_arn,
        Tags=[
            {
                'Key': tag_key,
                'Value': tag_value
            }
        ]
    )
    return response


"""
sns 리소스에 대해 특정 태그가 있는지 찾고, 없다면 태그를 부여하는 코드
"""

sns = boto3.client('sns')
topic_list = sns.list_topics()['Topics']
databricks_topic_arns = []

tag_key = 'tag_key'                       # Set 'Key' what you need
tag_value = 'tag_value'                   # Set 'Value' what you need


for topic in topic_list:
    if 'databricks' in topic['TopicArn']:
        databricks_topic_arns.append(topic['TopicArn'])

for topic_arn in databricks_topic_arns:
    if tag_check(topic_arn=topic_arn, tag_key=tag_key):
        pass
    else:
        tag_update(
            topic_arn=topic_arn,
            tag_key=tag_key,
            tag_value=tag_value
        )
