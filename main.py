from fastapi import FastAPI, HTTPException, Request
from firebase_admin import credentials, initialize_app, firestore
import uvicorn

app = FastAPI()

# Initialize Firebase Admin
cred = credentials.Certificate('firebasekeyy.json')  # Updated path
initialize_app(cred)
db = firestore.client()

@app.post("/upload-sensor-data")
async def upload_sensor_data(request: Request):
    data = await request.json()
    # Add data to Firestore
    db.collection('sensor_data').add(data)
    return {"status": "success", "data": data}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
