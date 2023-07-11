from .controller import *

class MinecraftController(GameController):

    def __init__(self, class_name:str='[CLASS:GLFW30]', window_control:str="") -> None:
        super().__init__(class_name=class_name, window_control=window_control)

    async def mouse1click(self):
        await self.left_click()

    async def mouse2click(self):
        await self.right_click()

    async def mouse1down(self):
        await self.left_click_down()

    async def mouse1up(self):
        await self.left_click_up()

    async def mouse2down(self):
        await self.right_click_down()

    async def mouse2up(self):
        await self.right_click_up()

    async def w(self):
        await self.key_press("w")

    async def s(self):
        await self.key_press("s", duration=0.2)

    async def a(self):
        await self.key_press("a", duration=0.2)

    async def d(self):
        await self.key_press("d", duration=0.2)

    async def e(self):
        await self.key_send("e")

    async def q(self):
        await self.key_send("q")

    async def esc(self):
        await self.esc_press()

    async def jump(self):
        await self.space_press()

    async def ctrl(self):
        await self.ctrl_press()

    async def shift(self):
        await self.shift_press()

    async def slot1(self):
        await self.key_send("1")

    async def slot2(self):
        await self.key_send("2")

    async def slot3(self):
        await self.key_send("3")

    async def slot4(self):
        await self.key_send("4")

    async def slot5(self):
        await self.key_send("5")

    async def slot6(self):
        await self.key_send("6")

    async def slot7(self):
        await self.key_send("7")

    async def slot8(self):
        await self.key_send("8")

    async def slot9(self):
        await self.key_send("9")

    async def upless(self):
        await self.left_click()
        await self.move_mouse(0,-50)

    async def downless(self):
        await self.left_click()
        await self.move_mouse(0, 50)

    async def leftless(self):
        await self.left_click()
        await self.move_mouse(-50,0)

    async def rightless(self):
        await self.left_click()
        await self.move_mouse(50, 0)

    async def up(self):
        await self.left_click()
        await self.move_mouse(0,-100)

    async def down(self):
        await self.left_click()
        await self.move_mouse(0, 100)

    async def left(self):
        await self.left_click()
        await self.move_mouse(-100,0)

    async def right(self):
        await self.left_click()
        await self.move_mouse(100, 0)

    async def turn(self):
        await self.left_click()
        await self.move_mouse(180, 0)
