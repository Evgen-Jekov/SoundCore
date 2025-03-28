import requests
from config import API, URL, headers, data

def ask_model(user_TTL):
    data['messages'][0]['content'] = user_TTL
    
    try:
        response = requests.post(URL, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        
        answer = result["choices"][0]["message"]["content"]
        return answer.strip()
    
    except requests.exceptions.RequestException as e:
        return f"Ошибка запроса: {e}"
    except (KeyError, IndexError) as e:
        return "Ошибка: не удалось разобрать ответ API."