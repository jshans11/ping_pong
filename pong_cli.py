import sys
import httpx
import asyncio




async def send_command(command, param=None):
    urls = ["http://localhost:8000", "http://localhost:8001"]
    async with httpx.AsyncClient() as client:
        for url in urls: #need to send game status updates to both instances
            if command == "start":
                response = await client.post(f"{url}/start?interval={param}")
            elif command == "pause":
                response = await client.post(f"{url}/pause")
            elif command == "resume":
                response = await client.post(f"{url}/resume")
            elif command == "stop":
                response = await client.post(f"{url}/stop")
            print(f"Response from {url}: {response.json()}")

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python pong-cli.py <command> <param>")
        sys.exit(1)
    
    command = sys.argv[1]
    param = int(sys.argv[2]) if len(sys.argv) > 2 else None

    if command == "start":
        # start_servers()
        asyncio.run(send_command(command, param))
    elif command == "stop":
        asyncio.run(send_command(command))
        # stop_servers()
    elif command in ["pause", "resume"]:
        asyncio.run(send_command(command))
    else:
        print("Unknown command")

    
