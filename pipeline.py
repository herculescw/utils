import boto3
import urllib2

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# Upload a new file
#data = open('test.txt', 'rb')
#s3.Bucket('handsgridataoregon').put_object(Key='test.txt', Body=data)

with open('handsdataurl.txt') as f:
    urllist = f.readlines()
    for url in urllist:
        print url
        tiffile = urllib2.urlopen(url)
        with open(url.rsplit('/', 1)[-1],'wb') as output:
            output.write(tiffile.read())


