import requests
from django.conf import settings
from .models import TelegramUser

TOKEN = settings.TELEGRAM_BOT_TOKEN
BASE_URL = f'https://api.telegram.org/bot{TOKEN}'

def get_updates(offset=None):
    url = f"{BASE_URL}/getUpdates"
    params = {'timeout': 100, 'offset': offset}
    response = requests.get(url, params=params)
    return response.json()

def send_message(chat_id, text):
    url = f"{BASE_URL}/sendMessage"
    payload = {'chat_id': chat_id, 'text': text}
    requests.post(url, data=payload)

def handle_updates():
    last_update_id = None
    updates = get_updates(last_update_id)

    for update in updates.get("result", []):
        message = update.get("message", {})
        text = message.get("text", "")
        chat = message.get("chat", {})
        username = chat.get("username")
        first_name = chat.get("first_name")
        last_name = chat.get("last_name")
        chat_id = chat.get("id")

        if text == "/start":
            if not TelegramUser.objects.filter(username=username).exists():
                TelegramUser.objects.create(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    chat_id=chat_id,
                )
                send_message(chat_id, f"Hello {first_name}, you are now registered!")
            else:
                send_message(chat_id, "You're already registered!")

        last_update_id = update["update_id"] + 1
