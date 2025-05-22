
import boto3

bedrock = boto3.client(service_name='bedrock', region_name='us-east-1')

response = bedrock.list_foundation_models()
models = response['modelSummaries']
for model in models:
    print(model['providerName'] + " - " + model['modelName'] + " - " + model['modelId'])


    