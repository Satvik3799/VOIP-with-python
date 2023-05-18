import socket
import threading
import pyaudio

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     
while 1:
    try:
        target_ip = input('Enter IP address of server --> ')
        target_port = int(input('Enter target port of server --> '))
        s.connect((target_ip, target_port))
        break
    except:
        print("Couldn't connect to server")

chunk = 1024
audio_format = pyaudio.paInt16
channels = 1
rate = 20000

p = pyaudio.PyAudio()
play = p.open(format=audio_format, channels=channels, rate=rate, output=True, frames_per_buffer=chunk)
record = p.open(format=audio_format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)
        
print("Connected to Server")

def receive():
    while True:
        try:
            data = s.recv(1024)
            play.write(data)
        except:
            pass

def send():
    while True:
        try:
            data = record.read(1024)
            s.sendall(data)
        except:
            pass

receive_thread = threading.Thread(target=receive).start()
send()

