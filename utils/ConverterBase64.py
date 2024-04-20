import base64

class ConverterBase64:

    def convert_into_base64(self, creds):
        return base64.b64encode(str.encode(creds)).decode('utf-8')