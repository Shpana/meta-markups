from typing import Callable
from dataclasses import dataclass

from ..markups import (
        wrap_attachment, RuntimeMarkupContext, TTarget
    )


context = RuntimeMarkupContext()


@dataclass
class AuthorMarkupOption:
    name: str


def author(name: str) -> Callable:
    return lambda target: wrap_attachment(
        context, target, AuthorMarkupOption(name))


def select_authors(target: TTarget) -> tuple[AuthorMarkupOption]:
    return context.try_get_attributes_with_type(target, AuthorMarkupOption)


@author("Shpana")
@author("Roman")
class BookAboutDecorators: ...


if __name__ == "__main__":
    for author_option in select_authors(BookAboutDecorators):
        print(author_option)
