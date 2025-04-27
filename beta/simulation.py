"""
simulation.py
Generate a large simulated dataset to mimic 100,000 crawled records.
"""

import random
import string
from file_utils import save_json_file

def random_sentence(word_count):
    """
    Generates a random sentence with the specified number of words.

    Args:
        word_count (int): Number of words in the sentence.

    Returns:
        str: Randomly generated sentence.
    """
    words = []
    for _ in range(word_count):
        word_length = random.randint(3, 10)
        word = ''.join(random.choices(string.ascii_lowercase, k=word_length))
        words.append(word)
    return " ".join(words) + "."

def random_paragraph(sentence_count):
    """
    Generates a random paragraph with the specified number of sentences.

    Args:
        sentence_count (int): Number of sentences in the paragraph.

    Returns:
        str: Randomly generated paragraph.
    """
    return " ".join(random_sentence(random.randint(5, 15)) for _ in range(sentence_count))

def generate_simulated_records(num_records=100000):
    """
    Generates a list of simulated records.

    Args:
        num_records (int): Number of records to generate.

    Returns:
        list: List of simulated record dictionaries.
    """
    records = []
    for i in range(num_records):
        record = {
            "title": f"Simulated Title {i}",
            "url": f"https://example.com/page{i}",
            "text": random_paragraph(random.randint(5, 20))
        }
        records.append(record)
    return records

def main():
    """
    Main function to generate and save the simulated dataset.
    """
    output_path = "simulated_output.json"
    print("Generating simulated dataset...")
    simulated_data = generate_simulated_records(100000)
    print(f"Saving {len(simulated_data)} simulated records to {output_path}...")
    save_json_file(simulated_data, output_path)
    print("Simulation completed successfully.")

if __name__ == "__main__":
    main()
