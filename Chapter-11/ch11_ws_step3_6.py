from mistralai_gcp import MistralGoogleCloud
from ch11_ws_step3_3 import get_gcloud_access_token
from ch11_ws_step3_4 import MODEL, PROJECT_ID, LOCATION

access_token = get_gcloud_access_token()

# uncomment to troubleshoot
# print(f"access_token: {access_token}")
# print(f"MODEL: {MODEL}")
# print(f"PROJECT_ID: {PROJECT_ID}")
# print(f"LOCATION: {LOCATION}")

client = MistralGoogleCloud(
    access_token=access_token, region=LOCATION, project_id=PROJECT_ID
)

try:
    stream = client.chat.stream(
        model=f"{MODEL}",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": "Who is the best French painter? Answer in one short sentence.",
            }
        ],
    )

    for chunk in stream:
        print(chunk.data.choices[0].delta.content)

except Exception as e:
    print(f"An error occurred: {e}")
    print(f"[debug] access_token: {access_token}")
    print(f"[debug] MODEL: {MODEL}")
    print(f"[debug] PROJECT_ID: {PROJECT_ID}")
    print(f"[debug] LOCATION: {LOCATION}")