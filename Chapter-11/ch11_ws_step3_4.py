# please replace with your preferred model if needed 
MODEL = "mistral-small-2503"

# please replace with your preferred project ID if needed 
PROJECT_ID = "learnmistral"

# please replace with your preferred location 
LOCATION = "us-central1" 


def validate_configuration():
    if not PROJECT_ID:
        raise ValueError("Please set your PROJECT_ID")

    if not MODEL:
        raise ValueError("Please set your MODEL")
    
# uncomment to test    
# validate_configuration()