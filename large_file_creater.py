def create_large_file(file_path, size_in_mb):
    """Create a large file with repeating English text of the given size in MB."""
    
    text = """This is an example of a large file with English text.
    The quick brown fox jumps over the lazy dog.
    This sentence contains every letter of the alphabet.
    We are creating a large file for testing purposes, which will be split into smaller fragments.
    The file size will be large enough to test the splitting and downloading process. 
    
    Keep repeating this text to fill the file with content until we reach the required size.
    """
    
    # Join the text into a single string and calculate the size in bytes
    text = text * 500  # Repeat the text block to make the file larger
    
    with open(file_path, 'w') as f:
        size_in_bytes = size_in_mb * 1024 * 1024
        while f.tell() < size_in_bytes:  # Write until the desired size is reached
            f.write(text)
    
    print(f"Created a file at {file_path} with size {size_in_mb}MB.")

if __name__ == "__main__":
    file_path = "large_file.dat"  # Specify the file name (can be any name)
    size_in_mb = 2  # Specify the size of the file in MB (5MB in this case)
    
    create_large_file(file_path, size_in_mb)
