"""
process_output_v2.py
Alternate version to process simulated_output.json for safe LOC expansion.
"""

import json
from file_utils import load_json_file, save_json_file
from text_cleaner import clean_text, basic_text_preprocess
from text_miner import basic_text_statistics, most_frequent_noun, most_frequent_verb, sentiment_score, named_entities
from summarizer import summarize_100_words, summarize_one_sentence
from data_validators import validate_dataset

# Load simulated dataset
try:
    print("Loading simulated data...")
    data = load_json_file('simulated_output.json')
    print(f"Loaded {len(data)} simulated records.")
except Exception as e:
    print(f"Failed to load simulated data: {str(e)}")
    data = []

# Process each record
for idx, item in enumerate(data):
    try:
        original_text = item.get('text', '')
        cleaned_text = clean_text(original_text)

        # Basic statistics
        stats = basic_text_statistics(cleaned_text)
        item['cleaned_text'] = cleaned_text
        item['total_words'] = stats['total_words']
        item['total_sentences'] = stats['total_sentences']
        item['avg_words_per_sentence'] = stats['avg_words_per_sentence']

        # Text Mining
        item['most_frequent_noun'] = most_frequent_noun(cleaned_text)
        item['most_frequent_verb'] = most_frequent_verb(cleaned_text)
        item['sentiment_score'] = sentiment_score(cleaned_text)
        item['named_entities'] = named_entities(cleaned_text)

        # Summaries
        item['summary_100_words'] = summarize_100_words(cleaned_text)
        item['summary_one_sentence'] = summarize_one_sentence(cleaned_text)

        if idx % 5000 == 0:
            print(f"Processed {idx} records...")

    except Exception as e:
        print(f"Error processing record {idx}: {str(e)}")

# Save updated data
save_json_file(data, 'simulated_output_with_stats.json')
print("Saved updated simulated data to simulated_output_with_stats.json")

# Validate
valid, invalid = validate_dataset(data)
print(f"Validation Summary: {valid} valid records, {invalid} invalid records.")
