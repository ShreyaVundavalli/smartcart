from fastapi import FastAPI, Request
import firebase_admin
from firebase_admin import credentials, firestore
import os
import base64
import json

app = FastAPI()

encoded_creds = os.getenv('FIREBASE_CREDENTIALS_BASE64')
if not encoded_creds:
    raise Exception("Firebase credentials environment variable is not set.")

# Decode from base64 and load the credentials directly
decoded_creds = base64.b64decode(encoded_creds)
firebase_creds_dict = json.loads(decoded_creds.decode('utf-8'))
cred = credentials.Certificate(firebase_creds_dict)
firebase_admin.initialize_app(cred)

db = firestore.client()

@app.post("/upload-sensor-data")
async def upload_sensor_data(request: Request):
    data = await request.json()
    doc_ref = db.collection('sensor_data').add(data)
    return {"status": "success", "data": data, "doc_id": doc_ref[1].id}
