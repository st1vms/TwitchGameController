from twitchAPI import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.types import AuthScope, ChatEvent
from twitchAPI.chat import Chat, EventData, ChatMessage, ChatSub, ChatCommand
import pyautogui
import asyncio
import string
import re
import os
import json
from config import *

COMMANDS_JSON_PATH = os.path.join(os.getcwd(), COMMANDS_JSON_FILENAME)


class GameBotController:
    def __init__(self, creds: dict) -> None:
        self.twitch = None
        self.creds: dict = creds
        self.__USER_SCOPE = [AuthScope.CHAT_READ, AuthScope.CHAT_EDIT]

        self.key_params_pattern = r"(\b\S\b):([\d.]+)"
        self.mouse_coords_pattern = r"(-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?)"

        if os.path.exists(COMMANDS_JSON_PATH):
            with open(COMMANDS_JSON_PATH) as fp:
                self.CUSTOM_COMMANDS = json.load(fp)
        else:
            self.CUSTOM_COMMANDS = {}

        self.window_size = pyautogui.size()

    async def __on_ready(self, ready_event: EventData):
        await ready_event.chat.join_room(self.creds["channel"])
        print("Bot ready!")

    async def __on_message(self, msg: ChatMessage):
        print(f"in {msg.room.name}, {msg.user.name} said: {msg.text}")

    async def __on_sub(self, sub: ChatSub):
        print(
            f"New subscription in {sub.room.name}:\\n"
            f"  Type: {sub.sub_plan}\\n"
            f"  Message: {sub.sub_message}"
        )

    async def call_macro_command(self, cmd: ChatCommand):
        pass

    async def type_key_command(self, cmd: ChatCommand):
        pass

    async def mouse_command(self, cmd: ChatCommand):
        pass

    async def set_key_macro_command(self, cmd: ChatCommand):
        def check_key_macros(macros: tuple) -> bool:
            for m in macros:
                if not m:
                    return False

                if m[0].lower() not in string.printable:
                    return False
                elif m[1] < 0.01 or m[1] > 5:
                    return False
            return True

        user = cmd.user.name

        if not cmd.parameter:
            await cmd.reply(f"{user}: Invalid parameters")
            return

        try:
            aliasname = cmd.parameter.split()[0]
            commands = cmd.parameter[len(aliasname) :].strip()
            if not aliasname or not commands:
                await cmd.reply(f"{user}: Invalid parameters")
                return
        except:
            await cmd.reply(f"{user}: Invalid parameters")
            return
        else:
            matches = re.findall(self.key_params_pattern, commands)
            if not matches or not check_key_macros(matches):
                await cmd.reply(f"{user}: Invalid parameters")
                return

            if cmd.user.name not in self.CUSTOM_COMMANDS:
                self.CUSTOM_COMMANDS[cmd.user.name] = {"key": {}, "mouse": {}}

            elif aliasname in self.CUSTOM_COMMANDS[cmd.user.name]["key"]:
                await cmd.reply(
                    f"{user}: Macro named '{aliasname}' was already created!"
                )
                return

            self.CUSTOM_COMMANDS[cmd.user.name]["key"][aliasname] = matches

            await cmd.reply(f"{user}: Successfully registered macro '{aliasname}'")

    async def set_mouse_macro_command(self, cmd: ChatCommand):
        def check_mouse_macros(macros: tuple) -> bool:
            for m in macros:
                if m[0] < 0 or m[0] > self.window_size[0]:
                    return False
                elif m[1] < 0 or m[1] > self.window_size[1]:
                    return False
            return True

        user = cmd.user.name

        if not cmd.parameter:
            await cmd.reply(f"{user}: Invalid parameters")
            return

        try:
            aliasname = cmd.parameter.split()[0]
            action = cmd.parameter.split()[1]
            commands = cmd.parameter[len(aliasname) :].strip()
            commands = cmd.parameter[len(action) :].strip()

            if (
                (action is not "click" and action is not "move")
                or not aliasname
                or not commands
            ):
                await cmd.reply(f"{user}: Invalid parameters")
                return
        except:
            await cmd.reply(f"{user}: Invalid parameters")
            return
        else:
            matches = re.findall(self.mouse_coords_pattern, commands)
            if not matches or not check_mouse_macros(matches):
                await cmd.reply(f"{user}: Invalid parameters")
                return

            if cmd.user.name not in self.CUSTOM_COMMANDS:
                self.CUSTOM_COMMANDS[cmd.user.name] = {"key": {}, "mouse": {}}

            elif aliasname in self.CUSTOM_COMMANDS[cmd.user.name]["mouse"]:
                await cmd.reply(
                    f"{user}: Macro named '{aliasname}' was already created!"
                )
                return

            self.CUSTOM_COMMANDS[cmd.user.name]["mouse"][aliasname] = (action, matches)

            await cmd.reply(f"{user}: Successfully registered macro '{aliasname}'")

    async def help_command(self, cmd: ChatCommand):
        def _get_page(k: str) -> str:
            return {
                "newkey": NEW_KEY_HELP,
                "newmouse": NEW_MOUSE_HELP,
                "call": CALL_MACRO_HELP,
                "typekey": TYPE_KEY_HELP,
                "mousedo": MOUSE_DO_HELP,
                "showmacros": SHOW_HELP,
                "delmacro": DEL_MACRO_HELP,
            }[cmd.parameter]

        try:
            if not cmd.parameter:
                s = HELP_PAGE
            else:
                s = _get_page(cmd.parameter)
        except:
            await cmd.reply(f"{cmd.user.name}: Invalid command parameter!")
            return
        else:
            await cmd.reply(f"{cmd.user.name}: {cmd.parameter} -> {s}")

    async def delete_macro_command(self, cmd: ChatCommand):
        if cmd.user.name not in self.CUSTOM_COMMANDS:
            await cmd.reply(f"{cmd.user.name}: You have no custom macros saved!")
            return

        k_m = self.CUSTOM_COMMANDS[cmd.user.name]["key"]
        m_m = self.CUSTOM_COMMANDS[cmd.user.name]["mouse"]
        if not k_m and not m_m:
            await cmd.reply(f"{cmd.user.name}: macro not found!")
            return

        aliasname = cmd.parameter.split()[0]
        if aliasname in k_m:
            del self.CUSTOM_COMMANDS[cmd.user.name]["key"][aliasname]
            await cmd.reply(f"{cmd.user.name}: macro {aliasname} removed!")
            return
        elif aliasname in m_m:
            del self.CUSTOM_COMMANDS[cmd.user.name]["mouse"][aliasname]
            await cmd.reply(f"{cmd.user.name}: macro {aliasname} removed!")
            return
        else:
            await cmd.reply(f"{cmd.user.name}: macro {aliasname} not found!")
            return

    async def show_macros_command(self, cmd: ChatCommand):
        if cmd.user.name not in self.CUSTOM_COMMANDS:
            await cmd.reply(f"{cmd.user.name}: You have no custom macros saved!")
            return

        k_m = self.CUSTOM_COMMANDS[cmd.user.name]["key"]
        m_m = self.CUSTOM_COMMANDS[cmd.user.name]["mouse"]
        if not k_m and not m_m:
            await cmd.reply(f"{cmd.user.name}: You have no custom macros saved!")
            return

        s = ""
        if k_m:
            s = f"Keyboard macros: {' '.join(k_m)}\n"

        if m_m:
            s += f" Mouse macros: {' '.join(m_m)}\n"

        await cmd.reply(f"{cmd.user.name}: {s}")

    async def __register_events(self):
        self.chat.register_event(ChatEvent.READY, self.__on_ready)
        # chat.register_event(ChatEvent.MESSAGE, self.on_message)
        # chat.register_event(ChatEvent.SUB, self.on_sub)

        self.chat.register_command("newkey", self.set_key_macro_command)
        self.chat.register_command("newmouse", self.set_mouse_macro_command)
        self.chat.register_command("call", self.call_macro_command)
        self.chat.register_command("typekey", self.type_key_command)
        self.chat.register_command("mousedo", self.mouse_command)
        self.chat.register_command("delmacro", self.delete_macro_command)
        self.chat.register_command("showmacros", self.show_macros_command)
        self.chat.register_command("help", self.help_command)

    async def init_bot(self) -> None:
        self.twitch = await Twitch(self.creds["id"], self.creds["secret"])
        auth = UserAuthenticator(self.twitch, self.__USER_SCOPE)
        token, refresh_token = await auth.authenticate()
        await self.twitch.set_user_authentication(
            token, self.__USER_SCOPE, refresh_token
        )
        self.chat = await Chat(self.twitch)

    async def run(self) -> None:
        await self.__register_events()

        self.chat.start()
        try:
            while True:
                await asyncio.sleep(1)
        except KeyboardInterrupt:
            pass
        finally:
            self.chat.stop()
            await self.twitch.close()

            with open(COMMANDS_JSON_PATH, "w") as fp:
                json.dump(self.CUSTOM_COMMANDS, fp)
