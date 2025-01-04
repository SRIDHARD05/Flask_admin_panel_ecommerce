from src import get_config
import boto3
from botocore.exceptions import NoCredentialsError


class AmazonS3:
    @staticmethod
    def get_connection(bucket):
        try:
            s3 = boto3.client('s3',aws_access_kry_id= get_config("s3_aws_access_key"),aws_secret_access_key=get_config("s3_aws_secret_access_key"))
            return s3
        except NoCredentialsError as e:
            return {
                'status' : 'No limits of credits'
            }