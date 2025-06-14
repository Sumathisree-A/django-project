from django.core.management.base import BaseCommand
from telegram_bot.bot import handle_updates

class Command(BaseCommand):
    help = 'Run Telegram bot to handle /start command'

    def handle(self, *args, **kwargs):
        self.stdout.write("Telegram bot is running... Press Ctrl+C to stop.")
        try:
            while True:
                handle_updates()
        except KeyboardInterrupt:
            self.stdout.write("Bot stopped.")
