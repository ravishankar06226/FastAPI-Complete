import asyncio
from fastapi import FastAPI
import time

app = FastAPI()


@app.get("/")
async def home():
    start = time.time()
    print(f"START {start:.2f}")
    await asyncio.sleep(10) # Non-blocking sleep
    end = time.time()
    print(f"END   {end:.2f}")
    return {"message": "Finished waiting!"}
@app.get("/test")
async def test():
    await asyncio.sleep(10)
    return {"message":"Finished Test"}
