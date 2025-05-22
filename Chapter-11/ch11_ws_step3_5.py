from mistralai_gcp import MistralGoogleCloud
from ch11_ws_step3_3 import get_gcloud_access_token
from ch11_ws_step3_4 import MODEL, PROJECT_ID, LOCATION

access_token = get_gcloud_access_token()

client = MistralGoogleCloud(
    access_token=access_token, 
    region=LOCATION, 
    project_id=PROJECT_ID
)

try:
    resp = client.chat.complete(
        model=f"{MODEL}",
        messages=[
            {
                "role": "user",
                "content": "Who is the best French painter?in one short sentence",
            }
        ],
    )
    print(resp.choices[0].message.content)

except Exception as e:
    print(f"An error occurred: {e}")
    print(f"[debug] access_token: {access_token}")
    print(f"[debug] MODEL: {MODEL}")
    print(f"[debug] PROJECT_ID: {PROJECT_ID}")
    print(f"[debug] LOCATION: {LOCATION}")

