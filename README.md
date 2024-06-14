<h2> Ping Pong Game </h2>

<h3> Overview: </h3> 
<p> Goal is to create a 'Ping Pong' Game between two servers. The First server sends a ping to the second, the second waits pong_time_ms milliseconds before sending s request back to the first at "/ping" endpoint. </p>

<h3> Scripts: </h3>
    <strong> pong_cli.py: </strong> 
                    <ul><p>Manages CLI commands for the game including:<p>
                    <li> start *pong_time_ms*: starts the ping pong game between the two servers with pong_time_ms between requests </li> 
                    <li> pause: pauses the ping pong game </li> 
                    <li> resume: resumes a paused ping pong game </li> 
                    <li> stop: ends the game </li> 
                    </ul>
    <strong> server1.py: </strong>
        FastAPI server running on port 8000. Has endpoints to handle requests on the game: <br>
                 [/ping, <br>
                 /start,<br>
                 /pause,<br>
                 /resume,<br>
                 /stop"]<br>
        Function <strong> send_ping: </strong> <p>While the game is running and not paused, sends a ping request to other server (port 8001) and waits for pong_time_ms </p> <br>
    <strong> server2.py: </strong> <p> Same script as server1.py, aside from the port it is running on and sending requests to. </p>