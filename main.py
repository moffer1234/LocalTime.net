from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/time")
def get_time():
    response = httpx.get("http://worldtimeapi.org/api/timezone/Etc/UTC")
    if response.status_code == 200:
        data = response.json()
        return {"utc_datetime": data["utc_datetime"]}
    else:
        return {"error": "Unable to fetch time"}


    