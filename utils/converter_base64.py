import base64


def convert_into_base64(creds: str) -> str:
    return base64.b64encode(str.encode(creds)).decode('utf-8')
