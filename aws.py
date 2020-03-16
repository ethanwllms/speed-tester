import boto, csv
import boto.s3
import sys
from boto.s3.key import Key

def putToS3(filename):
    credentials = gatherCredentials()
    AWS_ACCESS_KEY_ID = credentials["Access key ID"]
    AWS_SECRET_ACCESS_KEY = credentials["Secret access key"]

    bucket_name = 'network-speed-test-temp'
    conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
            AWS_SECRET_ACCESS_KEY)

    bucket = conn.create_bucket(bucket_name,
        location=boto.s3.connection.Location.DEFAULT)

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
    csvLoc = "../../Downloads/credentials.csv"
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
