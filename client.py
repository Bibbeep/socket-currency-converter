import socket
import json

print('=== This client will take inputs from user and connect to a server which call an API to convert a currency to another ===\n')

SV_HOST = '127.0.0.1'
SV_PORT = 12345
server = socket.socket()

from_curr = str(input('\nCurrency to convert from: ')).upper()
to_curr = str(input('Currency to convert to: ')).upper()
amount = float(input('The amount of money: '))
data = {
    'from': from_curr,
    'to': to_curr,
    'amount': amount
}
json_data = json.dumps(data)

server.connect((SV_HOST, SV_PORT))
print(f'\nConnected to the server {SV_HOST}:{SV_PORT}\n')


server.sendall(json_data.encode())
recv_data = server.recv(1024).decode()

print(f'{from_curr} {amount} = {to_curr} {recv_data}')
server.close()
print('\nConnection closed')