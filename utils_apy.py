import requests

def get_quote():
    url = "https://api.quotable.io/random"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return f"💡 Quote: \"{data['content']}\" — {data['author']}"
    except Exception:
        return "⚠ Could not fetch quote."
