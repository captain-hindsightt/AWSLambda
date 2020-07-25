s
import boto3

AMI = os.environ['ami-08a74056dfd30c986']
INSTANCE_TYPE = os.environ['t2-micro']
KEY_NAME = os.environ['Work']
SUBNET_ID = os.environ['subnet-0360f2c5780c9ea0b']

ec2 = boto3.resource('ec2')


def lambda_handler(event, context):

    instance = ec2.run_instances(
        ImageId=AMI,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        SubnetId=SUBNET_ID,
        MaxCount=1,
        MinCount=1
    )

    print("New instance created:", instance[0].id)
