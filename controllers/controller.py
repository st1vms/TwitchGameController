from typing import Callable, TypeVar

GameControllerType = TypeVar("GameControllerType", bound="GameController")


class GameController:
    controls: dict[str, Callable[..., None]] = {}

    @classmethod
    def register(cls, func: Callable[..., None]) -> Callable[..., None]:
        if not hasattr(cls, "controls"):
            cls.controls = {}
        if func.__name__ not in cls.controls:
            cls.controls[func.__name__] = func
        return func
