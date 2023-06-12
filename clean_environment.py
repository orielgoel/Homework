import requests
# Stops the backend server
requests.get('http://127.0.0.1:5000/stop_server')

# Stops the frontend server
# requests.get('http://127.0.0.1:5001/stop_server')