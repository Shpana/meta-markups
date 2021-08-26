from typing import Callable
from dataclasses import dataclass

from markups import apply_option


@dataclass
class AuthorMarkupOption:
    name: str


def author(name: str) -> Callable:
    return lambda target: apply_option(target, AuthorMarkupOption(name))


@dataclass
class TagMakrupOption:
    tag: str


def with_tag(tag: str) -> Callable:
    return lambda target: apply_option(target, TagMakrupOption(tag))