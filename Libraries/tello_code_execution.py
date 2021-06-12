import socket
import json
import time

local_port = None
tello_drone_ip = None
tello_drone_port = None
timeout = None
s = None

try:
    config = json.load(open("config/tello_code_execonfig.json"))
    local_port = int(config["local_port"])
    tello_drone_ip = str(config["tello_drone_ip"])
    tello_drone_port = int(config["tello_drone_port"])
    timeout = int(config["timeout"])
except FileNotFoundError:
    print("no tello-code-execution config file found")


def connect():
    global s
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, b'wlan0')
    s.bind(("", local_port))
    print(send_command("command"))


def send_command(command:str) -> str:
    if local_port != None:
        if tello_drone_ip != None:
            if tello_drone_port != None:
                if timeout != None:
                    if s != None:
                        s.connect((tello_drone_ip, tello_drone_port))
                        s.settimeout(timeout)
                        s.send(command.encode('ASCII'))
                        r = s.recv(1024)
                        return r.decode(errors='replace').strip()
                        
    print("invalid configuration")
    return "error (from tello code execution code)"


def disconnect():    
    if s == None:
        return
    
    s.shutdown(socket.SHUT_RDWR)
    s.close()


connect()
print(send_command("takeoff"))
print(send_command("land"))
disconnect()
