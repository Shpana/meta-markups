from typing import Callable, TypeVar

from ..markups import (
        wrap_attachment, RuntimeMarkupContext, TTarget
    )


context = RuntimeMarkupContext()


class ShowInConsoleAttribute:
    pass


def show_in_console(target: TTarget) -> Callable:
    return wrap_attachment(
        context, target, ShowInConsoleAttribute())


def should_show_in_console(target: TTarget) -> bool:
    return len(list(
        context.try_get_attributes_with_type(target, ShowInConsoleAttribute))) > 0


class Player:
    
    @show_in_console
    @property
    def health(self) -> float: ...

    @property
    def max_possible_health(self) -> float: ...


TComponent = TypeVar("TComponent")

def show_fields_in_console(component: TComponent) -> None: 
    for key, value in type(component).__dict__.items():
        if should_show_in_console(value):
            print(key)


if __name__ == "__main__":
    player = Player()

    show_fields_in_console(player)
