from typing import Callable, TypeVar
from dataclasses import dataclass

from ..markups import (
        wrap_attachment, RuntimeMarkupContext, TRealTarget
    )


context = RuntimeMarkupContext()


class Color:
    Empty = ''
    Blue = '\033[94m'
    Cyan = '\033[96m'
    Green = '\033[92m'


@dataclass
class ColorAttribute:
    color: str


def with_color(color: str) -> Callable:
    return lambda target: wrap_attachment(
        context, target, ColorAttribute(color))


def apply_color(target: TRealTarget, handle: str) -> str:
    if not context.has_attribute_with_type(target, ColorAttribute):
        return handle
    else:
        color_spec = context.try_get_attributes_with_type(target, ColorAttribute)
        return color_spec[0].color + handle + '\033[0m'


class ShowInConsoleAttribute:
    pass


def show_in_console(target: TRealTarget) -> Callable:
    return wrap_attachment(
        context, target, ShowInConsoleAttribute())


def should_show_in_console(target: TRealTarget) -> bool:
    return context.has_attribute_with_type(target, ShowInConsoleAttribute) 


class Player:
    
    __health: float 
    __damage: float 

    @show_in_console
    @property
    def health(self) -> float: 
        return self.__health

    @show_in_console
    @with_color(Color.Green)
    @property
    def damage(self) -> float:
        return self.__damage

    @show_in_console
    @with_color(Color.Blue)
    @property
    def max_possible_health(self) -> float: 
        return 100.0

    @property
    def some_secret_statistic(self) -> float: ...

    def __init__(self) -> None:
        self.__health = self.max_possible_health - 20.0
        self.__damage = 1.0


TComponent = TypeVar("TComponent")


def show_fields_in_console(component: TComponent) -> None: 
    for key, value in type(component).__dict__.items():
        if isinstance(value, TRealTarget.__bound__):
            if should_show_in_console(value):
                print(f"- {apply_color(value, key)}={value.fget(component)}")


if __name__ == "__main__":
    player = Player()

    show_fields_in_console(player)
