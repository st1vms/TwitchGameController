import os
import json
import asyncio
import traceback
from bot import *

__AUTH_FILENAME = "auth.json"

__CREDS_FILENAME = os.path.join(os.getcwd(), __AUTH_FILENAME)


def __ask_creds() -> dict | None:
    if os.path.exists(__CREDS_FILENAME):
        with open(__CREDS_FILENAME, "r") as fp:
            j = json.load(fp)
            return j

    i = input("\nInsert Twitch App ID\n>>").lstrip().rstrip()
    if not i:
        raise ValueError("\nInvalid App ID...")

    s = input("\nInsert Twitch App secret\n>>").lstrip().rstrip()
    if not s:
        raise ValueError("\nInvalid App secret...")

    c = input("\nInsert Twitch channel name\n>>").lstrip().rstrip()
    if not s:
        raise ValueError("\nInvalid channel name...")

    j = {"id": i, "secret": s, "channel": c}
    with open(__CREDS_FILENAME, "w") as fp:
        json.dump(j, fp, indent=4)

    return j


async def __main() -> None:
    try:
        creds = __ask_creds()
        if not creds:
            raise ValueError("Invalid credentials")

        bot = GameBotController(creds)
        await bot.init_bot()
    except:
        traceback.print_exc()
        print("Invalid Twitch API credentials!")
        return
    else:
        await bot.run()


if __name__ == "__main__":
    try:
        asyncio.run(__main())
    except:
        traceback.print_exc()
