import boto3
import json

client = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')

model_id = 'mistral.mistral-small-2402-v1:0'

# Payload for Bedrock
payload = {
    "prompt": "Explain the concept of reinforcement learning in simple terms.",
    "temperature": 0.7,
    "max_tokens": 300
}

try:
    # Call the Bedrock model
    response = client.invoke_model(
        modelId=model_id,
        body=json.dumps(payload),
        contentType="application/json",
        accept="application/json"
    )
    # Read the response body (convert StreamingBody to string)
    response_body = response["body"].read().decode("utf-8")
    result = json.loads(response_body)

    # Extract the model's output
    output_text = result.get("outputs", [{}])[0].get("text", "No response received.")
    print(">>>", payload["prompt"])
    print("<<<", output_text)
    # print("Raw Response:", result)
except Exception as e:
    # Print detailed debug information
    print("Error occurred while invoking the model:")
    print(f"Exception Type: {type(e).__name__}")
    print(f"Error Message: {e}")
    if hasattr(e, 'response'):
        print("AWS Error Response:")
        print(json.dumps(e.response, indent=2))


