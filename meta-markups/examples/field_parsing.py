from typing import Callable, NoReturn, TypeVar

from markups import markup_wrapper, BetterRuntimeMarkupContext, TTarget


markup_context = BetterRuntimeMarkupContext()


class ShowInInspectorMarkupOption:
    pass


def show_in_inspector(target: TTarget) -> Callable:
    return markup_wrapper(
        markup_context, target, ShowInInspectorMarkupOption())


def should_show_in_inspector(target: TTarget) -> bool:
    return len(list(
        markup_context.select_options(target, ShowInInspectorMarkupOption))) > 0


class Player:
    
    @show_in_inspector
    @property
    def health(self) -> float: ...

    @property
    def max_possible_health(self) -> float: ...


TComponent = TypeVar("TComponent")

def show_component_in_console(component: TComponent) -> NoReturn: 
    for key, value in type(component).__dict__.items():
        if should_show_in_inspector(value):
            print(key)


if __name__ == "__main__":
    player = Player()

    show_component_in_console(player)
