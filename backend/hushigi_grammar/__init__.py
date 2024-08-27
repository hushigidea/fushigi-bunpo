import os
import json

def load_data():
  file_path = os.path.join(os.path.dirname(__file__), 'data.json')
  with open(file_path, 'r', encoding='utf-8') as f:
    return json.load(f)
