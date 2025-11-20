# srcs/api_exps/mock_data/__init__.py
from pathlib import Path
import json

# Get the directory of the current file
current_dir = Path(__file__).parent

# Build the absolute path to the JSON file
json_path = current_dir / "mock_database.json"

# Load the JSON data
with open(json_path, "r", encoding="utf-8") as f:
    mock_data = json.load(f)