from .controller import *
import asyncio

class MinecraftController(GameController):

    def __init__(self, process_name:str=None, window_title:str="Minecraft 1.20.1 - Singleplayer") -> None:
        super().__init__(process_name=process_name, window_title=window_title)

    @GameController.register
    async def leftclick(self):
        await self.left_click()

    @GameController.register
    async def rightclick(self):
        await self.right_click()

    @GameController.register
    async def forward(self):
        await self.key_down("w")
        await asyncio.sleep(0.5)
        await self.key_up("w")

    @GameController.register
    async def back(self):
        await self.key_down("s")
        await asyncio.sleep(0.5)
        await self.key_up("s")

    @GameController.register
    async def left(self):
        await self.key_down("a")
        await asyncio.sleep(0.5)
        await self.key_up("a")

    @GameController.register
    async def right(self):
        await self.key_down("d")
        await asyncio.sleep(0.5)
        await self.key_up("d")

    @GameController.register
    async def inventory(self):
        await self.key_down("e")
        await self.key_up("e")

    @GameController.register
    async def drop(self):
        await self.key_down("q")
        await self.key_up("q")

    @GameController.register
    async def jump(self):
        await self.space_down()
        await asyncio.sleep(0.5)
        await self.space_up()

    @GameController.register
    async def docrouch(self):
        await self.ctrl_down()

    @GameController.register
    async def undocrouch(self):
        await self.ctrl_down()

    @GameController.register
    async def doshift(self):
        await self.shift_down()

    @GameController.register
    async def undoshift(self):
        await self.shift_up()

    @GameController.register
    async def lookupless(self):
        await self.move_mouse(0,-30)

    @GameController.register
    async def lookdownless(self):
        await self.move_mouse(0, 30)

    @GameController.register
    async def lookleftless(self):
        await self.move_mouse(-30,0)

    @GameController.register
    async def lookrightless(self):
        await self.move_mouse(30, 0)

    @GameController.register
    async def lookup(self):
        await self.move_mouse(0,-75)

    @GameController.register
    async def lookdown(self):
        await self.move_mouse(0, 75)

    @GameController.register
    async def lookleft(self):
        await self.move_mouse(-75,0)

    @GameController.register
    async def lookright(self):
        await self.move_mouse(75, 0)

    @GameController.register
    async def turn(self):
        await self.move_mouse(150, 0)

    @GameController.register
    async def slot1(self):
        await self.key_down("1")
        await self.key_up("1")

    @GameController.register
    async def slot2(self):
        await self.key_down("2")
        await self.key_up("2")

    @GameController.register
    async def slot3(self):
        await self.key_down("3")
        await self.key_up("3")

    @GameController.register
    async def slot4(self):
        await self.key_down("4")
        await self.key_up("4")

    @GameController.register
    async def slot5(self):
        await self.key_down("5")
        await self.key_up("5")

    @GameController.register
    async def slot6(self):
        await self.key_down("6")
        await self.key_up("6")

    @GameController.register
    async def slot7(self):
        await self.key_down("7")
        await self.key_up("7")

    @GameController.register
    async def slot8(self):
        await self.key_down("8")
        await self.key_up("8")

    @GameController.register
    async def slot9(self):
        await self.key_down("9")
        await self.key_up("9")
