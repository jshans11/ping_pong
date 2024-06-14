# server 2 on port 8001
from fastapi import FastAPI
import httpx
import asyncio

app = FastAPI()
pong_time_ms = 1000
game_paused = False
game_running = False

@app.post("/ping", status_code=200)
async def ping():
    print("server2 got pinged")
    return {"message": "pong"}

@app.post("/start")
async def start_game(interval: int):
    global pong_time_ms, game_running, game_paused
    pong_time_ms = interval
    game_running = True
    game_paused = False
    asyncio.create_task(send_ping())
    return {"message": "game started"}

@app.post("/pause")
async def pause_game():
    global game_paused
    game_paused = True
    return {"message": "game paused"}

@app.post("/resume")
async def resume_game():
    global game_paused
    game_paused = False
    asyncio.create_task(send_ping())
    return {"message": "game resumed"}

@app.post("/stop")
async def stop_game():
    global game_running
    game_running = False
    return {"message": "game stopped"}

async def send_ping():
    global pong_time_ms, game_running, game_paused
    while game_running:
        if not game_paused:
            async with httpx.AsyncClient() as client:
                try:
                    response = await client.post("http://localhost:8000/ping") 
                    print(response.json())
                except Exception as e:
                    print(e)
        await asyncio.sleep(pong_time_ms / 1000) 

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
