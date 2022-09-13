#from turtle import position
import boto3
sourceFile = 'prisoner.jpg'
targetFile = 'group-pic.jpeg'
client = boto3.client('rekognition')
imageSource = open(sourceFile, 'rb')
imageTarget = open(targetFile, 'rb')
response = client.compare_faces(SimilarityThreshold=90,
                                SourceImage={'Bytes': imageSource.read()},
                                TargetImage={'Bytes': imageTarget.read()}
                                )
for faceMatch in response['FaceMatches']:
    print("FaceMatch:")
    print(150*"="+'\n')
    print(faceMatch)
    print(150*"="+'\n')
    position = faceMatch['Face']['BoundingBox']
    similarity = str(faceMatch['Similarity'])
    print('The face at'+'\n' +
          'left:'+str(position['Left'])+''+'\n' +
          'Top:'+str(position['Top'])+''+'\n' +
          'Width:'+str(position['Width'])+''+'\n' +
          'Height:'+str(position['Height'])+''+'\n' + '\n' +
          'matches with' + similarity + '% confidence'
          )
imageSource.close()
imageTarget.close()
