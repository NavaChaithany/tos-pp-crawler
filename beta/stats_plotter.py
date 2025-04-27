"""
stats_plotter.py
Plots various statistics about text mining results.
"""

import matplotlib.pyplot as plt
from collections import Counter
import random

def plot_word_count_histogram(records):
    """
    Plot histogram of word counts across records.
    """
    word_counts = [len(record.get('text', '').split()) for record in records]
    plt.hist(word_counts, bins=20, color='blue', edgecolor='black')
    plt.title('Word Count Distribution')
    plt.xlabel('Number of Words')
    plt.ylabel('Number of Records')
    plt.grid(True)
    plt.show()

def plot_sentence_count_histogram(records):
    """
    Plot histogram of sentence counts across records.
    """
    sentence_counts = [record.get('total_sentences', 0) for record in records]
    plt.hist(sentence_counts, bins=20, color='green', edgecolor='black')
    plt.title('Sentence Count Distribution')
    plt.xlabel('Number of Sentences')
    plt.ylabel('Number of Records')
    plt.grid(True)
    plt.show()

def plot_top_keywords(records, top_n=10):
    """
    Plot top keywords frequency across all records.
    """
    all_words = []
    for record in records:
        words = record.get('text', '').lower().split()
        all_words.extend(words)

    counter = Counter(all_words)
    most_common = counter.most_common(top_n)

    keywords, counts = zip(*most_common)

    plt.bar(keywords, counts, color='orange')
    plt.xticks(rotation=45)
    plt.title(f'Top {top_n} Keywords')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.grid(axis='y')
    plt.show()

def plot_named_entity_distribution(records):
    """
    Plot pie chart of named entity types found.
    """
    all_entities = []
    for record in records:
        entities = record.get('named_entities', [])
        types = [entity_type for _, entity_type in entities]
        all_entities.extend(types)

    counter = Counter(all_entities)
    labels = list(counter.keys())
    sizes = list(counter.values())

    if labels:
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('Named Entity Distribution')
        plt.axis('equal')
        plt.show()
    else:
        print("No entities found to plot.")

def save_histogram(data, title, filename):
    """
    Save histogram to file.
    """
    plt.hist(data, bins=20, color='purple', edgecolor='black')
    plt.title(title)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.savefig(filename)
    plt.close()
    print(f"Saved histogram to {filename}")

def simulate_dummy_records(n=50):
    """
    Generate dummy records for testing.
    """
    dummy_records = []
    for i in range(n):
        text = "word " * random.randint(50, 500)
        record = {
            "title": f"Dummy {i}",
            "url": f"https://example.com/{i}",
            "text": text,
            "total_sentences": random.randint(5, 50),
            "named_entities": [("ExampleEntity", "ORG")] * random.randint(1, 5)
        }
        dummy_records.append(record)
    return dummy_records

def run_all_plots(records):
    """
    Run all plotting functions.
    """
    print("\nPlotting Word Count Histogram...")
    plot_word_count_histogram(records)

    print("\nPlotting Sentence Count Histogram...")
    plot_sentence_count_histogram(records)

    print("\nPlotting Top Keywords...")
    plot_top_keywords(records)

    print("\nPlotting Named Entity Distribution...")
    plot_named_entity_distribution(records)

    print("\nSaving a Sample Histogram...")
    word_counts = [len(record.get('text', '').split()) for record in records]
    save_histogram(word_counts, "Saved Word Count Histogram", "word_histogram.png")
