from typing import Callable, Iterable, Type
from dataclasses import dataclass

from markups import \
    markup_wrapper, RuntimeMarkupContext, TTarget


commands_context = RuntimeMarkupContext()


@dataclass
class TitleMarkupOption:
    value: str


def title(value: str) -> Callable:
    return lambda target: markup_wrapper(
        commands_context, target, TitleMarkupOption(value))


def select_title(target: TTarget) -> TitleMarkupOption:
    if not commands_context.has_option(target, TitleMarkupOption):
        raise ValueError("Command must contain title.")

    titles = tuple(commands_context.select_options(target, TitleMarkupOption))

    if len(titles) > 1:
        raise ValueError("Command must have only one title.")
    
    return titles[0]


@dataclass
class AliasMarkupOption:
    value: str


def alias(value: str) -> Callable:
    return lambda target: markup_wrapper(
        commands_context, target, AliasMarkupOption(value))


def select_aliases(target: TTarget) -> Iterable[AliasMarkupOption]:
    return commands_context.select_options(target, AliasMarkupOption)


@dataclass
class AttributeMarkupOption:
    name: str
    type: Type


def with_attribute(name: str, type: Type) -> Callable:
    return lambda target: markup_wrapper(
        commands_context, target, AttributeMarkupOption(name, type))


def select_attributes(target: TTarget) -> Iterable[AttributeMarkupOption]:
    if commands_context.has_option(target, AttributeMarkupOption):
        return commands_context.select_options(target, AttributeMarkupOption)
    else:
        return []
 