import json
import nltk
from collections import Counter
import re

def clean_text(text):
    # Step 1: Remove known garbage patterns
    text = re.sub(r'\"[^"]*\.(graphql|react|rendererRef)[^\"]*\"', '', text)  # remove .graphql, .react, .rendererRef
    text = re.sub(r'\\"[^\\"]*\\.(graphql|react|rendererRef)[^\\"]*\\"', '', text)  # for escaped quotes
    text = re.sub(r'css[\]\}\"]+', '', text)  # remove random 'css]]}' junk
    text = re.sub(r'\{.*?\}', '', text, flags=re.DOTALL)  # remove {...}
    text = re.sub(r'\[.*?\]', '', text, flags=re.DOTALL)  # remove [...]
    
    # Step 2: Remove leftover numbers, special chars artifacts
    text = re.sub(r'[0-9]+', '', text)  # remove numbers
    text = re.sub(r'[,\\\[\]\{\}\"]+', ' ', text)  # remove stray brackets and commas
    text = re.sub(r'\s+', ' ', text)  # collapse spaces
    
    # Step 3: Keep only readable ASCII characters
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)  # remove non-ASCII

    return text.strip()

# Step 1: Load output.json fully
with open('output.json', 'r', encoding='utf-8') as f:
    raw_data = f.read()

# Step 2: Quick clean trick to fix embedded JSON garbage
raw_data = raw_data.replace('\n', '').replace('}{', '},{')  # Fix missing commas

# Step 3: Load the clean JSON
data = json.loads(raw_data)

print("Loaded", len(data), "records from output.json")

# Step 4: Download nltk punkt tokenizer
nltk.download('punkt')
import spacy

# Load the English NLP model
nlp = spacy.load('en_core_web_sm')

def named_entities(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities


# Step 5: Define helper functions first
def basic_text_statistics(text):
    words = nltk.word_tokenize(text)
    sentences = nltk.sent_tokenize(text)
    total_words = len(words)
    total_sentences = len(sentences)
    avg_words_per_sentence = total_words / total_sentences if total_sentences > 0 else 0
    return {
        "total_words": total_words,
        "total_sentences": total_sentences,
        "avg_words_per_sentence": avg_words_per_sentence
    }
def most_frequent_verb(text):
    words = nltk.word_tokenize(text)
    pos_tags = nltk.pos_tag(words)
    verbs = [word for word, pos in pos_tags if pos.startswith('VB')]  # VB = Verb
    if verbs:
        most_common_verb = Counter(verbs).most_common(1)[0][0]
    else:
        most_common_verb = None
    return most_common_verb
from textblob import TextBlob

def sentiment_score(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity  # Polarity score between -1 (negative) and +1 (positive)


def most_frequent_noun(text):
    words = nltk.word_tokenize(text)
    pos_tags = nltk.pos_tag(words)
    nouns = [word for word, pos in pos_tags if pos.startswith('NN')]  # NN, NNS, NNP, NNPS
    if nouns:
        most_common_noun = Counter(nouns).most_common(1)[0][0]
    else:
        most_common_noun = None
    return most_common_noun

# Step 6: Apply the functions to each record
for item in data:
    item['text'] = clean_text(item['text'])
    stats = basic_text_statistics(item['text'])
    item['total_words'] = stats['total_words']
    item['total_sentences'] = stats['total_sentences']
    item['avg_words_per_sentence'] = stats['avg_words_per_sentence']
    item['most_frequent_noun'] = most_frequent_noun(item['text'])
    item['most_frequent_verb'] = most_frequent_verb(item['text'])
    item['sentiment_score'] = sentiment_score(item['text'])
    item['named_entities'] = named_entities(item['text'])

# Step 7: Save the updated data
with open('output_with_stats.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)

print("Saved updated data to output_with_stats.json")
