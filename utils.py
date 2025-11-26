import logging
import requests  


logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger()


def get_cat_fact():
    try:
        response = requests.get("https://catfact.ninja/fact")
        return "🐱 Cat fact: " + response.json()["fact"]
    except:
        return "🐱 Cats are awesome!"
