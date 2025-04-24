import pandas as pd
import urllib.request
import hashlib

# Function to compute hash of a file's content
def compute_file_hash(filename):
    hasher = hashlib.md5()  # You can use other algorithms like sha256
    with open(filename, 'rb') as f:  # Read file in binary mode
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

# Load URLs from Excel
df = pd.read_excel('input.xlsx')

# Dictionary to store hash values and corresponding filenames
hash_dict = {}

for idx, url in enumerate(df['URL'], 1):
    filename = f"{idx}.txt"
    urllib.request.urlretrieve(url, filename)  # Download the file

    # Compute hash for the downloaded content
    file_hash = compute_file_hash(filename)

    # Check if this hash already exists
    if file_hash in hash_dict:
        print(f"Duplicate content found: {filename} is identical to {hash_dict[file_hash]}")
    else:
        hash_dict[file_hash] = filename  # Store the hash and filename

