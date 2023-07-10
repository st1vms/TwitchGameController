from typing import Callable, TypeVar
import pyautogui
import win32gui

GameControllerType = TypeVar("GameControllerType", bound="GameController")


class GameController:
    controls: dict[str, Callable[..., None]] = {}

    def __init__(self, process_name:str=None, window_title:str=None):
        self._hwnd = win32gui.FindWindow(process_name, window_title)
        if self._hwnd == 0:
            raise ValueError(f"Invalid window title: {window_title}")

    @classmethod
    def register(cls, func: Callable[..., None]) -> Callable[..., None]:
        if not hasattr(cls, "controls"):
            cls.controls = {}
        if func.__name__ not in cls.controls:
            cls.controls[func.__name__] = func
        return func

    async def is_window_in_focus(self) -> bool:
        w = win32gui.GetForegroundWindow()
        return self._hwnd == w

    async def key_down(self, key:str):
        pyautogui.keyDown(key)

    async def key_up(self, key:str):
        pyautogui.keyUp(key)

    async def move_mouse(self, xoff:float, yoff:float):
        mouse_pos = pyautogui.position()
        pyautogui.moveTo( mouse_pos.x+xoff,  mouse_pos.y+yoff, duration=0.5)

    async def left_click(self):
        pyautogui.mouseDown(button='left')
        pyautogui.mouseUp(button='left')

    async def right_click(self):
        pyautogui.mouseDown(button='right')
        pyautogui.mouseUp(button='right')

    async def left_click_down(self):
        pyautogui.mouseDown(button='left')

    async def left_click_up(self):
        pyautogui.mouseUp(button='left')

    async def right_click_down(self):
        pyautogui.mouseDown(button='right')

    async def right_click_up(self):
        pyautogui.mouseUp(button='right')

    async def space_down(self):
        await self.key_down("space")

    async def space_up(self):
        await self.key_up("space")

    async def enter_down(self):
        await self.key_down("enter")

    async def enter_up(self):
        await self.key_up("enter")

    async def ctrl_down(self):
        await self.key_down("ctrl")

    async def ctrl_up(self):
        await self.key_up("ctrl")

    async def shift_down(self):
        await self.key_down("shift")

    async def shift_up(self):
        await self.key_up("shift")

    async def tab_down(self):
        await self.key_down("tab")

    async def tab_up(self):
        await self.key_up("tab")

    async def alt_down(self):
        await self.key_down("alt")

    async def alt_up(self):
        await self.key_up("alt")
