from typing import Callable, Iterable
from dataclasses import dataclass

from markups import markup_wrapper, RuntimeMarkupContext, TTarget


@dataclass
class AuthorMarkupOption:
    name: str


author_markup_context = RuntimeMarkupContext()


def author(name: str) -> Callable:
    return lambda target: markup_wrapper(
        author_markup_context, target, AuthorMarkupOption(name))


def select_authors(target: TTarget) -> Iterable[AuthorMarkupOption]:
    return author_markup_context.select_options(target, AuthorMarkupOption)


@author("Shpana")
@author("Roman")
class BookAboutDecorators: ...


if __name__ == "__main__":
    for author_option in select_authors(BookAboutDecorators):
        print(author_option)
