import socket
import numpy as np

HOST = "127.0.0.1"
PORT = 25001

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections (maximum 1 connection in the queue)
server_socket.listen(1)

print(f"Server listening on {HOST}:{PORT}")

while True:
    # Wait for a connection
    print("Waiting for a connection...")
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    # Receive and print the data from the client
    data = client_socket.recv(1024)
    if not data:
        break  # If no data is received, break the loop

    # print(f"Received data: {data.decode('utf-8')}")
    
    data = data.decode('utf-8')
    arr = data.split('|')
    np_arr = np.array([0,0])
    for i in range(0, int(len(arr)/2)):
        np_arr = np.append(np_arr, np.array([[float(arr[2*i]), float(arr[2*i + 1])]]))
    print(np_arr)
    
    # Send a response back to the client
    response = "Hello from the server!"
    client_socket.sendall(response.encode('utf-8'))

    # Close the connection with the client
    client_socket.close()

# Close the server socket
server_socket.close()

