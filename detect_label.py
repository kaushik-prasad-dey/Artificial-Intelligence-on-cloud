#from urllib import response
import boto3
if __name__ == "__main__":
    filename = 'rekog-pic.jpeg'
    bucket = 'spk-sagemaker-rek'
    client = boto3.client('rekognition')
    response = client.detect_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': filename}})
    print('Detected labels for' + filename)
    for label in response['Labels']:
        print(label['Name']+':'+str(label['Confidence']))
