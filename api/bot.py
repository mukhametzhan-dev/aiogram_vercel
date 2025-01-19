from aiohttp.web import Request, json_response
from api import app
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage

import bot.handlers  # Ensure your bot handlers are properly imported
from bot import WEBHOOK_PATH, WEBHOOK_URL, BOT_TOKEN

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(storage=MemoryStorage())

@app.post(WEBHOOK_PATH)
async def bot_webhooks_endpoint(request: Request):
    try:
        # Parse the incoming update
        update_data = await request.json()
        telegram_update = types.Update(**update_data)

        # Process the update
        await dp.process_update(telegram_update)

        # Return a successful response
        return json_response({"status": "ok"})
    except Exception as e:
        # Log and handle any errors
        print(f"Error processing update: {e}")
        return json_response({"status": "error", "message": str(e)}, status=500)
