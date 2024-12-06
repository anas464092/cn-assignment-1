import socket
import threading
import os
import time

# Define the fragment files and server details
fragment_files = ['file_fragment_1.dat', 'file_fragment_2.dat']
server_ips = ['127.0.0.1', '127.0.0.1', '127.0.0.1']  # IPs of the servers
server_ports = [12345, 12346, 12347]  # Ports of the servers
output_file = 'recombined_large_file.dat'

# Function to download a fragment from a server with retries
def download_fragment(server_ip, server_port, fragment_file):
    """Download a single file fragment from the server."""
    retries = 3  # Number of retries in case of failure
    attempt = 0

    while attempt < retries:
        try:
            # Create a socket and connect to the server
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect((server_ip, server_port))
                print(f"Connected to {server_ip}:{server_port} to download {fragment_file}")

                # Open the file to save the downloaded fragment
                with open(fragment_file, 'wb') as f:
                    while True:
                        # Receive chunks of the file
                        chunk = client_socket.recv(1024)
                        if not chunk:
                            break
                        f.write(chunk)
                print(f"Downloaded {fragment_file}")
                return True
        except Exception as e:
            print(f"Error while downloading {fragment_file}: {e}")
            attempt += 1
            print(f"Retrying... Attempt {attempt}/{retries}")
            time.sleep(2)  # Wait before retrying

    print(f"Failed to download {fragment_file} after {retries} attempts.")
    return False

# Function to recombine the downloaded fragments into the original file
def recombine_fragments(fragment_files, output_file):
    """Recombine the downloaded file fragments into the original file."""
    with open(output_file, 'wb') as output_file_handle:
        for fragment_file in fragment_files:
            with open(fragment_file, 'rb') as fragment:
                output_file_handle.write(fragment.read())
            print(f"Recombined {fragment_file}")
    print(f"Recombined all fragments into {output_file}")

# Main function to download fragments concurrently and recombine them
def main():
    # First, check if the file already exists (for download resuming)
    already_downloaded = {fragment_file: os.path.exists(fragment_file) for fragment_file in fragment_files}

    threads = []
    for i, fragment_file in enumerate(fragment_files):
        if not already_downloaded[fragment_file]:
            # Only download the fragment if it hasn't been downloaded yet
            thread = threading.Thread(target=download_fragment, args=(server_ips[i], server_ports[i], fragment_file))
            threads.append(thread)
            thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # After downloading all fragments, recombine them into the original file
    recombine_fragments(fragment_files, output_file)

if __name__ == "__main__":
    main()
