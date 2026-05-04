import asyncio
from client import DiscordClient
from endpoints import (
    get_messages,
    create_message,
    delete_message
)
import os, dotenv
import time

dotenv.load_dotenv()


TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("TEST_CHANNEL_ID")


async def main():
    client = DiscordClient(TOKEN)

    print("---- TEST 1: GET MESSAGES ----")
    messages = await client.get(get_messages(CHANNEL_ID))
    print(messages if isinstance(messages, dict) else f"{len(messages)} messages fetched")

    time.sleep(5)

    print("\n---- TEST 2: SEND MESSAGE ----")
    res = await client.post(
        create_message(CHANNEL_ID),
        json={"content": "MCP test message"}
    )
    print(res)

    # Save message ID for delete test
    message_id = res.get("id") if isinstance(res, dict) else None
    time.sleep(5)
    if message_id:
        print("\n---- TEST 3: DELETE MESSAGE ----")
        delete_res = await client.delete(
            delete_message(CHANNEL_ID, message_id)
        )
        print(delete_res)

    await client.client.aclose()


asyncio.run(main())