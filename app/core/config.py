import os
from dotenv import load_dotenv

load_dotenv()

API = os.getenv('API_KEY')
URL = os.getenv('API_URL')

headers = {
        "Authorization": f"Bearer {API}",
        "Content-Type": "application/json"
    }
    
data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": None}],
        "temperature": 0.7
    }

data['messages'][0]['content']