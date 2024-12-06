import os

def split_file(file_path, chunk_size):
    """Splits a large file into smaller fragments."""
    
    if not os.path.exists(file_path):
        print(f"Error: The file {file_path} does not exist.")
        return
    
    try:
        with open(file_path, 'rb') as f:
            chunk_number = 1
            while chunk := f.read(chunk_size):
                fragment_file = f"file_fragment_{chunk_number}.dat"
                
                with open(fragment_file, 'wb') as chunk_file:
                    chunk_file.write(chunk)
                print(f"Created {fragment_file}")
                
                chunk_number += 1
        print(f"File {file_path} has been split into {chunk_number - 1} fragments.")
    except Exception as e:
        print(f"Error during file split: {e}")

if __name__ == "__main__":
    file_path = "large_file.dat"  # Replace with your actual file path
    chunk_size = 1 * 1024 * 1024  # 1MB chunks

    split_file(file_path, chunk_size)
