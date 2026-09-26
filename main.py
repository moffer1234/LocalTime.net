from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/time")
async def get_time():
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://timeapi.io/api/v1/time/current/zone/?timeZone=UTC"
        )

    if response.status_code == 200:
        data = response.json()
        return {"date_time": data["date_time"]}

    return {"error": "Unable to fetch time"}