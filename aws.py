import boto3, csv, logging, sys, os
from boto.s3.key import Key
from botocore.exceptions import ClientError

def putToS3(filename):
 credentials = gatherCredentials()
# print("Credentials gathered")
 AWS_ACCESS_KEY_ID = credentials["Access key ID"]
# print(credentials["Access key ID"]) 
 AWS_SECRET_ACCESS_KEY = credentials["Secret access key"]
# print(credentials["Secret access key"])

 os.environ['AWS_PROFILE'] = "default"
 os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'

 bucket_name = 'network-speed-test-temp'
 s3 = boto3.client('s3')
 with open(filename, "rb") as f:
  s3.upload_fileobj(f, bucket_name, filename, ExtraArgs={'ACL': 'public-read'})
 
# print('Uploading ' + filename + ' to Amazon S3 bucket: ' + bucket_name)

def percent_cb(complete, total):
 sys.stdout.write('.')
 sys.stdout.flush()

 k = Key(bucket)
 k.key = filename
 k.set_contents_from_filename(filename,
  cb=percent_cb, num_cb=10)
 print('Upload completed..')

def gatherCredentials():
 csvLoc = "/home/pi/Downloads/credentials.csv"
 credentials = {}
 input_file = csv.DictReader(open(csvLoc))
 for row in input_file:
  credentials.update(row)
 # print(credentials)
 try:
  del credentials["User name"]
 except:
  print("Could not delete 'User name'; Key not found.")
 try:
  del credentials["Password"]
 except:
  print("Could not delete 'Password'; Key not found.")
 try:
  del credentials["Console login link"]
 except:
  print("Could not delete 'Console login link'; Key not found.")
 # print(credentials)
 return credentials
