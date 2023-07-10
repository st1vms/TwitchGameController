from .controller import *
import asyncio

class MinecraftController(GameController):

    def __init__(self, process_name:str=None, window_title:str="Minecraft 1.20.1 - Singleplayer") -> None:
        super().__init__(process_name=process_name, window_title=window_title)

    @GameController.register
    async def stop(self):
        await self.left_click_up()
        await self.right_click_up()
        await self.shift_up()
        await self.ctrl_up()

    @GameController.register
    async def lclick(self):
        await self.left_click()

    @GameController.register
    async def rclick(self):
        await self.right_click()

    @GameController.register
    async def lpress(self):
        await self.left_click_down()

    @GameController.register
    async def rpress(self):
        await self.right_click_down()

    @GameController.register
    async def w(self):
        await self.key_down("w")
        await asyncio.sleep(0.5)
        await self.key_up("w")

    @GameController.register
    async def s(self):
        await self.key_down("s")
        await asyncio.sleep(0.5)
        await self.key_up("s")

    @GameController.register
    async def a(self):
        await self.key_down("a")
        await asyncio.sleep(0.5)
        await self.key_up("a")

    @GameController.register
    async def d(self):
        await self.key_down("d")
        await asyncio.sleep(0.5)
        await self.key_up("d")

    @GameController.register
    async def e(self):
        await self.key_down("e")
        await self.key_up("e")

    @GameController.register
    async def q(self):
        await self.key_down("q")
        await self.key_up("q")

    @GameController.register
    async def jump(self):
        await self.space_down()
        await self.space_up()

    @GameController.register
    async def ctrl(self):
        await self.ctrl_down()
        await self.ctrl_up()

    @GameController.register
    async def shift(self):
        await self.shift_down()
        await self.shift_up()

    @GameController.register
    async def upless(self):
        await self.move_mouse(0,-50)

    @GameController.register
    async def downless(self):
        await self.move_mouse(0, 50)

    @GameController.register
    async def leftless(self):
        await self.move_mouse(-50,0)

    @GameController.register
    async def rightless(self):
        await self.move_mouse(50, 0)

    @GameController.register
    async def up(self):
        await self.move_mouse(0,-100)

    @GameController.register
    async def down(self):
        await self.move_mouse(0, 100)

    @GameController.register
    async def left(self):
        await self.move_mouse(-100,0)

    @GameController.register
    async def right(self):
        await self.move_mouse(100, 0)

    @GameController.register
    async def turn(self):
        await self.move_mouse(180, 0)

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
