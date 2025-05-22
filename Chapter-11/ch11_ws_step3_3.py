import subprocess

def get_gcloud_access_token():
    process = subprocess.Popen(
        "gcloud auth print-access-token",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True
    )
    access_token_bytes, err = process.communicate()

    if process.returncode != 0:
        raise RuntimeError(f"Failed to get access token: {err.decode('utf-8').strip()}")

    return access_token_bytes.decode("utf-8").strip()


# uncomment to test and see the acccess token
# print(get_gcloud_access_token())