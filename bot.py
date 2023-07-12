from twitchAPI import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.types import AuthScope, ChatEvent
from twitchAPI.chat import Chat, EventData, ChatMessage, ChatCommand
import asyncio
from controllers.controller import *


class GameBotController:
    def __init__(self, creds: dict, controller: GameControllerType) -> None:
        self.twitch = None
        self.creds: dict = creds
        self.__USER_SCOPE = [AuthScope.CHAT_READ, AuthScope.CHAT_EDIT]
        self.controller: GameControllerType = controller
        self.HELP_PING_TIMEOUT_SEC = 60*15

    async def __on_ready(self, ready_event: EventData):
        await ready_event.chat.join_room(self.creds["channel"])
        print("Bot ready!")

    async def __on_message(self, msg: ChatMessage):
        text = msg.text.lower().lstrip().rstrip()
        if text in self.controller.controls:
            await self.controller.controls[text]()

    async def __register_events(self):
        self.chat.register_event(ChatEvent.READY, self.__on_ready)
        self.chat.register_event(ChatEvent.MESSAGE, self.__on_message)
        self.chat.register_command("help", self.__help_command)

    async def __help_command(self, cmd: ChatCommand):
        s = "Available controls (type any of these words): "
        for control in self.controller.controls.keys():
            s += f"{control} "
        await cmd.reply(s)

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
            s = "Available controls (type any of these words): "
            for control in self.controller.controls.keys():
                s += f"{control} "

            while True:
                await asyncio.sleep(self.HELP_PING_TIMEOUT_SEC)
                await self.chat.send_message(self.creds["channel"], s)
        except KeyboardInterrupt:
            pass
        finally:
            self.chat.stop()
            await self.twitch.close()
