How deploy a static website using Amazon S3:

1. Create an Amazon S3 bucket: First, create an S3 bucket to store static webpage. 
	1.1 Go to the AWS Management Console and navigate to the S3 service. Click the "Create Bucket" button and follow the prompts to create a new bucket. Make sure to name your bucket something unique and remember the region where it was created.
	1.2 Use aws CLI
		aws s3api create-bucket --bucket my-bucket-name --region us-east-1 --create-bucket-configuration LocationConstraint=us-east-1
		aws s3 cp index.html s3://my-bucket-name/index.html
		aws s3 website s3://my-bucket-name/ --index-document index.html --error-document error.html

	1.3 Use aws SDK, i.e. Python Boto3.

2. Upload website content: Upload the website content to your S3 bucket. This can be done using the S3 Management Console, AWS CLI, or AWS SDKs. Ensure that your website content files are named properly and contain any necessary metadata.

3. Configure bucket properties: Configure the bucket properties to enable static website hosting. Navigate to the bucket properties and select the "Static website hosting" option. Then, set the index document and error document as appropriate for your website.

4. Set up DNS routing: Use Route 53 to create a new DNS record that points to your S3 bucket. This allows users to access your website using a custom domain name.

5. Enable CloudFront distribution: Enable CloudFront distribution for your website. CloudFront is a content delivery network (CDN) that caches your website content at edge locations around the world, improving website performance for users. To enable CloudFront, create a new distribution and configure it to use your S3 bucket as the origin.

6. Test your website: Once your website is configured, test it to make sure it is accessible to users. Use your custom domain name to access the website, and verify that all content is loading properly.

Overall, this project will help you understand the basics of hosting a static website on AWS using S3, Route 53, and CloudFront.