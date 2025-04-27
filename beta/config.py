"""
config.py
Centralized configuration settings for the project.
"""

# File paths
INPUT_FILE = "output.json"
SIMULATED_FILE = "simulated_output.json"
OUTPUT_FILE = "output_with_stats.json"

# Database file path
DATABASE_FILE = "tosppcrawler.db"

# Simulation settings
DEFAULT_NUM_SIMULATED_RECORDS = 100000

# Text cleaning settings
REMOVE_WINDOW_OBJECTS = True
REMOVE_FUNCTIONS = True
REMOVE_JSON_ARTIFACTS = True
REMOVE_NUMBERS = True

# Sentiment analysis settings
USE_VADER = True

# Web server settings (for api_server.py if needed later)
API_HOST = "127.0.0.1"
API_PORT = 5000
