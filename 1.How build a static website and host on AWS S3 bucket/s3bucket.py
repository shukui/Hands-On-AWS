import boto3

# Set up S3 client
s3_client = boto3.client('s3')

# Set up S3 resource
s3_resource = boto3.resource('s3')

# Set bucket name and region
bucket_name = 'my-bucket-static-webpage'
bucket_region = 'us-east-2'

# Set index and error documents
index_document = '.\\index.html'
error_document = '.\\error.html'

# Set S3 bucket website configuration
website_configuration = {
    'ErrorDocument': {'Key': error_document},
    'IndexDocument': {'Suffix': index_document}
}

# Create S3 bucket
try:
    s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': bucket_region})
    print(f"S3 bucket {bucket_name} created successfully in region {bucket_region}.")
except Exception as e:
    print(f"Error creating S3 bucket: {e}")


# Upload index.html file to S3 bucket
try:
    s3_resource.Object(bucket_name, 'index.html').upload_file('.\\index.html')
    print(f"index.html file uploaded successfully to S3 bucket {bucket_name}.")
except Exception as e:
    print(f"Error uploading index.html file: {e}")

try:
    # Configure S3 bucket for static website hosting
    s3_client.put_bucket_website(
        Bucket = bucket_name,
        WebsiteConfiguration = website_configuration
    )
    print(f"S3 bucket {bucket_name} configured for static website hosting with index document {index_document} and error document {error_document}.")
except Exception as e:
    print(f"Error configuring S3 bucket for static website hosting: {e}")



# Get S3 bucket website configuration
try:
    website_configuration = s3_client.get_bucket_website(
        Bucket=bucket_name
    )
    endpoint_url = website_configuration['Endpoint']
    print(f"S3 bucket endpoint URL: {endpoint_url}")
except Exception as e:
    print(f"Error getting S3 bucket website configuration: {e}")
