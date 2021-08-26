from typing import Callable, Iterable
from dataclasses import dataclass

from markups import markup_wrapper, RuntimeMarkupContext, TTarget


author_markup_context = RuntimeMarkupContext()


@dataclass
class AuthorMarkupOption:
    name: str


def author(name: str) -> Callable:
    return lambda target: markup_wrapper(
        author_markup_context, target, AuthorMarkupOption(name))


def select_authors(target: TTarget) -> Iterable[AuthorMarkupOption]:
    return author_markup_context.select_options(target, AuthorMarkupOption)
