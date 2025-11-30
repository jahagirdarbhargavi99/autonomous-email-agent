from googleapiclient.discovery import build

def gmail_service(creds):
    return build("gmail", "v1", credentials=creds)
