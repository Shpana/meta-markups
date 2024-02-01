from typing import Callable, TypeVar

from ..markups import (
        wrap_attachment, RuntimeMarkupContext, TRealTarget
    )


context = RuntimeMarkupContext()


class ShowInConsoleAttribute:
    pass


def show_in_console(target: TRealTarget) -> Callable:
    return wrap_attachment(
        context, target, ShowInConsoleAttribute())


def should_show_in_console(target: TRealTarget) -> bool:
    return len(list(
        context.try_get_attributes_with_type(target, ShowInConsoleAttribute))) > 0


class Player:
    
    __health: int

    @show_in_console
    @property
    def health(self) -> float: 
        return self.__health

    @show_in_console
    @property
    def max_possible_health(self) -> float: 
        return 100

    def __init__(self) -> None:
        self.__health = self.max_possible_health - 20


TComponent = TypeVar("TComponent")


def show_fields_in_console(component: TComponent) -> None: 
    for key, value in type(component).__dict__.items():
        if isinstance(value, TRealTarget.__bound__):
            if should_show_in_console(value):
                print(f"- {key}={value.fget(component)}")


if __name__ == "__main__":
    player = Player()

    show_fields_in_console(player)
