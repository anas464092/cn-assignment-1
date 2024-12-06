import socket
import os
import time
import random

def serve_file(fragment_file, client_socket):
    """Send the requested file fragment to the client."""
    try:
        with open(fragment_file, 'rb') as file:
            while True:
                chunk = file.read(1024)  # Read in 1KB chunks
                if not chunk:
                    break
                client_socket.send(chunk)
    except Exception as e:
        print(f"Error while serving file: {e}")
        client_socket.close()

def start_server(host, port, fragment_file):
    """Start the server to listen for incoming requests."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server started at {host}:{port}, serving {fragment_file}")

    while True:
        try:
            client_socket, client_address = server_socket.accept()
            print(f"Connection established with {client_address}")
            serve_file(fragment_file, client_socket)
            client_socket.close()
            print(f"Connection closed with {client_address}")
            
            # Simulating random server failure (for testing purposes)
            if random.random() < 0.05:  # 5% chance of server failure
                print("Simulating server failure...")
                raise Exception("Server failure simulated.")

        except Exception as e:
            print(f"Error during connection: {e}")

if __name__ == "__main__":
    host = '0.0.0.0'  # Listen on all network interfaces
    port = 12347       # Port for the server
    fragment_file = 'file_fragment_3.dat'  # Example fragment

    start_server(host, port, fragment_file)
