import sqlite3
import re
from collections import Counter

def load_text():
    conn = sqlite3.connect("tosppcrawler/tospp_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT text FROM tos_data")
    text_data = cursor.fetchall()
    conn.close()
    return ' '.join([row[0] for row in text_data])

def clean_and_tokenize(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)  # remove punctuation
    words = text.split()
    return words

if __name__ == "__main__":
    raw_text = load_text()
    tokens = clean_and_tokenize(raw_text)
    word_freq = Counter(tokens)

    print("Top 10 most common words:")
    for word, freq in word_freq.most_common(10):
        print(f"{word}: {freq}")
# Generate a simple one-sentence summary (naive approach)
summary_sentence = "This Terms of Service page emphasizes topics like " + ', '.join(
    [word for word, freq in word_freq.most_common(5)]
) + "."

print("\nOne-sentence summary:")
print(summary_sentence)

# Generate a 100-word summary (naive approach using word frequency)
important_words = set([word for word, freq in word_freq.most_common(20)])
summary_tokens = [word for word in tokens if word in important_words][:100]
summary_100 = ' '.join(summary_tokens)

print("\n100-word summary:")
print(summary_100)
