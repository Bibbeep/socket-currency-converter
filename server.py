import socket
import requests
import json

SV_IP = '127.0.0.1'
SV_PORT = 12345

server = socket.socket()
server.bind((SV_IP, SV_PORT))

print(f'Server {SV_IP}:{SV_PORT} is listening...')
server.listen(1)

while True:
    try:
        conn, address = server.accept()
        print(f'\nConnected with {address[0]}:{address[1]}')

        data = json.loads(conn.recv(1024).decode())
        print(f'Data received: {data}')
        if not data:
            raise Exception('Invalid data from the client')

        from_curr, to_curr, amount = data['from'], data['to'], data['amount']

        response = requests.get(f'https://api.frankfurter.app/latest?amount={amount}&from={from_curr}&to={to_curr}')
        if not response:
            raise Exception('Fail to fetch data from API')

        conn.sendall(str(response.json()['rates'][to_curr]).encode())
    except Exception as message:
        print(message)
    finally:
        conn.close()