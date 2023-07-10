import os
import json
import asyncio
import traceback
from bot import *
from controllers.controller import *
from controllers.minecraft_controller import *

__CREDS_FILENAME = os.path.join(os.getcwd(), "auth.json")


MAIN_MENU = """
0) Exit
1) Minecraft

>>"""

MENU_CHOICES = (0, 1)


async def get_controller(c: int) -> GameControllerType | None:
    if c == 1:
        return MinecraftController()
    return None


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

        c = 0
        while True:
            try:
                c = int(input(MAIN_MENU).lstrip().rstrip())
                if c not in MENU_CHOICES:
                    print("\nInvalid choice...")
                    continue

                if c == 0:
                    print("Quitting...")
                    return

                break
            except KeyboardInterrupt:
                break
            except:
                print("\nInvalid choice...")

        controller = await get_controller(c)
        bot = GameBotController(creds, controller=controller)
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
