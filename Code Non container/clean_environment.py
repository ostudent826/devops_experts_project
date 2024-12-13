
import requests

def stop_server():
    servers = [
        'http://127.0.0.1:5000/stop_server',
        'http://127.0.0.1:5001/stop_server'
    ]

    for server in servers:
        try:
            response = requests.get(server)
            if response.status_code == 200:
                print(f"Server at {server} stopped successfully.")
            else:
                print(f"Failed to stop server at {server}, Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error stopping server at {server}: {e}")



if __name__ == '__main__':
    stop_server()