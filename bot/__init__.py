import logging
from urllib.parse import urljoin
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand
from aiogram.utils.chat_action import ChatActionMiddleware

from config import Config

# Constants for Webhook configuration
WEBHOOK_PATH = f"/api/bot/{Config.BOT_TOKEN}"
WEBHOOK_URL = urljoin(Config.WEBHOOK_HOST, WEBHOOK_PATH)
ALLOWED_UPDATES = ["message", "callback_query", "inline_query"]

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    datefmt="%Y/%m/%d %H:%M:%S",
    format="[%(asctime)s][%(name)s][%(levelname)s] ==> %(message)s",
)

# Bot and Dispatcher initialization
bot = Bot(token=Config.BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Middleware setup
dp.message.middleware(ChatActionMiddleware())  # Adds typing and other chat actions
