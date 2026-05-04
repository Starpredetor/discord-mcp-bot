import asyncio
from mcp_server.core.executor import MCPExecutor
import os, dotenv
import time

dotenv.load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("TEST_CHANNEL_ID")


async def main():
    executor = MCPExecutor(TOKEN)

    print("---- TEST: MESSAGE_CREATE ----")
    res = await executor.execute(
        "MESSAGE_CREATE",
        {"channel_id": CHANNEL_ID},
        {"content": "Executor route test"}
    )
    print(res)
    time.sleep(5)
    message_id = res.get("id")

    print("\n---- TEST: MESSAGES_GET ----")
    res = await executor.execute(
        "MESSAGES_GET",
        {"channel_id": CHANNEL_ID}
    )
    print(f"Fetched {len(res)} messages")

    if message_id:
        print("\n---- TEST: MESSAGE_FETCH ----")
        res = await executor.execute(
            "MESSAGE_FETCH",
            {
                "channel_id": CHANNEL_ID,
                "message_id": message_id
            }
        )
        print(res["content"])

        print("\n---- TEST: MESSAGE_EDIT ----")
        res = await executor.execute(
            "MESSAGE_EDIT",
            {
                "channel_id": CHANNEL_ID,
                "message_id": message_id
            },
            {"content": "Edited message"}
        )
        print(res["content"])
        time.sleep(5)
        print("\n---- TEST: MESSAGE_DELETE ----")
        res = await executor.execute(
            "MESSAGE_DELETE",
            {
                "channel_id": CHANNEL_ID,
                "message_id": message_id
            }
        )
        print(res)

asyncio.run(main())