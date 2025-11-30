import re
import base64

def clean_email(text):
    text = re.sub(r"<[^>]+>", "", text)
    return text.strip()

def extract_email_body(payload):
    body = ""

    if payload.get("body", {}).get("data"):
        try:
            decoded = base64.urlsafe_b64decode(
                payload["body"]["data"]
            ).decode("utf-8", errors="ignore")
            return clean_email(decoded)
        except:
            return ""

    if "parts" in payload:
        for part in payload["parts"]:
            if part.get("body", {}).get("data"):
                try:
                    decoded = base64.urlsafe_b64decode(
                        part["body"]["data"]
                    ).decode("utf-8", errors="ignore")
                    body += decoded + "\n"
                except:
                    pass

            if "parts" in part:
                body += extract_email_body(part)

    return clean_email(body.strip())
