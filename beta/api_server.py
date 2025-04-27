"""
api_server.py
Simple Flask API to serve TOS/Privacy Policy crawled data.
"""

from flask import Flask, jsonify
from file_utils import load_json_file
import config

app = Flask(__name__)

# Load data once at startup
try:
    data = load_json_file(config.OUTPUT_FILE)
except Exception as e:
    print(f"Failed to load data: {str(e)}")
    data = []

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the TOS/PP Crawler API!"})

@app.route('/records', methods=['GET'])
def get_records():
    """
    Returns all available records.
    """
    return jsonify(data)

@app.route('/record/<int:index>', methods=['GET'])
def get_record(index):
    """
    Returns a single record by index.
    """
    if 0 <= index < len(data):
        return jsonify(data[index])
    else:
        return jsonify({"error": "Invalid index"}), 404

@app.route('/summary/<int:index>', methods=['GET'])
def get_summary(index):
    """
    Returns a summary (100 words + one-sentence) of a record.
    """
    from summarizer import summarize_100_words, summarize_one_sentence

    if 0 <= index < len(data):
        record = data[index]
        text = record.get('text', '')
        summary_100 = summarize_100_words(text)
        summary_one_sentence = summarize_one_sentence(text)
        return jsonify({
            "title": record.get('title', 'Untitled'),
            "summary_100_words": summary_100,
            "summary_one_sentence": summary_one_sentence
        })
    else:
        return jsonify({"error": "Invalid index"}), 404

if __name__ == '__main__':
    app.run(host=config.API_HOST, port=config.API_PORT, debug=True)
