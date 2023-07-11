from typing import Callable, TypeVar
import autoit
import time


GameControllerType = TypeVar("GameControllerType", bound="GameController")


class GameController:
    controls: dict[str, Callable[..., None]] = {}

    def __init__(self, class_name:str="", window_control:str=""):
        self.window_control = window_control
        self.class_name = class_name

    def register(self, *funcs: Callable[..., None]) :
        if not hasattr(self, "controls"):
            self.controls = {}

        for func in funcs:
            if func.__name__ not in self.controls:
                self.controls[func.__name__] = func

    async def get_window_center(self) -> tuple[float, float]:
        x1,y1,x2,y2 = autoit.win_get_pos(self.class_name)
        center_x = x1 + ((x2 - x1) // 2)
        center_y = y1 + ((y2 - y1) // 2)
        return (center_x, center_y)

    async def key_press(self, key, duration:float=0.1):
        t = time.time() + (duration)
        while time.time() <= t:
            autoit.control_send(self.class_name, self.window_control, key, down=True)
        autoit.control_send(self.class_name, self.window_control, key, up=True)

    async def key_send(self, key):
        autoit.control_send(self.class_name, self.window_control, key)

    async def space_press(self, duration:float=0.1):
        await self.key_send('{SPACE}')

    async def enter_press(self, duration:float=0.1):
        await self.key_send('{ENTER}')

    async def ctrl_press(self, duration:float=0.1):
        await self.key_send('{CTRL}')

    async def shift_press(self, duration:float=0.1):
        await self.key_send('{SHIFT}')

    async def tab_press(self, duration:float=0.1):
        await self.key_send('{TAB}')

    async def esc_press(self, duration:float=0.1):
        await self.key_send('{ESC}')

    async def move_mouse(self, xoff:float=0.0, yoff:float=0.0):
        x,y = await self.get_window_center()
        autoit.mouse_move(x, y, 0)
        if xoff != 0 or yoff != 0:
            print(f"moving to {x} {y}")
            autoit.mouse_move(x+xoff, y+yoff, 25)

    async def left_click(self, x:float=-1, y:float=-1):
        if x == -1 or y == -1:
            x,y = await self.get_window_center()
        autoit.mouse_click("left", x, y, 1, 0)

    async def right_click(self, x:float=-1, y:float=-1):
        if x == -1 or y == -1:
            x,y = await self.get_window_center()
        autoit.mouse_click("right", x, y, 1, 0)

    async def left_click_down(self):
        autoit.mouse_down("left")

    async def left_click_up(self):
        autoit.mouse_up("left")

    async def right_click_down(self):
        autoit.mouse_down("right")

    async def right_click_up(self):
        autoit.mouse_up("right")
