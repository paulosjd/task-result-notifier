
**Quick Start**

Install dependencies using `pip install -r requirements.txt` and `npm install socketio --save`

Run the notifier service: `node notifier.js`

Run the application server: `python server.py`

Run the task manager: `celery worker -A worker`

*nb* Current configuration requires a RabbitMQ service as a message broker for Celery.

**Overview**

On loading the page, `index.html` a websocket connection should be established
between the client and the notifier service, then an id for the client is emitted
from the notifier service and received by the client. On a browser click event,
this id is sent in the POST request body to the application server, which then 
creates a Celery task, which is passed this id. The server view function returns 
a simple string in a 202 Response stating that the task is being processed.

When the task is completed, the task result is sent along with the client id 
in the body of a POST request to the 'notify' endpoint of the notifier service.
A function is then executed which uses the client id to find the appropriate
connection and broadcasts the result which it received. The client, which listens
for this, receives the data and updates the DOM with it.