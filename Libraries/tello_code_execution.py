import socket
import json

local_port = None
tello_drone_ip = None
tello_drone_port = None
connection_timeout_in_seconds = None

try:
    config = json.load(open('config/tello_code_execonfig.json"))
    local_port = int(config["local_port"])
    tello_drone_ip = str(config["tello_drone_ip"])
    tello_drone_port = int(config["tello_drone_port"])
    connection_timeout_in_seconds = float(config["connection_timeout_in_seconds"])
except FileNotFoundError:
    print("No tello-code-execution config file found.")


def send_command(command:str) -> str:
    if local_port and tello_drone_ip and tello_drone_port and connection_timeout_in_seconds:
        conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        conn.bind(('', local_port))
        conn.connect((tello_drone_ip, tello_drone_port))
        conn.settimeout(connection_timeout_in_seconds)
        conn.send(command.encode('ASCII'))
        resp = conn.recv(1024)
        return resp.decode(errors='replace').strip()

    print("Invalid configuration.")
    return "Error"
