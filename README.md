Ping Pong Game

Overview: Goal is to create a 'Ping Pong' Game between two servers. The First server sends a ping to the second, the second waits pong_time_ms milliseconds before sending s request back to the first at "/ping" endpoint. 

Scripts:
    pong_cli.py: Manages CLI commands for the game including:
                    start <pong_time_ms>: starts the ping pong game between the two servers with pong_time_ms between requests
                    pause: pauses the ping pong game
                    resume: resumes a paused ping pong game
                    stop: ends the game
    server1.py: 
        FastAPI server running on port 8000. Has endpoints to handle requests on the game:
                 [/ping, 
                 /start,
                 /pause,
                 /resume,
                 /stop"]
        Fucnction send_ping: While the game is running and not paused, sends a ping request to other server (port 8001) and waits for pong_time_ms
    
    server2.py: Same script as server1.py, aside from the port it is running on and sending requests to.