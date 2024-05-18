import json
import base64

# Use a raw string for the file path
file_path = r'C:\Users\Lenovo\Documents\my_fastapi_project\jason.json'

with open(file_path, 'r') as json_file:
    data = json.load(json_file)
    encoded_json = base64.b64encode(json.dumps(data).encode('utf-8')).decode('utf-8')
    print(encoded_json)
