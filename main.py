from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/time")
async def root():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://worldtimeapi.org/api/timezone/Etc/UTC", params={"timezone": "Europe/London"},)
        return response.json()
    