import json

# Read the large file
input_file = 'beta/output_with_stats_simulated.json'
chunk_size = 1 * 1024 * 1024 * 1024  # 1 GB

with open(input_file, 'r') as f:
    data = json.load(f)

# Function to split the data into smaller parts
def split_json(data, chunk_size):
    chunks = []
    current_chunk = []
    current_size = 0

    for item in data:
        item_size = len(json.dumps(item))  # Estimate the size of the item in bytes

        if current_size + item_size > chunk_size:
            chunks.append(current_chunk)
            current_chunk = [item]
            current_size = item_size
        else:
            current_chunk.append(item)
            current_size += item_size

    if current_chunk:
        chunks.append(current_chunk)

    return chunks

# Split the data into smaller chunks
chunks = split_json(data, chunk_size)

# Save the chunks as separate JSON files
for i, chunk in enumerate(chunks):
    output_filename = f'beta/output_with_stats_simulated_part_{i+1}.json'
    with open(output_filename, 'w') as f:
        json.dump(chunk, f, indent=4)

    print(f'Chunk {i+1} saved as {output_filename}')
