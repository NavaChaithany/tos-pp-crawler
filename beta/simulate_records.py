import json
import random
import copy

# Step 1: Load your real output file
with open('output_with_stats.json', 'r', encoding='utf-8') as f:
    real_data = json.load(f)

print(f"Loaded {len(real_data)} real records.")

# Step 2: Create synthetic 50,000 records
simulated_data = []
target_count = 50000

for i in range(target_count):
    base_item = copy.deepcopy(random.choice(real_data))  # Randomly pick a real record
    
    # Minor modifications to make it look unique
    base_item['title'] += f" Copy {i+1}"
    base_item['url'] += f"?id={i+1}"
    base_item['text'] = base_item['text'][:random.randint(200, len(base_item['text']))]  # Randomly shorten text
    base_item['total_words'] += random.randint(-10, 10)  # Small variation
    base_item['total_sentences'] += random.randint(-2, 2)
    base_item['avg_words_per_sentence'] = base_item['total_words'] / max(base_item['total_sentences'], 1)
    
    # Keep noun/verb/sentiment/entities same (fine for simulation)
    simulated_data.append(base_item)

print(f"Generated {len(simulated_data)} simulated records.")

# Step 3: Save into a new file
with open('output_with_stats_simulated.json', 'w', encoding='utf-8') as f:
    json.dump(simulated_data, f, indent=4)

print("Saved simulated 50,000 records to output_with_stats_simulated.json")
