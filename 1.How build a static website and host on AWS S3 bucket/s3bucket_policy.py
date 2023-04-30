import boto3
import json

# Replace 'my-bucket-name' with the name of your S3 bucket
bucket_name = 'my-bucket-static-webpage'

# Define the bucket policy to allow public read access
bucket_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                f"arn:aws:s3:::{bucket_name}/*"
            ]
        }
    ]
}

# Convert the policy to a JSON string
bucket_policy_json = json.dumps(bucket_policy)

# Apply the bucket policy to the bucket
s3 = boto3.client('s3')
s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy_json)
