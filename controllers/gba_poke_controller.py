from .controller import *


class GBAPokeController(GameController):
    def __init__(
        self,
        class_name: str = "[CLASS:Qt5153QWindowIcon]",
        window_control: str = "[CLASS:Qt5153QWindowIcon; INSTANCE:1]",
    ) -> None:
        super().__init__(class_name=class_name, window_control=window_control)
        self.register(
            self.a,
            self.b,
            self.up,
            self.down,
            self.left,
            self.right,
            self.select,
            self.start,
            self.lb,
            self.rb,
        )

    async def a(self):
        await self.key_press("a")

    async def b(self):
        await self.key_press("b")

    async def up(self):
        await self.key_press("i")

    async def down(self):
        await self.key_press("k")

    async def left(self):
        await self.key_press("j")

    async def right(self):
        await self.key_press("l")

    async def select(self):
        await self.key_press("q")

    async def start(self):
        await self.key_press("e")

    async def lb(self):
        await self.key_press("1")

    async def rb(self):
        await self.key_press("2")
