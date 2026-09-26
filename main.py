from urllib import response

from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/time")

def get_time():
    response = httpx.get("https://timeapi.io/api/v1/time/current/zone/?timeZone=UTC")
    if response.status_code == 200:
        data = response.json()
        print(data)
        return {"date_time": data["date_time"]}

    else:
        return {"error": "Unable to fetch time"}

    
